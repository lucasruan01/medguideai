from app.services.document_service import load_all_documents
from app.services.chunk_service import create_chunks
from app.services.vector_service import add_embedding
from app.services.supabase_service import save_document_chunk

def ingest_documents():
    documents = load_all_documents()

    for document in documents:

        chunks = create_chunks(document)

        for chunk in chunks:

            chunk = add_embedding(chunk)

            save_document_chunk(chunk)