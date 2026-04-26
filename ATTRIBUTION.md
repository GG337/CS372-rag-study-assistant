# Attribution

## AI Tools Used

ChatGPT was used to assist with:
- debugging Python code (e.g., fixing errors in FAISS retrieval and model setup)
- generating initial boilerplate code for the RAG pipeline
- suggesting improvements for prompt design and evaluation structure

The generated code was not used directly without review. All outputs were:
- tested and modified to work with the project pipeline
- adjusted for compatibility with the chosen models (e.g., Phi-2)
- refined to improve output quality and clarity

Significant manual work was required to:
- debug integration between components (PDF loading, embeddings, retrieval, generation)
- design evaluation experiments (RAG vs no-RAG and prompt comparison)

## Libraries Used

- HuggingFace Transformers
- Sentence Transformers
- FAISS
- PyPDF

## Models Used

- microsoft/phi-2 (language model)
- sentence-transformers/all-MiniLM-L6-v2 (embeddings)

## Data Sources

- Course lecture slides provided in CS372
