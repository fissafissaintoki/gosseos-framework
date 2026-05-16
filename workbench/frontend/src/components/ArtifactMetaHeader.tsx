import type { ArtifactRecord } from '../types';

export function ArtifactMetaHeader({ artifact }: { artifact: ArtifactRecord }) {
  return (
    <div style={{ background: '#111827', border: '1px solid #334155', borderRadius: 16, padding: 18, marginBottom: 16 }}>
      <h3 style={{ marginTop: 0, marginBottom: 10 }}>{artifact.title}</h3>
      <div style={{ display: 'grid', gridTemplateColumns: '180px 1fr', gap: 8 }}>
        <div style={{ color: '#94a3b8' }}>Status</div><div>{artifact.status}</div>
        <div style={{ color: '#94a3b8' }}>Version</div><div>{artifact.version}</div>
        <div style={{ color: '#94a3b8' }}>Mode</div><div>{artifact.mode}</div>
        <div style={{ color: '#94a3b8' }}>Depth</div><div>{artifact.depth}</div>
        <div style={{ color: '#94a3b8' }}>Artifact Type</div><div>{artifact.artifact_type}</div>
        <div style={{ color: '#94a3b8' }}>Domain</div><div>{artifact.domain}</div>
      </div>
    </div>
  );
}
