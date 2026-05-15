import type { ArtifactCreate, ArtifactRecord, ArtifactUpdate } from '../types';

const API_BASE = (import.meta.env.VITE_API_BASE_URL as string | undefined) ?? 'http://127.0.0.1:8000';

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: { 'Content-Type': 'application/json', ...(init?.headers ?? {}) },
    ...init,
  });

  const contentType = response.headers.get('content-type') ?? '';
  const body = contentType.includes('application/json') ? await response.json() : await response.text();

  if (!response.ok) {
    const detail = typeof body === 'string' ? body : JSON.stringify(body);
    throw new Error(detail || `HTTP ${response.status}`);
  }

  return body as T;
}

export function saveArtifact(payload: ArtifactCreate): Promise<ArtifactRecord> {
  return request<ArtifactRecord>('/api/artifacts', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}

export function getArtifact(artifactId: string): Promise<{ artifact: ArtifactRecord; content: unknown }> {
  return request<{ artifact: ArtifactRecord; content: unknown }>(`/api/artifacts/${artifactId}`);
}

export function listArtifacts(filters?: { status?: string; domain?: string; mode?: string; artifact_type?: string }): Promise<ArtifactRecord[]> {
  const params = new URLSearchParams();
  if (filters?.status) params.set('status', filters.status);
  if (filters?.domain) params.set('domain', filters.domain);
  if (filters?.mode) params.set('mode', filters.mode);
  if (filters?.artifact_type) params.set('artifact_type', filters.artifact_type);
  const query = params.toString();
  return request<ArtifactRecord[]>(`/api/artifacts${query ? `?${query}` : ''}`);
}

export function updateArtifact(artifactId: string, payload: ArtifactUpdate, markReviewed = false): Promise<ArtifactRecord> {
  return request<ArtifactRecord>(`/api/artifacts/${artifactId}${markReviewed ? '?mark_reviewed=true' : ''}`, {
    method: 'PATCH',
    body: JSON.stringify(payload),
  });
}
