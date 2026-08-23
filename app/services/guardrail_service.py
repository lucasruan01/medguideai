FALLBACK_ANSWER = "Não encontrei informações suficientes nos documentos."


def validate_question(question):
    if not question:
        return False

    if not question.strip():
        return False

    return True


def validate_search_results(search_results, minimum_similarity=0.40):
    if not search_results:
        return False

    best_similarity = search_results[0].get("similarity", 0)

    if best_similarity is None:
        return False

    if best_similarity < minimum_similarity:
        return False

    return True

def validate_context(context):
    if not context:
        return False

    if not context.strip():
        return False

    return True
