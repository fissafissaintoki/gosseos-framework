import type { PropsWithChildren } from 'react';

export function WorkbenchLayout({ children }: PropsWithChildren) {
  return (
    <div style={{ minHeight: '100vh', background: '#0b1220', color: '#f5f7fb', fontFamily: 'Inter, Arial, sans-serif' }}>
      <header style={{ borderBottom: '1px solid #1f2a44', padding: '20px 24px', background: '#0f172a' }}>
        <div style={{ maxWidth: 1100, margin: '0 auto' }}>
          <h1 style={{ margin: 0, fontSize: 28 }}>GosseOS Workbench</h1>
          <p style={{ margin: '8px 0 0', color: '#94a3b8' }}>
            Raw Input - Routing - Output
          </p>
        </div>
      </header>
      <main style={{ maxWidth: 1100, margin: '0 auto', padding: 24 }}>{children}</main>
    </div>
  );
}
