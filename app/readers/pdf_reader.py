from pypdf import PdfReader

reader = PdfReader(file)

text = ""

def load_pdf_documents():
    documents = []
    for page in reader.pages:
        text += page.extract_text()
    documents.append(text)
    return documents