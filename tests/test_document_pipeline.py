from app.services.document_service import load_and_chunk_documents

chunks = load_and_chunk_documents()

print(f"Total de chunks: {len(chunks)}")

for chunk in chunks:
    print(
        f"Arquivo: {chunk.filename} | "
        f"Tipo: {chunk.type} | "
        f"Chunk: {chunk.chunk_id}"
    )