# GOSSEOS WORKBENCH V1 – IMPLEMENTATION PLAN

## Purpose

This document translates the app specification into a concrete implementation plan.

It defines:
- project structure
- frontend component map
- backend service map
- API endpoints
- Claude prompt-composition flow
- build sequence

The goal is to make implementation direct, disciplined, and scope-safe.

---

## 1. Project structure

Recommended repository/app structure:

```text
/workbench
  /frontend
    /src
      /app
      /components
      /screens
      /hooks
      /services
      /types
      /utils
  /backend
    /app
      /api
      /services
      /models
      /schemas
      /routers
      /storage
      /prompts
      /utils
  /shared
    /schemas
    /types
  /docs
    app-flow.md
    api-contract.md
  /registry
    artifacts/
```

### Purpose of each top-level area

#### frontend
User-facing workbench UI.

#### backend
Routing, prompt composition, Claude execution, integrity checks, registry save logic.

#### shared
Shared request/response schemas and types.

#### docs
Implementation and interface documentation.

#### registry
Optional local artifact file storage or exported artifact snapshots.

---

## 2. Frontend component map

## Screen 1 – Input

### Main screen component
- `InputScreen`

### Subcomponents
- `InputTitleField`
- `RawInputTextArea`
- `ContextNotesField`
- `DesiredOutcomeField`
- `AnalyzeInputButton`
- `ClearInputButton`

### State handled
- title
- raw_input
- context_notes
- desired_outcome

---

## Screen 2 – Routing

### Main screen component
- `RoutingScreen`

### Subcomponents
- `ProblemClassSelect`
- `ModeSelect`
- `DepthSelect`
- `ArtifactTypeSelect`
- `GovernanceRelevanceToggle`
- `AcceptRouteButton`
- `AdjustRouteButton`
- `ContinueToExecutionButton`

### State handled
- problem_class
- mode
- depth
- artifact_type
- governance_relevance
- route_source (rule/manual/claude)

---

## Screen 3 – Output

### Main screen component
- `OutputScreen`

### Subcomponents
- `CoreResultPanel`
- `FactsPanel`
- `AssumptionsPanel`
- `LimitsPanel`
- `OptionalPanel`
- `CopyResultButton`
- `RerunButton`
- `IntegrityReviewButton`
- `SaveToRegistryButton`

### State handled
- generated_output
- integrity_note
- parse_status

---

## Screen 4 – Registry Save

### Main screen component
- `RegistrySaveScreen`

### Subcomponents
- `ArtifactMetadataForm`
- `SaveArtifactButton`
- `CancelSaveButton`

### State handled
- artifact metadata fields
- validation status

---

## Screen 5 – Artifact View

### Main screen component
- `ArtifactViewScreen`

### Subcomponents
- `ArtifactHeader`
- `ArtifactMetadataPanel`
- `ArtifactContentPanel`
- `DuplicateArtifactButton`
- `MarkReviewedButton`
- `ArchiveArtifactButton`

---

## 3. Backend service map

### 1. Input Parser Service
Purpose:
Normalize incoming raw input and assemble the initial case record.

### 2. Routing Service
Purpose:
Determine or suggest:
- problem_class
- mode
- depth
- artifact_type

Logic:
- deterministic rules first
- Claude fallback if ambiguity is high
- user override always wins

### 3. Prompt Composer Service
Purpose:
Compose the Claude request from GosseOS markdown modules plus task context.

### 4. Claude Execution Service
Purpose:
Call Claude with the composed prompt and return structured output.

### 5. Output Parser Service
Purpose:
Validate JSON output contract.
Fallback to controlled raw text if parsing fails.

### 6. Integrity Review Service
Purpose:
Run lightweight checks for:
- drift risk
- unsupported claims
- artifact mismatch
- malformed structure

### 7. Registry Service
Purpose:
Persist approved outputs as reusable artifacts.

---

## 4. Minimal API plan

## Cases

### POST `/api/cases`
Create a case record.

Input:
- title
- raw_input
- context_notes
- desired_outcome

Output:
- case_id
- stored case record

---

### POST `/api/cases/{case_id}/route`
Route the case.

Input:
- optional manual preferences

Output:
- problem_class
- mode
- depth
- artifact_type
- governance_relevance
- route_source
- confidence_note

---

## Execution

### POST `/api/cases/{case_id}/execute`
Run Claude generation for the routed case.

Input:
- confirmed routing payload

Output:
- output_id
- structured output JSON
- parse_status
- integrity_note (optional basic)

---

### POST `/api/outputs/{output_id}/integrity-review`
Run lightweight integrity checks.

Input:
- output_id

Output:
- integrity_status
- integrity_findings

---

## Registry

### POST `/api/outputs/{output_id}/save-artifact`
Save output into artifact registry.

Input:
- artifact metadata form

Output:
- artifact_id
- artifact record

---

### GET `/api/artifacts/{artifact_id}`
Fetch a saved artifact.

Output:
- artifact metadata
- linked output
- content

---

### GET `/api/artifacts`
List artifacts.

Optional filters:
- status
- domain
- mode
- artifact_type

---

## 5. Claude prompt-composition flow

The backend should compose prompts in this order:

1. `GOSSEOS_CORE.md`
2. `INTEGRITY_KERNEL.md`
3. selected mode excerpt from `MODE_SPECIFICATIONS.md`
4. task block from case + routing
5. requested artifact format
6. optional governance add-on when relevance is medium/high

### Output contract
Claude should be instructed to return JSON with these keys:
- `core_result`
- `facts`
- `assumptions_uncertainties`
- `limits`
- `optional`

### Rule
Do not load all possible documents into every request.
Use only the minimum required stack for the active route.

---

## 6. Minimal data relationships

### CaseRecord
1 case -> 1 routing record
1 case -> many output records possible over time

### OutputRecord
1 output -> may become 1 artifact
1 case -> many reruns -> many outputs

### ArtifactRecord
1 artifact -> tied to one output snapshot
artifacts are versionable and reviewable

---

## 7. Build sequence

## Phase 1 – foundation
- backend app bootstrap
- frontend app bootstrap
- case creation
- routing endpoint
- input screen
- routing screen

## Phase 2 – execution
- prompt composer
- Claude execution endpoint
- output parser
- output screen

## Phase 3 – persistence
- artifact registry model
- save artifact endpoint
- registry save screen
- artifact view screen

## Phase 4 – integrity
- lightweight integrity review endpoint
- integrity review button/action
- structured findings display

---

## 8. V1 scope guardrails

Do not add in v1:
- agent swarm logic
- multi-user roles
- workflow automation marketplace
- broad dashboard layer
- dynamic module service
- autonomous execution loops
- uncontrolled chat history branching

V1 must remain:
- single-user
- structured
- route-first
- artifact-focused
- registry-capable

---

## 9. Build-ready formula

**Frontend captures and renders.**
**Backend routes, composes, and validates.**
**Claude generates.**
**Registry preserves.**

That is enough for GosseOS Workbench v1.
