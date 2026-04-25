from transformers import pipeline

generator = pipeline("text-generation", model="microsoft/phi-2")

def generate_answer(context, question):
    prompt = f"""
Answer the question using ONLY the context below.
Be concise.

Context:
{context}

Question:
{question}

Answer:
"""
    result = generator(prompt, max_new_tokens=120)
    return result[0]["generated_text"].split("Answer:")[-1].strip()