# DocDoc: Multi-Agent Self-Correcting Documentation Assistant

An RAG system designed to transform how developers interact with complex software and technical documentation. By leveraging a multi-agent framework orchestrated through state machines, Agent recursively processes technical text, isolates and validates code execution syntax, and cross-references an active memory layer before delivering precise answers.

---

## 🎯 Project Roadmap & Core Novelty Checklist

This checklist defines the technical milestones and unique engineering features that set this project apart from basic, linear RAG pipelines.

- [ ] **Hierarchical Multi-Agent Crew :** Deploy distinct, specialized AI agents (e.g., *Documentation Scraper Agent*, *Code Validation Agent*, and *Technical Writer Agent*) working in tandem rather than relying on a single monolithic LLM prompt.
- [ ] **Cyclic State Control (LangGraph):** Implement fallback loops where agents can dynamically reject poor search queries, rewrite search terms, or re-route queries based on structural feedback.
- [ ] **Hybrid Dense & Sparse Retrieval in ChromaDB:** Combine standard semantic embeddings with keyword-matching capabilities inside ChromaDB to ensure exact terminal flags (e.g., `-laX`) are perfectly matched.
- [ ] **Contextual Chunk Enrichment:** Automatically prepend a high-level page summary to every tiny code or text chunk during ingestion so structural context is never lost.
- [ ] **Real-Time Agent Thought Stream (UI):** Build a diagnostic step-by-step UI visibility console so users can actively see *which* agent is processing data and *what* database chunks were pulled.
- [ ] **Automated Evaluation Loop:** Integrate test metrics tracking to mathematically grade the system's *Faithfulness* and *Context Precision* to eliminate hallucinations entirely.

---

## 🛠️ Technology Stack & Architecture Justification

The core architecture uses a modular approach, leveraging specialized open-source frameworks to handle the complex, non-linear nature of software documentation.

| Pipeline Component | Technology Chosen | Why This Specific Technology? |
| :--- | :--- | :--- |
| **Multi-Agent Logic** | `*Unknown` | 
| **State Orchestration**| `LangGraph` |
| **Vector Storage** | `ChromaDB` | 
| **Ingestion Engine** | `Crawl4AI` + `Playwright` | 
| **User Interface** | `*Unknown` | 
