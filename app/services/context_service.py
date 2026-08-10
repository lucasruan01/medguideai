def build_context(search_results):
    context_parts = []

    for result in search_results:
        context_parts.append(
            f"Arquivo: {result['filename']}\n"
            f"Conteúdo:\n{result['text']}"
        )

    return "\n\n---\n\n".join(context_parts)