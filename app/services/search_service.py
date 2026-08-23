from app.services.embedding_service import create_embedding
from app.services.supabase_service import supabase


def search_documents(question, similarity_threshold=0.40, match_count=5):
    query_embedding = create_embedding(question)

    response = supabase.rpc(
        "match_document_chunks",
        {
            "query_embedding": query_embedding.tolist(),
            "match_count": match_count
        }
    ).execute()

    results = response.data or []

    filtered_results = [
        result
        for result in results
        if result.get("similarity", 0) >= similarity_threshold
    ]

    filtered_results.sort(
    key=lambda result: result.get("similarity", 0),
    reverse=True
    )

    return filtered_results[:3]