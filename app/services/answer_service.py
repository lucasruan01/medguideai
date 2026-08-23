from app.services.search_service import search_documents
from app.services.context_service import build_context
from app.services.llm_service import generate_answer
from app.services.guardrail_service import (
    FALLBACK_ANSWER,
    validate_question,
    validate_search_results,
    validate_context
)


def answer_question(question, similarity_threshold=0.40):

    if not validate_question(question):
        return FALLBACK_ANSWER

    search_results = search_documents(
        question,
        similarity_threshold
    )

    if not validate_search_results(
        search_results,
        minimum_similarity=similarity_threshold
    ):
        return FALLBACK_ANSWER

    context = build_context(search_results)

    if not validate_context(context):
        return FALLBACK_ANSWER

    return generate_answer(question, context)