export function OutputSection({ title, content }: { title: string; content?: string | null }) {
  return (
    <section style={{ background: '#111827', border: '1px solid #334155', borderRadius: 16, padding: 18, marginBottom: 16 }}>
      <h3 style={{ marginTop: 0 }}>{title}</h3>
      <div style={{ whiteSpace: 'pre-wrap', lineHeight: 1.5, color: '#e5e7eb' }}>
        {content && content.trim() ? content : '-'}
      </div>
    </section>
  );
}
