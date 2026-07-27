from pathlib import Path

MARKDOWN_FOLDER = Path("data/markdown")

def load_markdown_documents():
    documents = []
    for file in MARKDOWN_FOLDER.glob("*.md"):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
            documents.append(
    {
        "filename": file.name,
        "type": "markdown",
        "content": text
    }
)
    return documents