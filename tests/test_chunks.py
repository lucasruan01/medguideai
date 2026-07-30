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

from app.readers.pdf_reader import load_pdf_documents
from app.services.chunk_service import create_chunks

documents = load_pdf_documents()

for document in documents:
    chunks = create_chunks(document)

    print("\n==============================")
    print(f"Arquivo: {document['filename']}")
    print(f"Tipo: {document['type']}")
    print(f"Quantidade de chunks: {len(chunks)}")
    print("==============================")

    for chunk in chunks:
        print(f"\nChunk {chunk['chunk_id']}:")
        print(chunk["text"][:200])