from app.services.guardrail_service import (
FALLBACK_ANSWER,
validate_question,
validate_search_results,
validate_context,
)

print("=" * 70)
print("TESTE RÍGIDO DOS GUARDRAILS")
print("=" * 70)

# ============================================================

# 1. TESTES DE PERGUNTA

# ============================================================

question_tests = [
("Pergunta válida", "Quais convênios a clínica atende?", True),
("Pergunta vazia", "", False),
("Somente espaços", "     ", False),
("Pergunta muito curta", "Oi", True),
("Pergunta com espaços", "  Quais convênios a clínica atende?  ", True),
]

print("\n" + "=" * 70)
print("1. TESTES DE PERGUNTA")
print("=" * 70)

for name, question, expected in question_tests:
    result = validate_question(question)

status = "PASSOU" if result == expected else "FALHOU"

print(f"\n{name}")
print(f"Entrada: {repr(question)}")
print(f"Esperado: {expected}")
print(f"Obtido:   {result}")
print(f"Status:   {status}")

# ============================================================

# 2. TESTES DE RESULTADOS DA BUSCA

# ============================================================

search_tests = [
(
"Resultado forte",
[
{
"filename": "convenios.md",
"similarity": 0.73,
"text": "A clínica atende Unimed, Bradesco Saúde, SulAmérica e Amil."
}
],
True,
),
(
"Resultado exatamente no limite",
[
{
"filename": "convenios.md",
"similarity": 0.55,
"text": "A clínica atende Unimed."
}
],
True,
),
(
"Resultado abaixo do limite",
[
{
"filename": "convenios.md",
"similarity": 0.54,
"text": "A clínica atende Unimed."
}
],
False,
),
(
"Resultado muito baixo",
[
{
"filename": "convenios.md",
"similarity": 0.10,
"text": "A clínica atende Unimed."
}
],
False,
),
(
"Lista vazia",
[],
False,
),
(
"Similarity igual a zero",
[
{
"filename": "convenios.md",
"similarity": 0,
"text": "A clínica atende Unimed."
}
],
False,
),
]

print("\n" + "=" * 70)
print("2. TESTES DE RESULTADOS DA BUSCA")
print("=" * 70)

for name, search_results, expected in search_tests:
    result = validate_search_results(search_results)

status = "PASSOU" if result == expected else "FALHOU"

print(f"\n{name}")
print(f"Esperado: {expected}")
print(f"Obtido:   {result}")
print(f"Status:   {status}")

# ============================================================

# 3. TESTES DE CONTEXTO

# ============================================================

context_tests = [
(
"Contexto válido",
"""
Arquivo: convenios.md

A clínica atende:

Unimed
Bradesco Saúde
SulAmérica
Amil
""",
True,
),
(
"Contexto vazio",
"",
False,
),
(
"Contexto somente com espaços",
"     ",
False,
),
(
"Contexto com uma informação",
"Arquivo: convenios.md\nA clínica atende Unimed.",
True,
),
]

print("\n" + "=" * 70)
print("3. TESTES DE CONTEXTO")
print("=" * 70)

for name, context, expected in context_tests:
    result = validate_context(context)

status = "PASSOU" if result == expected else "FALHOU"

print(f"\n{name}")
print(f"Esperado: {expected}")
print(f"Obtido:   {result}")
print(f"Status:   {status}")

# ============================================================

# 4. TESTES DE CASOS EXTREMOS

# ============================================================

print("\n" + "=" * 70)
print("4. TESTES DE CASOS EXTREMOS")
print("=" * 70)

# Similaridade ausente

search_results = [
{
"filename": "convenios.md",
"text": "A clínica atende Unimed."
}
]

try:
    result = validate_search_results(search_results)

    print("\nSimilarity ausente")
    print(f"Resultado: {result}")
    print("Status: PASSOU - função não gerou exceção")


except Exception as error:
    print("\nSimilarity ausente")
    print(f"Status: FALHOU - exceção: {error}")

# Similaridade None

search_results = [
{
"filename": "convenios.md",
"similarity": None,
"text": "A clínica atende Unimed."
}
]

try:
    result = validate_search_results(search_results)

    print("\nSimilarity None")
    print(f"Resultado: {result}")
    print("Status: PASSOU - função não gerou exceção")

except Exception as error:
    print("\nSimilarity None")
    print(f"Status: FALHOU - exceção: {error}")

# Contexto None

try:
    result = validate_context(None)

    print("\nContexto None")
    print(f"Resultado: {result}")
    print("Status: PASSOU - função não gerou exceção")

except Exception as error:
    print("\nContexto None")
    print(f"Status: FALHOU - exceção: {error}")

# Pergunta None

try:
    result = validate_question(None)

    print("\nPergunta None")
    print(f"Resultado: {result}")
    print("Status: PASSOU - função não gerou exceção")

except Exception as error:
    print("\nPergunta None")
    print(f"Status: FALHOU - exceção: {error}")

print("\n" + "=" * 70)
print("FIM DO TESTE RÍGIDO")
print("=" * 70)
