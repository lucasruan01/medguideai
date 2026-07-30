from app.readers.markdown_reader import load_markdown_documents
from app.readers.pdf_reader import load_pdf_documents
from app.readers.csv_reader import load_csv_documents
from app.readers.docx_reader import load_docx_documents
from app.services.chunk_service import create_chunks

def load_all_documents():
    documents = []
    documents.extend(load_markdown_documents())
    documents.extend(load_pdf_documents())
    documents.extend(load_csv_documents())
    documents.extend(load_docx_documents())
    return documents

def load_and_chunk_documents():
    documents = load_all_documents()
    all_chunks = []
    for document in documents:
        chunks = create_chunks(document)
        all_chunks.extend(chunks)
    return all_chunks