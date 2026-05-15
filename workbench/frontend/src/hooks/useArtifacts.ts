import { useState } from 'react';

import { getArtifact, listArtifacts, saveArtifact, updateArtifact } from '../services/api';
import type { ArtifactCreate, ArtifactRecord, ArtifactUpdate } from '../types';

export function useArtifacts() {
  const [artifact, setArtifact] = useState<ArtifactRecord | null>(null);
  const [artifacts, setArtifacts] = useState<ArtifactRecord[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function createArtifact(payload: ArtifactCreate) {
    setLoading(true);
    setError(null);
    try {
      const created = await saveArtifact(payload);
      setArtifact(created);
      return created;
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Unknown artifact error';
      setError(message);
      throw err;
    } finally {
      setLoading(false);
    }
  }

  async function fetchArtifact(artifactId: string) {
    setLoading(true);
    setError(null);
    try {
      const data = await getArtifact(artifactId);
      setArtifact(data.artifact);
      return data;
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Unknown artifact error';
      setError(message);
      throw err;
    } finally {
      setLoading(false);
    }
  }

  async function fetchArtifacts(filters?: {
    status?: string;
    domain?: string;
    mode?: string;
    artifact_type?: string;
  }) {
    setLoading(true);
    setError(null);
    try {
      const items = await listArtifacts(filters);
      setArtifacts(items);
      return items;
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Unknown artifact error';
      setError(message);
      throw err;
    } finally {
      setLoading(false);
    }
  }

  async function patchArtifact(artifactId: string, payload: ArtifactUpdate, markReviewed = false) {
    setLoading(true);
    setError(null);
    try {
      const updated = await updateArtifact(artifactId, payload, markReviewed);
      setArtifact(updated);
      return updated;
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Unknown artifact error';
      setError(message);
      throw err;
    } finally {
      setLoading(false);
    }
  }

  return {
    artifact,
    artifacts,
    loading,
    error,
    createArtifact,
    fetchArtifact,
    fetchArtifacts,
    patchArtifact,
  };
}
