from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(text):
    """
    Creates an embedding for the given text.
    Args:
        text (str): The input text.

    Returns:
        numpy.ndarray: The created embedding.
    """
    return model.encode(text)