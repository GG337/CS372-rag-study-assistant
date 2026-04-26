from transformers import pipeline

generator = pipeline("text-generation", model="microsoft/phi-2")

def generate_answer(context, question, style=1):
    if style == 1:
        prompt = f"""
Answer the question using the context.

Context:
{context[:500]}

Question:
{question}

Answer:
"""
    elif style == 2:
        prompt = f"""
You are a helpful AI tutor. Answer clearly and concisely in 2 sentences.

Context:
{context[:500]}

Question:
{question}

Answer:
"""
    elif style == 3:
        prompt = f"""
Using only the information below, explain the answer step-by-step.

Context:
{context[:500]}

Question:
{question}

Step-by-step answer:
"""

    result = generator(
        prompt,
        max_new_tokens=80,
        do_sample=False
    )

    text = result[0]["generated_text"]
    return text.split("Answer:")[-1].strip()