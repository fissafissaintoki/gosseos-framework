import type { RoutingRecord } from '../types';

export function RoutingCard({ routing }: { routing: RoutingRecord }) {
  const rows = [
    ['Problem Class', routing.problem_class],
    ['Mode', routing.mode],
    ['Depth', routing.depth],
    ['Artifact Type', routing.artifact_type],
    ['Governance', String(routing.governance_relevance)],
    ['Route Source', routing.route_source],
    ['Confidence', routing.confidence_score == null ? '-' : String(routing.confidence_score)],
  ];

  return (
    <div style={{ background: '#111827', border: '1px solid #334155', borderRadius: 16, padding: 18 }}>
      <h3 style={{ marginTop: 0 }}>Routing</h3>
      <div style={{ display: 'grid', gridTemplateColumns: '180px 1fr', gap: 10 }}>
        {rows.map(([label, value]) => (
          <>
            <div key={`${label}-label`} style={{ color: '#94a3b8' }}>{label}</div>
            <div key={`${label}-value`} style={{ fontWeight: 700 }}>{value}</div>
          </>
        ))}
      </div>
    </div>
  );
}
