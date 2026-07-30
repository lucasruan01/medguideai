from app.services.embedding_service import create_embedding

text = "O paciente pode cancelar sua consulta com antecedência."

embedding = create_embedding(text)

print(embedding)
print(type(embedding))
print(len(embedding))