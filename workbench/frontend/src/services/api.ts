import type {
  CaseCreate,
  CaseRecord,
  IntegrityResult,
  OutputRecord,
  RoutingOverride,
  RoutingRecord,
} from '../types';

const API_BASE = (import.meta.env.VITE_API_BASE_URL as string | undefined) ?? 'http://127.0.0.1:8000';

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: { 'Content-Type': 'application/json', ...(init?.headers ?? {}) },
    ...init,
  });

  const contentType = response.headers.get('content-type') ?? '';
  const body = contentType.includes('application/json') ? await response.json() : await response.text();

  if (!response.ok) {
    const detail = typeof body === 'string' ? body : JSON.stringify(body.detail ?? body);
    throw new Error(detail || `HTTP ${response.status}`);
  }

  return body as T;
}

export function createCase(payload: CaseCreate): Promise<CaseRecord> {
  return request<CaseRecord>('/api/cases', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}

export function routeCase(caseId: string, override?: RoutingOverride): Promise<RoutingRecord> {
  return request<RoutingRecord>(`/api/cases/${caseId}/route`, {
    method: 'POST',
    body: override ? JSON.stringify(override) : undefined,
  });
}

export function executeCase(caseId: string): Promise<OutputRecord> {
  return request<OutputRecord>(`/api/cases/${caseId}/execute`, {
    method: 'POST',
  });
}

export function reviewIntegrity(outputId: string): Promise<IntegrityResult> {
  return request<IntegrityResult>(`/api/outputs/${outputId}/integrity-review`, {
    method: 'POST',
  });
}
