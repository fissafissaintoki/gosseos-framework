import type { IntegrityResult, ParseStatus } from '../types';

export function IntegrityStrip({ parseStatus, integrity }: { parseStatus: ParseStatus; integrity?: IntegrityResult | null }) {
  const color = parseStatus === 'ok' ? '#16a34a' : parseStatus === 'repaired' ? '#f59e0b' : '#dc2626';

  return (
    <div style={{ background: '#0f172a', border: `1px solid ${color}`, borderRadius: 12, padding: 14, marginBottom: 16 }}>
      <div style={{ fontWeight: 700 }}>Parse Status: <span style={{ color }}>{parseStatus}</span></div>
      {integrity ? (
        <div style={{ marginTop: 8, color: '#cbd5e1' }}>
          Drift: {String(integrity.drift)} | Hallucination Risk: {String(integrity.hallucination_risk)} | Artifact Mismatch: {String(integrity.artifact_mismatch)}
          {integrity.note ? <div style={{ marginTop: 8 }}>{integrity.note}</div> : null}
        </div>
      ) : null}
    </div>
  );
}
