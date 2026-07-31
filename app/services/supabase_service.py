from supabase import create_client
from app.utils.config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

def save_document_chunk(chunk):
    """
    Saves a DocumentChunk object to the Supabase database.

    Args:
        chunk (DocumentChunk): The DocumentChunk object to be saved.

    Returns:
        dict: The response from the Supabase database.
    """
    data = {
        "filename": chunk.filename,
        "type": chunk.type,
        "chunk_id": chunk.chunk_id,
        "text": chunk.text,
        "embedding": chunk.embedding.tolist() if chunk.embedding is not None else None
    }
    response = (
        supabase
        .table("document_chunks")
        .insert(data)
        .execute()
    )
    return response.data