from app.models.document_chunk import DocumentChunk
from app.services.vector_service import add_embedding


chunk = DocumentChunk(
    filename="teste.txt",
    type="text",
    chunk_id=1,
    text="Este é um documento de teste do MedGuide AI."
)

chunk = add_embedding(chunk)

print(f"Arquivo: {chunk.filename}")
print(f"Chunk: {chunk.chunk_id}")
print(f"Tamanho do embedding: {len(chunk.embedding)}")