# System Architecture — Reliable Multimodal Math Mentor

This document describes the architecture of the **Multimodal Math Mentor AI system**.  
The system is designed using a **multi-agent pipeline**, **RAG retrieval**, **multimodal inputs**, **HITL validation**, and a **memory layer** for learning from feedback.

---

# High-Level Architecture

```mermaid
flowchart TD

A[User Input] --> B{Input Type}

B -->|Text| C[Text Processor]
B -->|Image| D[OCR Engine]
B -->|Audio| E[Speech To Text]

C --> F[Parser Agent]
D --> F
E --> F

F --> G[Intent Router Agent]

G --> H[Memory Similarity Retrieval]

H --> I[RAG Retriever]

I --> J[Solver Agent]

J --> K[Verifier Agent]

K -->|Valid| L[Explainer Agent]
K -->|Uncertain| M[Human In The Loop]

M --> J

L --> N[Streamlit UI Output]

N --> O[User Feedback]

O --> P[Memory Store]

Agent Architecture

The system contains five core agents.

Parser Agent

Responsibilities:

Clean OCR / ASR output

Extract structured problem representation

Detect missing information

Output format:
{
  "problem_text": "...",
  "topic": "algebra",
  "variables": ["x"],
  "constraints": [],
  "needs_clarification": false
}

Intent Router Agent

Classifies the problem domain.

Supported domains:

Algebra

Probability

Calculus

Linear Algebra

This determines the solving strategy.

Solver Agent

Responsible for generating the mathematical solution.

Uses:

RAG retrieved knowledge

symbolic math tools

Grok reasoning model

Inputs:

structured problem

retrieved knowledge context

Outputs:
solution
intermediate reasoning
final answer

Verifier Agent

Ensures solution reliability.

Checks:

correctness

domain constraints

logical consistency

edge cases

If confidence is low:

trigger HITL
Explainer Agent

Transforms the verified solution into a student-friendly explanation.

Output style:

Step 1: Identify formula
Step 2: Substitute values
Step 3: Simplify expression
Step 4: Final result
RAG Pipeline

Knowledge base consists of curated documents:

data/
 algebra/
 calculus/
 probability/
 linear_algebra/

Pipeline:

Documents → Chunking → Embedding → FAISS Vector Store → Top-K Retrieval

Embedding model:

sentence-transformers/all-MiniLM-L6-v2
Multimodal Processing

Supported input types:

Text Input

Direct parsing.

Image Input

Pipeline:

Image → EasyOCR → Extracted Text → Parser Agent
Audio Input

Pipeline:

Audio → Whisper → Transcript → Parser Agent
Human-in-the-Loop (HITL)

HITL is triggered when:

OCR confidence is low

audio transcription unclear

parser ambiguity detected

verifier confidence below threshold

user requests re-check

Actions available:

approve

edit

reject

Corrections are stored in memory.

Memory System

The memory layer stores previous interactions.

Stored data:

original_input
parsed_problem
retrieved_context
solution
verification_result
user_feedback
timestamp

Purpose:

retrieve similar solved problems

reuse solution patterns

improve OCR corrections

Database:

SQLite
Application Layer

User interface built with:

Streamlit

UI capabilities:

input mode selector

OCR transcript preview

agent execution trace

retrieved knowledge display

final answer + explanation

feedback buttons

Deployment

Application can be deployed using:

Streamlit Cloud

HuggingFace Spaces

Render

Railway

Reviewer workflow:

Open link → Upload problem → View solution
End-to-End Pipeline
User Input
   ↓
Multimodal Processing
   ↓
Parser Agent
   ↓
Intent Router Agent
   ↓
Memory Retrieval
   ↓
RAG Retrieval
   ↓
Solver Agent
   ↓
Verifier Agent
   ↓
Explainer Agent
   ↓
Streamlit Output
   ↓
User Feedback
   ↓
Memory Update