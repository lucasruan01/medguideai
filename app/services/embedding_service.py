from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(text):
    """
    Creates an embedding for the given text using the SentenceTransformer model.

    Args:
        text (str): The input text to create an embedding for.

    Returns:
        numpy.ndarray: The created embedding.
    """
    return model.encode(text)