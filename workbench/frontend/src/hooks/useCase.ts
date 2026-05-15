import { useState } from 'react';

import { createCase } from '../services/api';

export function useCase() {
  const [title, setTitle] = useState('');
  const [rawInput, setRawInput] = useState('');
  const [contextNotes, setContextNotes] = useState('');
  const [desiredOutcome, setDesiredOutcome] = useState('');
  const [caseId, setCaseId] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submitCase() {
    setLoading(true);
    setError(null);
    try {
      const created = await createCase({
        title: title || undefined,
        raw_input: rawInput,
        context_notes: contextNotes || undefined,
        desired_outcome: desiredOutcome || undefined,
      });
      setCaseId(created.case_id);
      return created.case_id;
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Unknown error';
      setError(message);
      throw err;
    } finally {
      setLoading(false);
    }
  }

  function clear() {
    setTitle('');
    setRawInput('');
    setContextNotes('');
    setDesiredOutcome('');
    setCaseId(null);
    setError(null);
  }

  return {
    title,
    rawInput,
    contextNotes,
    desiredOutcome,
    caseId,
    loading,
    error,
    setTitle,
    setRawInput,
    setContextNotes,
    setDesiredOutcome,
    submitCase,
    clear,
  };
}
