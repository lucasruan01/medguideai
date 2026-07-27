from docx import Document

doc = Document(file)

text = ""

def load_docx_documents():
    documents = []
    for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
    documents.append(text)
    return documents