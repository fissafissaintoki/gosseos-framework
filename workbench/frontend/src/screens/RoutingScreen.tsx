import type { RoutingOverride, RoutingRecord } from '../types';
import { RoutingCard } from '../components/RoutingCard';

type RoutingScreenProps = {
  routing: RoutingRecord | null;
  loading: boolean;
  error: string | null;
  override: RoutingOverride;
  onOverrideChange: (next: RoutingOverride) => void;
  onApplyOverride: () => void;
  onContinue: () => void;
};

const problemClasses = ['analysis', 'planning', 'decision_support', 'documentation', 'communication', 'governance_risk', 'creative_development'];
const modes = ['Architect', 'Build', 'Audit', 'Red Team', 'Briefing'];
const depths = ['Direct', 'Compact', 'Standard', 'Endboss'];
const artifactTypes = ['one-pager', 'dossier', 'SOP', 'report', 'post', 'framework', 'prompt', 'briefing_note', 'registry_entry'];

function fieldStyle(): React.CSSProperties {
  return {
    width: '100%',
    padding: '10px 12px',
    borderRadius: 10,
    border: '1px solid #334155',
    background: '#0f172a',
    color: '#f8fafc',
  };
}

export function RoutingScreen(props: RoutingScreenProps) {
  return (
    <div style={{ display: 'grid', gap: 18 }}>
      {props.routing ? <RoutingCard routing={props.routing} /> : null}
      <div style={{ background: '#111827', border: '1px solid #334155', borderRadius: 16, padding: 20 }}>
        <h2 style={{ marginTop: 0 }}>Routing Override</h2>
        <p style={{ color: '#94a3b8' }}>Falls nötig, Routing manuell härten und danach in die Ausführung gehen.</p>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, minmax(0, 1fr))', gap: 14 }}>
          <select value={props.override.problem_class} onChange={(e) => props.onOverrideChange({ ...props.override, problem_class: e.target.value as RoutingOverride['problem_class'] })} style={fieldStyle()}>
            {problemClasses.map((value) => <option key={value} value={value}>{value}</option>)}
          </select>
          <select value={props.override.mode} onChange={(e) => props.onOverrideChange({ ...props.override, mode: e.target.value as RoutingOverride['mode'] })} style={fieldStyle()}>
            {modes.map((value) => <option key={value} value={value}>{value}</option>)}
          </select>
          <select value={props.override.depth} onChange={(e) => props.onOverrideChange({ ...props.override, depth: e.target.value as RoutingOverride['depth'] })} style={fieldStyle()}>
            {depths.map((value) => <option key={value} value={value}>{value}</option>)}
          </select>
          <select value={props.override.artifact_type} onChange={(e) => props.onOverrideChange({ ...props.override, artifact_type: e.target.value as RoutingOverride['artifact_type'] })} style={fieldStyle()}>
            {artifactTypes.map((value) => <option key={value} value={value}>{value}</option>)}
          </select>
        </div>
        <label style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 14 }}>
          <input type="checkbox" checked={props.override.governance_relevance} onChange={(e) => props.onOverrideChange({ ...props.override, governance_relevance: e.target.checked })} />
          Governance relevant
        </label>
        {props.error ? <div style={{ color: '#fca5a5', marginTop: 12 }}>{props.error}</div> : null}
        <div style={{ display: 'flex', gap: 12, marginTop: 16 }}>
          <button onClick={props.onApplyOverride} disabled={props.loading} style={{ padding: '10px 14px', borderRadius: 12, border: '1px solid #60a5fa', background: '#1d4ed8', color: '#fff', fontWeight: 700 }}>
            {props.loading ? 'Arbeite...' : 'Override anwenden'}
          </button>
          <button onClick={props.onContinue} disabled={!props.routing || props.loading} style={{ padding: '10px 14px', borderRadius: 12, border: '1px solid #334155', background: '#0f172a', color: '#fff', fontWeight: 700 }}>
            Weiter zur Ausführung
          </button>
        </div>
      </div>
    </div>
  );
}
