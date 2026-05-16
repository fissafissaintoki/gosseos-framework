import { ArtifactMetaHeader } from '../components/ArtifactMetaHeader';
import type { ArtifactRecord } from '../types';

export function ArtifactViewScreen({ artifact, content }: { artifact: ArtifactRecord | null; content?: unknown }) {
  if (!artifact) {
    return (
      <div style={{ background: '#111827', border: '1px solid #334155', borderRadius: 16, padding: 20, color: '#94a3b8' }}>
        Kein Artifact geladen.
      </div>
    );
  }

  return (
    <div>
      <ArtifactMetaHeader artifact={artifact} />
      <div style={{ background: '#111827', border: '1px solid #334155', borderRadius: 16, padding: 18 }}>
        <h3 style={{ marginTop: 0 }}>Content</h3>
        <pre style={{ whiteSpace: 'pre-wrap', margin: 0, color: '#e5e7eb' }}>{JSON.stringify(content ?? {}, null, 2)}</pre>
      </div>
    </div>
  );
}
