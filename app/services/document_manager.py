from app.readers.markdown_reader import load_markdown_documents
from app.readers.pdf_reader import load_pdf_documents
from app.readers.csv_reader import load_csv_documents
from app.readers.docx_reader import load_docx_documents

def load_all_documents():
    documents = []
    documents.extend(load_markdown_documents())
    documents.extend(load_pdf_documents())
    documents.extend(load_csv_documents())
    documents.extend(load_docx_documents())
    return documents