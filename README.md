# Reliable Multimodal Math Mentor

An AI-powered system that solves JEE-style mathematics problems using a **multi-agent architecture**, **Retrieval-Augmented Generation (RAG)**, **multimodal input processing**, **Human-in-the-Loop (HITL)** validation, and **memory-based learning**.

The system can accept math problems via **text, image, or audio**, solve them step-by-step, verify correctness, explain the reasoning clearly, and learn from feedback over time.

---

# Project Overview

This project implements a reliable AI tutoring system designed for solving mathematics problems typically seen in **JEE-level exams**.

Key goals of the system:

- Reliable reasoning using **multi-agent architecture**
- Reduce hallucinations using **RAG-based retrieval**
- Support **multimodal input**
- Enable **human correction when needed**
- Improve performance using **memory-based learning**

---

# Core Capabilities

### Multimodal Input
Users can submit problems through:

- Typed text
- Uploaded image (OCR extraction)
- Recorded or uploaded audio (speech-to-text)

### Multi-Agent System

The system uses specialized agents for different reasoning tasks.

| Agent | Responsibility |
|------|---------------|
Parser Agent | Convert raw input into structured math problem |
Intent Router | Identify the mathematical topic |
Solver Agent | Solve the problem using retrieved knowledge |
Verifier Agent | Check correctness and logical consistency |
Explainer Agent | Generate student-friendly explanation |

---

# System Architecture

The system follows a modular pipeline architecture.
User Input
│
▼
Multimodal Processing
(Text / Image / Audio)
│
▼
Parser Agent
│
▼
Intent Router Agent
│
▼
Memory Retrieval
│
▼
RAG Knowledge Retrieval
│
▼
Solver Agent
│
▼
Verifier Agent
│
▼
Explainer Agent
│
▼
UI Output
│
▼
User Feedback
│
▼
Memory Update


---

# RAG Pipeline

The system uses a **Retrieval-Augmented Generation architecture**.

Steps:

1. Load curated math documents
2. Chunk documents
3. Generate embeddings
4. Store embeddings in **FAISS vector database**
5. Retrieve top-k relevant documents
6. Provide retrieved context to the solver agent

Knowledge base includes:

- math formulas
- solution templates
- common mistakes
- domain constraints

---

# Multimodal Processing

### Image Input

Uses **EasyOCR** to extract mathematical text from images.

Workflow:
Image Upload
│
▼
OCR Extraction
│
▼
Preview + User Confirmation


### Audio Input

Uses **Whisper** speech-to-text engine.

Workflow:
Audio Input
│
▼
Speech Recognition
│
▼
Transcript Preview


---

# Human-in-the-Loop (HITL)

Human intervention is triggered when:

- OCR confidence is low
- audio transcription is unclear
- parser detects ambiguity
- verifier confidence is low

Users can:

- edit extracted text
- correct solutions
- provide feedback

These corrections are stored for future learning.

---

# Memory System

The system stores previous interactions in a persistent memory layer.

Stored data includes:

- original input
- parsed problem
- retrieved knowledge
- final solution
- verification result
- user feedback

The memory system enables:

- retrieval of similar problems
- reuse of successful solution patterns
- correction of OCR or transcription errors

---

# Project Structure
math-mentor-ai/
│
├── frontend/
├── agents/
├── rag/
├── multimodal/
├── tools/
├── memory/
├── hitl/
├── utils/
├── configs/
├── data/
├── vector_store/
├── tests/
│
├── app.py
├── requirements.txt
├── README.md
└── architecture.md


---

# Installation

Clone the repository:
git clone <repository-url>
cd math-mentor-ai


Create virtual environment:
python -m venv venv
venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


---

# Environment Configuration

Create `.env` file:
GROK_API_KEY=your_api_key_here


---

# Running the Application
streamlit run app.py


Open in browser:
http://localhost:8501


---

# Running Tests
pytest


---

# Technology Stack

| Component | Technology |
|----------|-----------|
Backend | Python |
UI | Streamlit |
Vector Database | FAISS |
Embeddings | Sentence Transformers |
OCR | EasyOCR |
Speech Recognition | Whisper |
Math Engine | SymPy |
LLM API | Grok |

---

# Deployment Options

The system can be deployed using:

- Streamlit Cloud
- HuggingFace Spaces
- Render
- Railway
- Vercel (backend service)

---

# Future Improvements

Possible extensions:

- symbolic math reasoning engine
- advanced equation parsing
- reinforcement learning from feedback
- larger curated math knowledge base
- adaptive tutoring system

---

# Conclusion

This system demonstrates how reliable AI tutoring systems can be built using:

- modular agent architectures
- retrieval-based grounding
- human oversight
- multimodal interaction

The architecture prioritizes **correctness, explainability, and continuous improvement**.