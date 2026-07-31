from app.models.document_chunk import DocumentChunk
from app.services.embedding_service import create_embedding


def add_embedding(chunk: DocumentChunk) -> DocumentChunk:
    """
    Generates an embedding for a DocumentChunk
    and returns the same chunk with the embedding attached.
    """

    chunk.embedding = create_embedding(chunk.text)

    return chunk