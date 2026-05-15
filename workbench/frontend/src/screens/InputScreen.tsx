type InputScreenProps = {
  title: string;
  rawInput: string;
  contextNotes: string;
  desiredOutcome: string;
  loading: boolean;
  error: string | null;
  onTitleChange: (value: string) => void;
  onRawInputChange: (value: string) => void;
  onContextNotesChange: (value: string) => void;
  onDesiredOutcomeChange: (value: string) => void;
  onSubmit: () => void;
  onClear: () => void;
};

function fieldStyle(multiline = false): React.CSSProperties {
  return {
    width: '100%',
    padding: '12px 14px',
    borderRadius: 12,
    border: '1px solid #334155',
    background: '#0f172a',
    color: '#f8fafc',
    fontSize: 14,
    minHeight: multiline ? 120 : undefined,
    resize: multiline ? 'vertical' : undefined,
    boxSizing: 'border-box',
  };
}

function labelStyle(): React.CSSProperties {
  return {
    display: 'block',
    marginBottom: 8,
    fontWeight: 700,
    color: '#cbd5e1',
  };
}

function buttonStyle(primary = false): React.CSSProperties {
  return {
    padding: '12px 16px',
    borderRadius: 12,
    border: primary ? '1px solid #60a5fa' : '1px solid #334155',
    background: primary ? '#2563eb' : '#111827',
    color: '#f8fafc',
    fontWeight: 700,
    cursor: 'pointer',
  };
}

export function InputScreen(props: InputScreenProps) {
  return (
    <div style={{ display: 'grid', gap: 18 }}>
      <div style={{ background: '#111827', border: '1px solid #334155', borderRadius: 16, padding: 20 }}>
        <h2 style={{ marginTop: 0 }}>Input</h2>
        <p style={{ color: '#94a3b8' }}>Rohinput sauber erfassen, bevor Routing und Ausführung starten.</p>

        <div style={{ display: 'grid', gap: 16 }}>
          <div>
            <label style={labelStyle()}>Titel</label>
            <input value={props.title} onChange={(e) => props.onTitleChange(e.target.value)} style={fieldStyle()} />
          </div>

          <div>
            <label style={labelStyle()}>Rohinput</label>
            <textarea value={props.rawInput} onChange={(e) => props.onRawInputChange(e.target.value)} style={fieldStyle(true)} />
          </div>

          <div>
            <label style={labelStyle()}>Kontext</label>
            <textarea value={props.contextNotes} onChange={(e) => props.onContextNotesChange(e.target.value)} style={fieldStyle(true)} />
          </div>

          <div>
            <label style={labelStyle()}>Desired Outcome</label>
            <textarea value={props.desiredOutcome} onChange={(e) => props.onDesiredOutcomeChange(e.target.value)} style={fieldStyle(true)} />
          </div>
        </div>

        {props.error ? <div style={{ marginTop: 16, color: '#fca5a5' }}>{props.error}</div> : null}

        <div style={{ display: 'flex', gap: 12, marginTop: 20 }}>
          <button onClick={props.onSubmit} disabled={props.loading || !props.rawInput.trim()} style={buttonStyle(true)}>
            {props.loading ? 'Analysiere...' : 'Analysieren'}
          </button>
          <button onClick={props.onClear} disabled={props.loading} style={buttonStyle(false)}>
            Leeren
          </button>
        </div>
      </div>
    </div>
  );
}
