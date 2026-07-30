from app.models.document_chunk import DocumentChunk


def create_chunks(document):
    """
    Splits a document into chunks of text.

    Args:
        document (dict): A document containing its filename, type, and content.

    Returns:
        list: A list of DocumentChunk objects.
    """
    chunks = []
    content = document["content"]
    paragraphs = content.split("\n\n")

    chunk_id = 1
    
    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        if len(paragraph) <= 1000:
            chunk = DocumentChunk(
                filename=document["filename"],
                type=document["type"],
                chunk_id=chunk_id,
                text=paragraph
            )
            chunks.append(chunk)
            chunk_id += 1

        else:
            for i in range(0, len(paragraph), 1000):
                sub_chunk = paragraph[i:i + 1000].strip()
                if sub_chunk:
                    chunk = DocumentChunk(
                        filename=document["filename"],
                        type=document["type"],
                        chunk_id=chunk_id,
                        text=sub_chunk
                    )
                    chunks.append(chunk)
                    chunk_id += 1

    return chunks