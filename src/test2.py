from load_data import load_pdf
from chunk import chunk_text
from embed import embed_chunks, model
from retrieve import Retriever
from generate import generate_answer


# Load ONE document
text = load_pdf("data/14-GuidedDiffusion.pdf")

# Build pipeline
chunks = chunk_text(text)
embeddings = embed_chunks(chunks)
retriever = Retriever(embeddings, chunks)

# ONE test question
question = "What is guided diffusion?"

print("\nQuestion:", question)

# RAG only (no baseline for now)
q_embed = model.encode([question])[0]
retrieved = retriever.query(q_embed, k=1)
context = " ".join(retrieved)

print("\nContext:")
print(context[:300], "...")

print("\nAnswer:")
print(generate_answer(context, question))