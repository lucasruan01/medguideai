from app.models.document_chunk import DocumentChunk
from app.services.embedding_service import create_embedding
from app.services.supabase_service import save_document_chunk


text = "Este é um documento de teste do MedGuide AI."

embedding = create_embedding(text)

chunk = DocumentChunk(
    filename="teste.txt",
    type="text",
    chunk_id=1,
    text=text,
    embedding=embedding
)

response = save_document_chunk(chunk)

print(response)