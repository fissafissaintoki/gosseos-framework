import { useEffect, useState } from 'react';

import { StepIndicator, type AppStep } from '../components/StepIndicator';
import { WorkbenchLayout } from '../components/WorkbenchLayout';
import { useCase } from '../hooks/useCase';
import { useRouting } from '../hooks/useRouting';
import { executeCase, reviewIntegrity } from '../services/api';
import { InputScreen } from '../screens/InputScreen';
import { OutputScreen } from '../screens/OutputScreen';
import { RoutingScreen } from '../screens/RoutingScreen';
import type { IntegrityResult, OutputRecord, RoutingOverride } from '../types';

const defaultOverride: RoutingOverride = {
  problem_class: 'analysis',
  mode: 'Build',
  depth: 'Standard',
  artifact_type: 'report',
  governance_relevance: false,
};

export default function App() {
  const [currentStep, setCurrentStep] = useState<AppStep>('input');
  const caseFlow = useCase();
  const routingFlow = useRouting();
  const [override, setOverride] = useState<RoutingOverride>(defaultOverride);
  const [output, setOutput] = useState<OutputRecord | null>(null);
  const [integrity, setIntegrity] = useState<IntegrityResult | null>(null);
  const [outputLoading, setOutputLoading] = useState(false);
  const [reviewLoading, setReviewLoading] = useState(false);
  const [outputError, setOutputError] = useState<string | null>(null);

  useEffect(() => {
    if (routingFlow.routing) {
      setOverride({
        problem_class: routingFlow.routing.problem_class,
        mode: routingFlow.routing.mode,
        depth: routingFlow.routing.depth,
        artifact_type: routingFlow.routing.artifact_type,
        governance_relevance: routingFlow.routing.governance_relevance,
      });
    }
  }, [routingFlow.routing]);

  async function handleCreateCase() {
    const createdCaseId = await caseFlow.submitCase();
    await routingFlow.fetchRouting(createdCaseId);
    setCurrentStep('routing');
  }

  async function handleApplyOverride() {
    if (!caseFlow.caseId) return;
    await routingFlow.overrideRouting(caseFlow.caseId, override);
  }

  async function handleContinueToOutput() {
    setCurrentStep('output');
    if (!output && caseFlow.caseId) {
      await handleExecute();
    }
  }

  async function handleExecute() {
    if (!caseFlow.caseId) return;
    setOutputLoading(true);
    setOutputError(null);
    setIntegrity(null);
    try {
      const result = await executeCase(caseFlow.caseId);
      setOutput(result);
    } catch (err) {
      setOutputError(err instanceof Error ? err.message : 'Execution failed');
    } finally {
      setOutputLoading(false);
    }
  }

  async function handleReview() {
    if (!output) return;
    setReviewLoading(true);
    setOutputError(null);
    try {
      const result = await reviewIntegrity(output.output_id);
      setIntegrity(result);
    } catch (err) {
      setOutputError(err instanceof Error ? err.message : 'Integrity review failed');
    } finally {
      setReviewLoading(false);
    }
  }

  return (
    <WorkbenchLayout>
      <StepIndicator currentStep={currentStep} />

      {currentStep === 'input' ? (
        <InputScreen
          title={caseFlow.title}
          rawInput={caseFlow.rawInput}
          contextNotes={caseFlow.contextNotes}
          desiredOutcome={caseFlow.desiredOutcome}
          loading={caseFlow.loading}
          error={caseFlow.error}
          onTitleChange={caseFlow.setTitle}
          onRawInputChange={caseFlow.setRawInput}
          onContextNotesChange={caseFlow.setContextNotes}
          onDesiredOutcomeChange={caseFlow.setDesiredOutcome}
          onSubmit={handleCreateCase}
          onClear={caseFlow.clear}
        />
      ) : null}

      {currentStep === 'routing' ? (
        <RoutingScreen
          routing={routingFlow.routing}
          loading={routingFlow.loading}
          error={routingFlow.error}
          override={override}
          onOverrideChange={setOverride}
          onApplyOverride={handleApplyOverride}
          onContinue={handleContinueToOutput}
        />
      ) : null}

      {currentStep === 'output' ? (
        <OutputScreen
          output={output}
          integrity={integrity}
          loading={outputLoading}
          reviewLoading={reviewLoading}
          error={outputError}
          onExecute={handleExecute}
          onReview={handleReview}
        />
      ) : null}
    </WorkbenchLayout>
  );
}
