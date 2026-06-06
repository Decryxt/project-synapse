# ADR 0001: CLI-First Interface

## Status
Accepted

## Context
Project Synapse is an Economic Intelligence Engine, not a consumer dashboard. The system should feel like an intelligence terminal and prioritize the core reasoning, prediction, scoring, and learning systems before visual interfaces.

## Decision
Project Synapse will use a CLI-first interface as the primary control surface.

The CLI is not the brain. It is only the operator interface.

## Consequences
- Faster experimentation
- Less frontend complexity
- Better alignment with intelligence workflows
- Easier automation
- React/FastAPI can be added later without replacing the core