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

    def split_paragraph(paragraph, max_chars=1000):
        words = paragraph.split()
        if not words:
            return []

        chunks = []
        current = []

        for word in words:
            candidate = f"{' '.join(current)} {word}".strip() if current else word

            if len(candidate) <= max_chars:
                current.append(word)
            else:
                if current:
                    chunks.append(" ".join(current))
                current = [word]

        if current:
            chunks.append(" ".join(current))

        return chunks

    paragraphs = [
        paragraph.strip()
        for paragraph in content.split("\n\n")
        if paragraph.strip()
    ]

    chunk_id = 1
    current_chunk = ""

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if not paragraph:
            continue

        print("=" * 60)
        print("NOVO PARÁGRAFO")
        print("Tamanho:", len(paragraph))
        print("Começo:", paragraph[:100])
        print("=" * 60)

        # Caso o próprio parágrafo seja maior que 1000 caracteres
        if len(paragraph) > 1000:

            # Primeiro salva o que já estava sendo acumulado
            if current_chunk:
                chunks.append(
                    DocumentChunk(
                        filename=document["filename"],
                        type=document["type"],
                        chunk_id=chunk_id,
                        text=current_chunk
                    )
                )

                chunk_id += 1
                current_chunk = ""

            # Divide o parágrafo grande em partes de até 1000 caracteres sem cortar palavras ao meio
            for sub_chunk in split_paragraph(paragraph, 1000):
                chunks.append(
                    DocumentChunk(
                        filename=document["filename"],
                        type=document["type"],
                        chunk_id=chunk_id,
                        text=sub_chunk
                    )
                )

                chunk_id += 1

        # Parágrafo normal
        elif not current_chunk:

            current_chunk = paragraph

        # Tenta adicionar o parágrafo ao chunk atual
        elif len(current_chunk) + len("\n\n") + len(paragraph) <= 1000:

            current_chunk += "\n\n" + paragraph

        # Não cabe: salva o chunk atual e começa outro
        else:

            chunks.append(
                DocumentChunk(
                    filename=document["filename"],
                    type=document["type"],
                    chunk_id=chunk_id,
                    text=current_chunk
                )
            )

            chunk_id += 1
            current_chunk = paragraph

    # Salva o último chunk restante
    if current_chunk:

        chunks.append(
            DocumentChunk(
                filename=document["filename"],
                type=document["type"],
                chunk_id=chunk_id,
                text=current_chunk
            )
        )

    return chunks