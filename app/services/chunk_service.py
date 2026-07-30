def create_chunks(document):
    """
    Splits a document into chunks of text.

    Args:
        document (dict): A dictionary containing the document's filename, type, and content.

    Returns:
        list: A list of dictionaries, each containing a chunk of text and its metadata.
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
            chunks.append({
                "filename": document["filename"],
                "type": document["type"],
                "chunk_id": chunk_id,
                "text": paragraph
            })
            chunk_id += 1

        else:
            for i in range(0, len(paragraph), 1000):
                sub_chunk = paragraph[i:i + 1000].strip()
                if sub_chunk:
                    chunks.append({
                        "filename": document["filename"],
                        "type": document["type"],
                        "chunk_id": chunk_id,
                        "text": sub_chunk
                    })
                    chunk_id += 1
            
    return chunks