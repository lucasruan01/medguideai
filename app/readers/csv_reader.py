from pathlib import Path
import pandas as pd

CSV_FOLDER = Path("data/csv")

def load_csv_documents():
    documents = []
    for file in CSV_FOLDER.glob("*.csv"):
        df = pd.read_csv(file)
        text = df.to_string(index=False)
        documents.append(
    {
        "filename": file.name,
        "type": "csv",
        "content": text
    }
)
    return documents