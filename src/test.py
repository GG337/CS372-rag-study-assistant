from load_data import load_pdf
from chunk import chunk_text
from embed import embed_chunks, model
from retrieve import Retriever
from generate import generate_answer


# =========================
# SETUP PIPELINE
# =========================

# Load PDF (change filename if needed)
files = [
    "data/13-Diffusion.pdf",
    "data/14-GuidedDiffusion.pdf"
]

text = ""
for f in files:
    text += load_pdf(f) + "\n"

# Chunk text
chunks = chunk_text(text)

# Create embeddings
embeddings = embed_chunks(chunks)

# Build retriever
retriever = Retriever(embeddings, chunks)


# =========================
# TEST QUESTIONS
# =========================

questions = [
    "What is guided diffusion?",
    "What is conditioning in diffusion models?",
    "What is cross-attention?",
    "What is the role of text in image generation?"
]


# =========================
# RUN EVALUATION
# =========================

for q in questions:
    print("\n" + "=" * 50)
    print("Question:", q)

    # ---- NO RAG (baseline) ----
    print("\n--- Without RAG ---")
    no_rag_answer = generate_answer("", q)
    print(no_rag_answer)

    # ---- WITH RAG ----
    q_embed = model.encode([q])[0]
    retrieved_chunks = retriever.query(q_embed, k=2)

    context = " ".join(retrieved_chunks)

    print("\n--- Retrieved Context ---")
    for i, chunk in enumerate(retrieved_chunks):
        print(f"\nChunk {i+1}:\n{chunk[:200]}...")

    print("\n--- With RAG ---")
    rag_answer = generate_answer(context, q)
    print(rag_answer)


print("\nDone.")