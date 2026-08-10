from app.services.embedding_service import create_embedding
from app.services.supabase_service import supabase


def search_documents(question, similarity_threshold=0.50):
    query_embedding = create_embedding(question)

    response = supabase.rpc(
        "match_document_chunks",
        {
            "query_embedding": query_embedding.tolist(),
            "match_count": 3
        }
    ).execute()

    #print("RESULTADOS BRUTOS:")
    #print(response)

    results = response.data

    filtered_results = [
        result
        for result in results
        if result["similarity"] >= similarity_threshold
    ]

    return filtered_results[:3]  # Retorna no máximo 3 resultados