# AI Study Assistant with RAG

## What it Does
This project implements a retrieval-augmented generation (RAG) system that answers questions based on course lecture slides. The system processes PDF documents, retrieves relevant text using embeddings and vector search, and generates answers using a pretrained language model. 

---

## Quick Start

Install dependencies:
```bash
python -m pip install -r requirements.txt
```

---

## Video Links

- Demo: [PASTE DEMO VIDEO LINK HERE]
- Technical Walkthrough: [PASTE TECHNICAL VIDEO LINK HERE]

---

## Evaluation

We compare system performance with and without retrieval (RAG).
This aligns with known RAG behavior, where access to relevant document context significantly improves LLM accuracy.

### Without RAG

- Model produces generic or incorrect answers  
- Often hallucinates information not related to the slides  

### With RAG

- Model retrieves relevant context from lecture slides  
- Answers are more accurate and grounded in the provided material  

### Example

Question: What is guided diffusion?

- Without RAG:  
  Produces vague or incorrect definitions  

- With RAG:  
  Correctly explains guided diffusion as conditioning a generative diffusion model on text input and using guidance mechanisms  

---

## Key Findings

- RAG significantly improves answer relevance and grounding  
- Model performance depends heavily on the quality of the language model  
- Retrieval quality improves when chunk size and context are tuned  
- PDF text extraction introduces noise due to:
  - images and diagrams not being captured  
  - mathematical symbols being partially corrupted  

---

## Method Overview

Pipeline:

PDF → Text Extraction → Chunking → Embeddings → FAISS → Retrieval → Language Model → Answer

### Components

- Embeddings: Sentence Transformers  
- Vector Search: FAISS (Like cosine similarity)
- Language Model: Phi-2
- Framework: Python + HuggingFace Transformers  

---

## Limitations

- Lecture slides contain diagrams and images that are not captured by text extraction  
- Mathematical notation is partially corrupted when parsed from PDF  
- Smaller local models may not fully utilize retrieved context  
- Some answers may still be incomplete or slightly inaccurate  
- The system currently processes one document at a time but could be extended to multiple documents.

---

## Future Improvements

- Use stronger instruction-tuned models  
- Improve PDF parsing (OCR or multimodal models)  
- Add quantitative evaluation metrics  
- Support multiple documents for broader retrieval  

---

## Individual Contributions

This project was completed individually.