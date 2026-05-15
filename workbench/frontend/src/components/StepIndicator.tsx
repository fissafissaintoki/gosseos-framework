type AppStep = 'input' | 'routing' | 'output';

const STEPS: AppStep[] = ['input', 'routing', 'output'];

export function StepIndicator({ currentStep }: { currentStep: AppStep }) {
  return (
    <div style={{ display: 'flex', gap: 12, marginBottom: 24 }}>
      {STEPS.map((step, index) => {
        const active = step === currentStep;
        return (
          <div
            key={step}
            style={{
              padding: '10px 14px',
              borderRadius: 12,
              background: active ? '#2563eb' : '#111827',
              border: `1px solid ${active ? '#60a5fa' : '#334155'}`,
              color: active ? '#fff' : '#cbd5e1',
              minWidth: 120,
            }}
          >
            <div style={{ fontSize: 12, opacity: 0.8 }}>Step {index + 1}</div>
            <div style={{ textTransform: 'capitalize', fontWeight: 700 }}>{step}</div>
          </div>
        );
      })}
    </div>
  );
}

export type { AppStep };
