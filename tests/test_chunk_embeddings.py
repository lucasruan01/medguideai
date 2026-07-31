from app.services.embedding_service import create_embedding
from app.models.document_chunk import DocumentChunk

chunk = DocumentChunk(
    filename="document.txt",
    type="text",
    chunk_id=1,
    text="Este é um exemplo de documento."
)
embedding = create_embedding(chunk.text)
print(len(embedding))