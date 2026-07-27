from pathlib import Path
import pandas as pd

CSV_FOLDER = Path("data/csv")

def load_csv_documents():
    documents = []
    for file in CSV_FOLDER.glob("*.csv"):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
            documents.append(text)
    return documents