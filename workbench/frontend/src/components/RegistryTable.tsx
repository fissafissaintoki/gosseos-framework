import type { ArtifactRecord } from '../types';

export function RegistryTable({ artifacts, onSelect }: { artifacts: ArtifactRecord[]; onSelect?: (artifactId: string) => void }) {
  return (
    <div style={{ background: '#111827', border: '1px solid #334155', borderRadius: 16, padding: 18 }}>
      <h3 style={{ marginTop: 0 }}>Registry</h3>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={{ textAlign: 'left', padding: '10px 8px', color: '#94a3b8' }}>Title</th>
            <th style={{ textAlign: 'left', padding: '10px 8px', color: '#94a3b8' }}>Status</th>
            <th style={{ textAlign: 'left', padding: '10px 8px', color: '#94a3b8' }}>Mode</th>
            <th style={{ textAlign: 'left', padding: '10px 8px', color: '#94a3b8' }}>Type</th>
          </tr>
        </thead>
        <tbody>
          {artifacts.map((artifact) => (
            <tr
              key={artifact.artifact_id}
              onClick={() => onSelect?.(artifact.artifact_id)}
              style={{ cursor: onSelect ? 'pointer' : 'default', borderTop: '1px solid #1f2937' }}
            >
              <td style={{ padding: '10px 8px' }}>{artifact.title}</td>
              <td style={{ padding: '10px 8px' }}>{artifact.status}</td>
              <td style={{ padding: '10px 8px' }}>{artifact.mode}</td>
              <td style={{ padding: '10px 8px' }}>{artifact.artifact_type}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
