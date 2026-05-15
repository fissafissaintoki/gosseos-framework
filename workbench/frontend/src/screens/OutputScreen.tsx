import type { IntegrityResult, OutputRecord } from '../types';
import { IntegrityStrip } from '../components/IntegrityStrip';
import { OutputSection } from '../components/OutputSection';

type OutputScreenProps = {
  output: OutputRecord | null;
  integrity: IntegrityResult | null;
  loading: boolean;
  reviewLoading: boolean;
  error: string | null;
  onExecute: () => void;
  onReview: () => void;
};

export function OutputScreen(props: OutputScreenProps) {
  return (
    <div style={{ display: 'grid', gap: 16 }}>
      <div style={{ display: 'flex', gap: 12 }}>
        <button onClick={props.onExecute} disabled={props.loading} style={{ padding: '10px 14px', borderRadius: 12, border: '1px solid #60a5fa', background: '#2563eb', color: '#fff', fontWeight: 700 }}>
          {props.loading ? 'Ausführung läuft...' : 'Ausführen'}
        </button>
        <button onClick={props.onReview} disabled={!props.output || props.reviewLoading} style={{ padding: '10px 14px', borderRadius: 12, border: '1px solid #334155', background: '#0f172a', color: '#fff', fontWeight: 700 }}>
          {props.reviewLoading ? 'Prüfe...' : 'Integrity Review'}
        </button>
      </div>

      {props.error ? <div style={{ color: '#fca5a5' }}>{props.error}</div> : null}

      {props.output ? (
        <>
          <IntegrityStrip parseStatus={props.output.parse_status} integrity={props.integrity} />
          <OutputSection title="Core Result" content={props.output.output_payload.core_result} />
          <OutputSection title="Facts" content={props.output.output_payload.facts} />
          <OutputSection title="Assumptions / Uncertainties" content={props.output.output_payload.assumptions_uncertainties} />
          <OutputSection title="Limits" content={props.output.output_payload.limits} />
          <OutputSection title="Optional" content={props.output.output_payload.optional} />
        </>
      ) : (
        <div style={{ background: '#111827', border: '1px solid #334155', borderRadius: 16, padding: 20, color: '#94a3b8' }}>
          Noch kein Output vorhanden. Starte die Ausführung.
        </div>
      )}
    </div>
  );
}
