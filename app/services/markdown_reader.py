from pathlib import Path

BASE_PATH = Path("data/markdown")

def load_markdown_documents():
    documents = []
    for file in BASE_PATH.glob("*.md"):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
            documents.append(text)
    return documents