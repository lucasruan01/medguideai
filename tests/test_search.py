from app.services.search_service import search_documents


results = search_documents(
    "Quais convênios a clínica atende?",
    #similarity_threshold=0.60
)

for result in results:
    print(result)