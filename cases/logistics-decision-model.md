# Case: Logistics Decision Model

## Purpose

This case shows how an operational logistics problem can become a structured decision model.

The goal is to move from subjective pressure to reviewable decision logic.

---

## 1. Raw Input Type

Typical input:

```text
Our warehouse process is unstable. Picking, replenishment, staffing, and cold chain risk are affecting performance.
```

---

## 2. Problem Class

This is an operational process and decision-support problem.

It combines:

- warehouse process analysis
- risk prioritization
- KPI logic
- staffing constraints
- cold chain or quality control
- management communication

---

## 3. Mode Routing

| Layer | Selection |
|---|---|
| Primary Mode | AUDIT |
| Secondary Mode | BUILD |
| Verification Mode | RED TEAM |
| Artifact Type | decision matrix + control checklist |
| Governance Signal | APPROVED WITH WARNING |

Reason:

Operational logistics decisions affect real people, goods, time, service level, and sometimes compliance.
Assumptions must be visible.

---

## 4. Decision Inputs

A useful logistics decision model should capture:

| Input | Meaning |
|---|---|
| demand pressure | how urgent the workload is |
| stockout risk | risk of empty pick slots or missing goods |
| cold chain risk | temperature or quality sensitivity |
| travel effort | time, distance, or route complexity |
| staffing load | available people and skill coverage |
| error probability | likelihood of wrong article, quantity, or zone |
| business impact | customer, service, cost, or compliance effect |

---

## 5. Example Scoring Model

Score each factor from 1 to 5.

| Factor | Score 1 | Score 5 |
|---|---|---|
| urgency | low pressure | critical time pressure |
| risk | minor operational issue | severe quality/service impact |
| detectability | easy to detect early | detected late or at customer |
| effort | low effort | high travel/time/coordination effort |
| staffing sensitivity | any trained worker can do it | only few people can handle it |

Priority can be estimated with:

```text
Priority = Urgency + Risk + Detectability + Effort + Staffing Sensitivity
```

Interpretation:

| Score | Priority |
|---:|---|
| 5-10 | Low |
| 11-17 | Medium |
| 18-25 | High |

---

## 6. Decision Matrix Template

| Issue | Urgency | Risk | Detectability | Effort | Staffing Sensitivity | Total | Priority | Action |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Pick slot unstable | 4 | 4 | 3 | 3 | 3 | 17 | Medium | monitor + replenish earlier |
| Temperature deviation | 5 | 5 | 4 | 2 | 4 | 20 | High | escalate + document |
| Staffing gap | 4 | 4 | 2 | 3 | 5 | 18 | High | reassign trained operator |

---

## 7. Control Checklist

Before acting, check:

- Is the problem recurring or one-time?
- Is customer impact possible?
- Is quality or cold chain affected?
- Is data available or only verbal pressure?
- Is the root cause process design or execution behavior?
- Who owns the decision?
- What must be documented?
- What should be escalated?

---

## 8. Red-Team Review

A weak model fails when it:

- treats every issue as equal
- ignores staffing reality
- ignores quality or cold chain risk
- uses KPI numbers without context
- hides assumptions
- creates a false sense of precision

A strong model:

- shows assumptions
- separates risk from effort
- links decisions to operational control
- defines escalation triggers
- can be reused with real site data

---

## 9. Governance Classification

```text
APPROVED WITH WARNING
```

Reason:

The model is useful for structuring decisions, but real operational data, site layout, system records, and management rules must validate the scoring.

---

## 10. Reuse Note

This case can be adapted for:

- replenishment prioritization
- cold chain deviation handling
- shift handover decisions
- warehouse bottleneck analysis
- staffing escalation
- transport loading priority
- service-level risk review

---

## Core Principle

Operational pressure must be translated into decision logic before it becomes action.
