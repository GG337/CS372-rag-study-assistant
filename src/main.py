from load_data import load_pdf
from chunk import chunk_text
from embed import embed_chunks, model
from retrieve import Retriever
from generate import generate_answer

# Load PDF
text = load_pdf("data/14-GuidedDiffusion.pdf")

# Chunk
chunks = chunk_text(text)

# Embed
embeddings = embed_chunks(chunks)

# Build retriever
retriever = Retriever(embeddings, chunks)

# Ask question
question = input("Ask a question: ")

# Embed question
question_embedding = model.encode([question])[0]

# Generate answer without RAG
print("\n--- Without RAG ---")
no_rag_answer = generate_answer("", question)
print(no_rag_answer)

# Retrieve relevant chunks
relevant_chunks = retriever.query(question_embedding, k=2)

print("\n--- Retrieved Context ---")
for i, chunk in enumerate(relevant_chunks):
    print(f"\nChunk {i+1}:\n{chunk[:300]}...")

context = " ".join(relevant_chunks)

# Generate answer with RAG
answer = generate_answer(context, question)
print("\n--- With RAG ---")
answer = generate_answer(context, question)
print("\nAnswer:\n", answer)