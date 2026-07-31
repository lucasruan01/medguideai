from app.services.supabase_service import supabase


response = (
    supabase
    .table("document_chunks")
    .select("*")
    .limit(1)
    .execute()
)

print(response.data)