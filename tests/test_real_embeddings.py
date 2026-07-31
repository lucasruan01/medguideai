from app.services.document_service import load_and_chunk_documents
from app.services.embedding_service import create_embedding

for chunk in load_and_chunk_documents():
    embedding = create_embedding(chunk.text)
    print(
        f"Arquivo: {chunk.filename} | "
        f"Tipo: {chunk.type} | "
        f"Chunk: {chunk.chunk_id} | "
        f"Texto: {chunk.text[:50]}... | "
        f"Tamanho do embedding: {len(embedding)}"
    )