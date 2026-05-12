export type ProblemClass =
  | "analysis"
  | "planning"
  | "decision_support"
  | "documentation"
  | "communication"
  | "governance_risk"
  | "creative_development";

export type Mode =
  | "Architect"
  | "Build"
  | "Audit"
  | "Red Team"
  | "Briefing";

export type Depth =
  | "Direct"
  | "Compact"
  | "Standard"
  | "Endboss";

export type ArtifactType =
  | "one-pager"
  | "dossier"
  | "SOP"
  | "report"
  | "post"
  | "framework"
  | "prompt"
  | "briefing_note"
  | "registry_entry";

export type ArtifactStatus =
  | "draft"
  | "working"
  | "validated"
  | "canonical"
  | "archived";

export type ParseStatus = "ok" | "repaired" | "failed";

export type RouteSource = "rule" | "claude" | "manual";

export interface CaseCreate {
  title?: string;
  raw_input: string;
  context_notes?: string;
  desired_outcome?: string;
}

export interface CaseRecord {
  case_id: string;
  title: string | null;
  raw_input: string;
  context_notes: string | null;
  desired_outcome: string | null;
  created_at: string;
}

export interface RoutingOverride {
  problem_class: ProblemClass;
  mode: Mode;
  depth: Depth;
  artifact_type: ArtifactType;
  governance_relevance: boolean;
}

export interface RoutingRecord {
  routing_id: string;
  case_id: string;
  problem_class: ProblemClass;
  mode: Mode;
  depth: Depth;
  artifact_type: ArtifactType;
  governance_relevance: boolean;
  route_source: RouteSource;
  confidence_score: number | null;
}

export interface OutputPayload {
  core_result: string;
  facts: string;
  assumptions_uncertainties: string;
  limits: string;
  optional?: string | null;
}

export interface OutputRecord {
  output_id: string;
  case_id: string;
  output_payload: OutputPayload;
  integrity_note: string | null;
  parse_status: ParseStatus;
  created_at: string;
}

export interface IntegrityResult {
  output_id: string;
  drift: boolean;
  hallucination_risk: boolean;
  artifact_mismatch: boolean;
  unsupported_claims: boolean;
  note: string | null;
}

export interface ArtifactCreate {
  case_id: string;
  output_id: string;
  title: string;
  status: ArtifactStatus;
  domain: string;
  problem_class: ProblemClass;
  mode: Mode;
  depth: Depth;
  artifact_type: ArtifactType;
  purpose: string;
  assumption_level: string;
  integrity_status: string;
  governance_relevance: boolean;
  version: string;
  reuse_notes?: string | null;
}

export interface ArtifactRecord extends ArtifactCreate {
  artifact_id: string;
  created_at: string;
  last_reviewed: string | null;
}

export interface ArtifactUpdate {
  status?: ArtifactStatus;
  reuse_notes?: string | null;
  version?: string;
  last_reviewed?: string | null;
}
