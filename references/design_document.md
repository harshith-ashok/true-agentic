# True Agentic

_A long-term cognitive assistant architecture_

---

## 0. Core Vision

> **Project Intelligence is a persistent cognitive system that observes work, builds evolving internal representations of ideas, and intervenes only when its confidence is high that doing so helps the user’s long-term goals.**

This is **not a chatbot**.  
This is **not a task manager**.  
This is **a thinking substrate around an LLM**.

---

## 1. Non-Negotiable Principles

1. No flat memory
    
2. No passive recall
    
3. No constant interruption
    
4. No hallucinated certainty
    
5. Everything must be explainable internally
    

If any design violates these → it is wrong.

---

## 2. Core Entity: Project

A **Project** is not a folder or chat.

> **A Project is a bounded evolving intention space.**

Each project contains:

- Purpose (explicit or inferred)
    
- Lifespan
    
- Internal tensions
    
- Evolving ideas
    

---

## 3. Goal Vector (Why the project exists)

Goals are **optimization directions**, not tasks.

Example axes:

- clarity ↑
    
- novelty ↑
    
- feasibility ↑
    
- time_to_execution ↓
    
- confidence ↑
    

Goal weights shift over time:

- Early → exploration, novelty
    
- Late → coherence, execution
    

---

## 4. Idea Graph (Heart of Intelligence)

### Nodes = Ideas

Not messages. Not files.

Each idea has:

- Canonical sentence
    
- Embedding
    
- Confidence
    
- Timestamp
    
- Origin event
    

### Edges = Relationships

- refines
    
- extends
    
- contradicts
    

Edges have:

- Direction
    
- Strength
    

This enables:

- Tracking evolution
    
- Detecting drift
    
- Surfacing forgotten ideas
    
- Preventing contradictions
    

---

## 5. Memory Streams

### Episodic Memory

What happened, when, context

### Semantic Memory

Generalized ideas

### Intent Memory

What the user meant, not said

### Emotional Signal (non-human)

Importance, friction, momentum

Emotion here is **signal weighting**, not feeling.

---

## 6. Project State Vector

A numerical snapshot of project dynamics.

MVP axes:

- exploration
    
- clarity
    
- momentum
    
- uncertainty
    

Used to:

- Bias retrieval
    
- Gate proactivity
    
- Adjust tone & depth
    

---

## 7. Insight Engine (Proactivity without annoyance)

> **Never surface insights just because you can.**

An insight is allowed only when:

1. A pattern exists in the idea graph
    
2. The state vector indicates receptivity
    
3. Confidence exceeds a threshold
    

### Insight types

- Convergence
    
- Drift
    
- Neglected idea
    
- Premature fixation
    

Insights are **observations**, not commands.

---

## 8. Role of the LLM

The LLM is **not the brain**.

It:

- Extracts ideas
    
- Proposes relations
    
- Synthesizes summaries
    

It does **not**:

- Own memory
    
- Decide importance
    
- Control state
    
- Track evolution
    

---

## 9. “Custom LLM” Without Training One

Personalization comes from:

- Context selection
    
- Memory shaping
    
- Graph evolution
    

Same model + different internal state = emergent intelligence.

---

## 10. MVP Philosophy

> The MVP’s goal is **long-term coherence**, not magic.

Success = leaving for days and resuming meaningfully.

---

## 11. Tech Stack (Settled)

### Backend

- Python 3.12
    
- FastAPI
    
- Pydantic v2
    

### Storage

- PostgreSQL (canonical memory)
    
- Vector DB (FAISS or pgvector)
    

### LLM Interface

- JSON-only inputs/outputs
    
- Strict schema validation
    
- Low temperature
    

### No Redis (yet)

Redis is **ephemeral coordination**, not memory.  
If losing Redis breaks intelligence → it’s wrong.

---

## 12. Internal Data Flow

```
User Input
  ↓
Raw Event (stored)
  ↓
LLM → JSON extraction
  ↓
Schema validation
  ↓
Idea Graph update
  ↓
State Vector update
  ↓
Optional Insight Gate
```

---

## 13. Database Schema

### projects

```
id (uuid)
title
description
status (exploring | shaping | executing)
created_at
last_active_at
```

### events (raw, immutable)

```
id
project_id
timestamp
source (chat | note | calendar | todo | system)
content
metadata (jsonb)
```

### ideas

```
id
project_id
source_event_id
content
confidence
idea_type (principle | decision | question | constraint | observation)
created_at
```

### idea_edges

```
id
project_id
from_idea_id
to_idea_id
relation_type (refines | extends | contradicts)
strength
created_at
```

### episodes

```
id
project_id
start_time
end_time
summary
dominant_idea_ids[]
unresolved_tensions
```

### project_state_snapshots

```
id
project_id
timestamp
exploration
clarity
momentum
uncertainty
```

### insights

```
id
project_id
insight_type (convergence | drift | neglected | blockage)
content
evidence_idea_ids[]
confidence
created_at
acknowledged
```

---

## 14. Why This Avoids Clippy / Cortana Failure

- No surface-level triggers
    
- No blind interruptions
    
- No certainty without evidence
    
- Proactivity is gated by confidence
    

This feels like **a tool that knows when to stay silent**.

---
