from app.services.search_service import search_documents
from app.services.context_service import build_context
from app.services.llm_service import generate_answer


def answer_question(question, similarity_threshold=0.50):

    search_results = search_documents(
        question,
        similarity_threshold
    )

    if not search_results:
        return "Não encontrei informações suficientes nos documentos."

    context = build_context(search_results)

    return generate_answer(question, context)