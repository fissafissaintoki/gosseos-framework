import type { ArtifactCreate } from '../types';

type RegistrySaveScreenProps = {
  form: ArtifactCreate;
  loading: boolean;
  error: string | null;
  onChange: (next: ArtifactCreate) => void;
  onSave: () => void;
};

function fieldStyle(): React.CSSProperties {
  return {
    width: '100%',
    padding: '10px 12px',
    borderRadius: 10,
    border: '1px solid #334155',
    background: '#0f172a',
    color: '#f8fafc',
    boxSizing: 'border-box',
  };
}

export function RegistrySaveScreen(props: RegistrySaveScreenProps) {
  return (
    <div style={{ background: '#111827', border: '1px solid #334155', borderRadius: 16, padding: 20 }}>
      <h2 style={{ marginTop: 0 }}>Save Artifact</h2>
      <div style={{ display: 'grid', gap: 14 }}>
        <input value={props.form.title} onChange={(e) => props.onChange({ ...props.form, title: e.target.value })} placeholder="Title" style={fieldStyle()} />
        <input value={props.form.domain} onChange={(e) => props.onChange({ ...props.form, domain: e.target.value })} placeholder="Domain" style={fieldStyle()} />
        <input value={props.form.purpose} onChange={(e) => props.onChange({ ...props.form, purpose: e.target.value })} placeholder="Purpose" style={fieldStyle()} />
        <input value={props.form.assumption_level} onChange={(e) => props.onChange({ ...props.form, assumption_level: e.target.value })} placeholder="Assumption Level" style={fieldStyle()} />
        <input value={props.form.integrity_status} onChange={(e) => props.onChange({ ...props.form, integrity_status: e.target.value })} placeholder="Integrity Status" style={fieldStyle()} />
        <textarea value={props.form.reuse_notes ?? ''} onChange={(e) => props.onChange({ ...props.form, reuse_notes: e.target.value })} placeholder="Reuse Notes" style={{ ...fieldStyle(), minHeight: 100, resize: 'vertical' }} />
      </div>
      {props.error ? <div style={{ color: '#fca5a5', marginTop: 12 }}>{props.error}</div> : null}
      <div style={{ marginTop: 16 }}>
        <button onClick={props.onSave} disabled={props.loading} style={{ padding: '10px 14px', borderRadius: 12, border: '1px solid #60a5fa', background: '#2563eb', color: '#fff', fontWeight: 700 }}>
          {props.loading ? 'Speichere...' : 'Artifact speichern'}
        </button>
      </div>
    </div>
  );
}
