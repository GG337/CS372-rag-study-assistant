def chunk_text(text, chunk_size=300):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]

        # filter out tiny/noisy chunks
        if len(chunk.strip()) > 100:
            chunks.append(chunk)

    return chunks