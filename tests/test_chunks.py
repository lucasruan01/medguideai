#from app.services.chunk_service import create_chunks

#document = {
#    "filename": "teste.pdf",
#    "type": "pdf",
#    "content": (
#        "Este é o primeiro parágrafo do nosso documento.\n\n"
#        "Este é o segundo parágrafo. Ele também será transformado "
#        "em um chunk separado."
#    )
#}

#chunks = create_chunks(document)

#for chunk in chunks:
#    print(chunk)

from app.services.document_service import load_all_documents
from app.services.chunk_service import create_chunks


documents = load_all_documents()

for document in documents:

    if document["filename"] == "test_chunks.md":

        print(repr(document["content"]))

        chunks = create_chunks(document)

        print("=" * 60)
        print(f"Arquivo: {document['filename']}")
        print(f"Quantidade de chunks: {len(chunks)}")
        print("=" * 60)

        for chunk in chunks:
            print(f"\nChunk {chunk.chunk_id}:")
            print(chunk.text)

            assert all(len(chunk.text) <= 1000 for chunk in chunks)
            print("\n✓ Todos os chunks possuem no máximo 1000 caracteres.")