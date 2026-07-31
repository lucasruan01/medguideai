from dataclasses import dataclass

@dataclass
class DocumentChunk:
    filename: str
    type: str
    chunk_id: int
    text: str
    #embedding: list = None