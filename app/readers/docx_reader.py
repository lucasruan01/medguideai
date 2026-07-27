from pathlib import Path
from docx import Document

DOCX_FOLDER = Path("data/docx")

def load_docx_documents():
    documents = []
    for file in DOCX_FOLDER.glob("*.docx"):
        doc = Document(file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        documents.append(
    {
        "filename": file.name,
        "type": "docx",
        "content": text
    }
)
    return documents