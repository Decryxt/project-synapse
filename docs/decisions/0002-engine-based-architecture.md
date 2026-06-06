# ADR 0002: Engine-Based Architecture

## Status
Accepted

## Context
Project Synapse must remain modular, scalable, and understandable as it grows. Organizing only by technical type such as models, services, and utilities can create large disconnected folders over time.

## Decision
Project Synapse will organize core capabilities into engines.

Initial engines:
- Observation
- Evidence
- Knowledge
- Reasoning
- Hypothesis
- Prediction
- Evaluation
- Learning
- Opportunity

## Consequences
- Each engine has a clear responsibility
- Future engineers can understand system boundaries
- Engines can be tested and replaced independently
- Architecture aligns with the observe → reason → predict → learn loop