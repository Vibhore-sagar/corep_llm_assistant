# LLM-Assisted COREP Reporting Assistant

## Overview
This project demonstrates a retrieval-grounded LLM assistant designed to support regulatory reporting workflows for COREP Own Funds (CET1).

The system converts natural-language reporting scenarios into structured COREP-aligned outputs with validation and audit traceability.

## Key Features
- Fully local LLM deployment using Ollama (no external APIs)
- Retrieval-Augmented Generation (RAG)
- Structured JSON outputs
- Validation layer for reporting logic
- Hallucination guardrails
- Audit logging

## Architecture
User → Streamlit → FastAPI → Retriever → Local LLM → Validation → Audit

## Why Local LLM?
This prototype prioritizes data privacy and regulatory safety by avoiding external AI providers.

## Risk Controls
- Retrieval grounding prevents unsupported generation  
- Deterministic temperature  
- Structured schema enforcement  
- Validation rules  
- Guardrails for explanation grounding  
- Audit trail  

## Limitations
This is a prototype and not intended for production regulatory use. Human oversight is required.

## Future Work
- Policy-as-code validation  
- Human-in-the-loop review  
- Regulatory knowledge versioning  
- Model risk governance  
