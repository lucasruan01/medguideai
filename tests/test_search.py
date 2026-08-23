from app.services.search_service import search_documents


questions = [
    "Quanto tempo antes devo chegar?",
    "Como faço para agendar uma consulta?",
    "Posso cancelar minha consulta?",
    "Até quando posso cancelar?"
]


for question in questions:

    print("\n" + "=" * 60)
    print(f"PERGUNTA: {question}")
    print("=" * 60)

    results = search_documents(question, similarity_threshold=0.40)

    if not results:
        print("Nenhum documento relevante encontrado.")
        continue

    for result in results:
        print(
            f"\nArquivo: {result['filename']}"
            f"\nTipo: {result['type']}"
            f"\nChunk: {result['chunk_id']}"
            f"\nSimilaridade: {result['similarity']:.4f}"
            f"\nTexto: {result['text']}"
        )