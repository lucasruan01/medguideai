from pathlib import Path
from pypdf import PdfReader

PDF_FOLDER = Path("data/pdf")

def load_pdf_documents():
    documents = []
    for file in PDF_FOLDER.glob("*.pdf"):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()
        documents.append(
        {
        "filename": file.name,
        "type": "pdf",
        "content": text
        }
)
    return documents