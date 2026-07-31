from dataclasses import dataclass
from typing import Optional
import numpy as np

@dataclass
class DocumentChunk:
    filename: str
    type: str
    chunk_id: int
    text: str
    embedding: Optional[np.ndarray] = None