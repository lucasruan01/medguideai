from app.services.search_service import search_documents
from app.services.context_service import build_context


question = "Quais convênios a clínica atende?"

print("=" * 60)
print(f"PERGUNTA: {question}")
print("=" * 60)

results = search_documents(question)

print("QUANTIDADE DE RESULTADOS:", len(results))

context = build_context(results)

print("\nCONTEXTO:")
print(context)