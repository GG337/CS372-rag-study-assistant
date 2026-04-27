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

- Demo: https://github.com/user-attachments/assets/cafc3472-9ea1-415f-9812-11c2ae420e89
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
  "Facilitated diffusion does"

- With RAG:  
  "Guided diffusion is a technique used to condition and guide a generative diffusion model given a text input. It involves using cross-attention to condition the model on the text input and guide it toward generating images that align with the input description.”


### Prompt Engineering Comparison

We evaluated three prompt designs to observe how prompt structure affects answer quality.

| Prompt Style | Description | Example Output |
|-------------|------------|----------------|
| Style 1 | Basic instruction | Guided diffusion is a technique used to condition and guide a generative diffusion model given a text input. It involves using cross-attention to condition the model on the text input and guide it towards generating images that are similar to the input text. |
| Style 2 | Concise tutor-style prompt | Guided diffusion is a technique used to condition and guide a generative diffusion model given a text input. It uses text conditioning to steer the model toward generating images that align with the input description. |
| Style 3 | Step-by-step reasoning prompt | 1. Guided diffusion is a technique used in machine learning to condition and guide a generative diffusion model given a text input. 2. It uses attention mechanisms to focus on relevant parts of the input text. 3. This allows the model to generate images that align with the given description. |

### Observations

- **Style 1:** Correct but includes extra irrelevant text (e.g., “Exercise”)  
- **Style 2:** Most clear and concise answer (best overall)  
- **Style 3:** More structured but often verbose and includes unnecessary context  

### Conclusion

Prompt design significantly affects answer quality. Concise prompts produce clearer answers, while step-by-step prompts increase structure but may introduce verbosity.

---

## Key Findings

- RAG significantly improves answer relevance and grounding  
- Model performance depends heavily on the quality of the language model  
- Retrieval quality improves when chunk size and context are tuned  
- PDF text extraction introduces noise due to:
  - images and diagrams not being captured  
  - mathematical symbols being partially corrupted  
- The use of FAISS instead of manually computing cosine similarity improves retrieval efficiency and scalability, especially as the number of document chunks increases.

---

## Method Overview

Pipeline:

PDF → Text Extraction → Chunking → Embeddings → FAISS → Retrieval → Language Model → Answer

### Components

- Embeddings: Sentence Transformers  
- Vector Search: FAISS (Like cosine similarity)
- Language Model: Phi-2
- Framework: Python + HuggingFace Transformers  

### Retrieval Method

This project uses FAISS (Facebook AI Similarity Search) for efficient similarity search over embeddings. FAISS performs nearest-neighbor search using L2 distance, which serves a similar role to cosine similarity but is optimized for speed and scalability.

This design choice allows the system to efficiently retrieve the most relevant text chunks compared to manually computing cosine similarity over all embeddings.

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
- Improve PDF parsing (multimodal models)  
- Add quantitative evaluation metrics  
- Support multiple documents for broader retrieval  

---

## Individual Contributions

This project was completed individually.
