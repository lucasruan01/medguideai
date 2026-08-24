# MedGuide AI

Assistente inteligente para clínicas, desenvolvido em Python, capaz de consultar documentos institucionais utilizando busca semântica e gerar respostas contextualizadas com um modelo de linguagem local.

O projeto foi desenvolvido como uma aplicação de **RAG (Retrieval-Augmented Generation)**, combinando ingestão de documentos, geração de embeddings, busca semântica, construção de contexto, guardrails e geração de respostas.

---

## Sobre o projeto

O MedGuide AI tem como objetivo permitir que usuários façam perguntas sobre informações presentes nos documentos de uma clínica.

Em vez de simplesmente enviar a pergunta diretamente para um modelo de linguagem, a aplicação primeiro procura informações relevantes nos documentos cadastrados. Os resultados encontrados são utilizados para construir um contexto, que posteriormente é enviado ao modelo de linguagem para geração da resposta.

Além disso, o projeto possui uma camada de **guardrails**, responsável por impedir que o modelo gere respostas quando não existem informações suficientes nos documentos.

### Fluxo principal

```text
Usuário
   ↓
Interface Web
   ↓
Flask
   ↓
Answer Service
   ↓
Guardrails
   ↓
Busca Semântica
   ↓
Supabase / Vetores
   ↓
Construção do Contexto
   ↓
LLM Local
   ↓
Resposta
   ↓
Interface Web
```

---

# Funcionalidades

* Interface web para interação com o assistente
* Perguntas em linguagem natural
* Busca semântica utilizando embeddings
* Armazenamento de documentos e embeddings no Supabase
* Construção de contexto a partir dos documentos encontrados
* Geração de respostas utilizando LLM local
* Guardrails para evitar respostas sem suporte documental
* Suporte à ingestão de diferentes formatos de documentos
* Testes funcionais e testes de integração
* Tratamento de casos extremos nos guardrails

---

# Arquitetura

O projeto foi organizado separando as principais responsabilidades da aplicação.

```text
medguideai/
│
├── app/
│   ├── models/
│   │
│   ├── readers/
│   │   ├── markdown_reader.py
│   │   ├── pdf_reader.py
│   │   ├── csv_reader.py
│   │   └── docx_reader.py
│   │
│   ├── routes/
│   │   └── chat.py
│   │
│   ├── services/
│   │   ├── answer_service.py
│   │   ├── agent_service.py
│   │   ├── chunk_service.py
│   │   ├── context_service.py
│   │   ├── document_service.py
│   │   ├── embedding_service.py
│   │   ├── guardrail_service.py
│   │   ├── ingestion_service.py
│   │   ├── llm_service.py
│   │   ├── search_service.py
│   │   ├── supabase_service.py
│   │   └── vector_service.py
│   │
│   └── utils/
│       └── config.py
│
├── data/
│   └── markdown/
│       ├── consultas.md
│       └── convenios.md
│
├── static/
│   └── js/
│       └── chat.js
│
├── templates/
│   └── index.html
│
├── tests/
│   ├── test_answer.py
│   ├── test_answer_guardrail.py
│   ├── test_chunks.py
│   ├── test_context.py
│   ├── test_document_pipeline.py
│   ├── test_embeddings.py
│   ├── test_guardrail.py
│   ├── test_llm.py
│   ├── test_real_embeddings.py
│   └── test_search.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

> Arquivos `.env` e arquivos gerados como `__pycache__` não devem ser versionados.

---

# Pipeline de documentos

A aplicação possui uma etapa de ingestão responsável por transformar documentos em dados que podem ser utilizados pela busca semântica.

O fluxo é:

```text
Documento
   ↓
Document Reader
   ↓
Chunk
   ↓
Embedding
   ↓
Supabase
```

## 1. Leitura

Os documentos são carregados através dos readers específicos para cada formato.

Atualmente existem readers para:

* Markdown
* PDF
* CSV
* DOCX

A função `load_all_documents()` centraliza o carregamento dos documentos.

---

## 2. Chunking

Os documentos são divididos em chunks menores através do `chunk_service.py`.

Isso permite que a busca semântica trabalhe com partes específicas dos documentos, em vez de precisar comparar a pergunta com um documento inteiro.

---

## 3. Embeddings

Cada chunk recebe um embedding utilizando o serviço de embeddings.

O embedding representa semanticamente o conteúdo do texto em forma vetorial.

Esses vetores são posteriormente utilizados para comparar a pergunta do usuário com os documentos armazenados.

---

## 4. Armazenamento

Os chunks e seus embeddings são armazenados no Supabase.

Cada registro contém informações como:

```text
filename
type
chunk_id
text
embedding
```

---

# Busca semântica

Quando o usuário faz uma pergunta, o sistema gera um embedding para a pergunta e consulta os documentos armazenados.

```text
Pergunta
   ↓
Embedding da pergunta
   ↓
Busca vetorial
   ↓
Resultados relevantes
   ↓
Filtro por similaridade
   ↓
Contexto
```

A busca utiliza a função RPC `match_document_chunks` no Supabase.

Os resultados são avaliados de acordo com sua similaridade com a pergunta.

Os resultados mais relevantes são utilizados na construção do contexto enviado ao modelo de linguagem.

---

# Guardrails

Uma das partes importantes do projeto é a camada de segurança implementada em:

```text
app/services/guardrail_service.py
```

O objetivo dos guardrails é impedir que o sistema gere respostas quando não existem informações suficientes para responder à pergunta.

Atualmente existem validações para:

### Pergunta

Verifica se a pergunta recebida é válida.

```text
validate_question()
```

### Resultados da busca

Verifica se existem resultados relevantes e se a similaridade encontrada é suficiente.

```text
validate_search_results()
```

### Contexto

Verifica se o contexto construído contém informação válida.

```text
validate_context()
```

Caso alguma dessas validações falhe, o sistema retorna:

```text
Não encontrei informações suficientes nos documentos.
```

Isso reduz o risco de o modelo de linguagem inventar informações que não estão presentes na base documental.

---

# Geração de respostas

Depois que os guardrails permitem a continuação do fluxo, o sistema constrói um contexto utilizando os resultados encontrados.

Esse contexto é enviado para o serviço responsável pelo modelo de linguagem local:

```text
app/services/llm_service.py
```

O modelo recebe:

```text
Pergunta do usuário
+
Contexto recuperado dos documentos
```

e gera uma resposta baseada nessas informações.

---

# Interface Web

A aplicação utiliza Flask para disponibilizar uma interface simples de interação.

O servidor é iniciado através de:

# Executando a aplicação localmente

Com o ambiente virtual ativado:

```bash
python run.py
```

A página principal apresenta um campo para o usuário enviar sua pergunta.

A comunicação entre frontend e backend acontece através de uma requisição HTTP:

```text
Browser
   ↓
POST /chat
   ↓
Flask
   ↓
Answer Service
   ↓
Resposta JSON
   ↓
Browser
```

O endpoint utilizado é:

```text
POST /chat
```

O corpo da requisição possui o formato:

```json
{
  "question": "Quais convênios a clínica atende?"
}
```

E a resposta:

```json
{
  "answer": "A clínica atende aos seguintes convênios: Unimed, Bradesco Saúde, SulAmérica e Amil."
}
```

---

# Testes

O projeto possui testes para diferentes partes do pipeline.

## Teste dos guardrails

```bash
python -m tests.test_guardrail
```

Esse teste verifica:

* Perguntas válidas
* Perguntas vazias
* Resultados sem similaridade suficiente
* Similaridade ausente
* Similaridade `None`
* Contexto vazio
* Contexto `None`
* Pergunta `None`

---

## Teste de busca

```bash
python -m tests.test_search
```

Utilizado para verificar os resultados retornados pela busca semântica para diferentes perguntas.

---

## Teste de contexto

```bash
python -m tests.test_context
```

Verifica a construção do contexto a partir dos resultados recuperados.

---

## Teste de respostas

```bash
python -m tests.test_answer
```

Testa o fluxo completo de geração de respostas para perguntas conhecidas e perguntas sem informação suficiente nos documentos.

Entre os cenários testados estão:

* Convênios
* Antecedência para chegada
* Agendamento
* Cancelamento
* Perguntas sem informação documental
* Convênio inexistente

---

## Teste de integração Answer Service + Guardrails

```bash
python -m tests.test_answer_guardrail
```

Verifica principalmente se:

1. Uma pergunta sem informação suficiente é bloqueada antes da chamada do LLM.
2. Uma pergunta com informação suficiente consegue chegar ao LLM.

---

# Exemplos

Considerando os documentos atualmente utilizados pelo projeto:

### Pergunta

```text
Quais convênios a clínica atende?
```

### Resposta esperada

```text
A clínica atende aos seguintes convênios:
Unimed, Bradesco Saúde, SulAmérica e Amil.
```

---

### Pergunta

```text
Com quanto tempo de antecedência o paciente deve chegar?
```

### Resposta

```text
20 minutos de antecedência.
```

---

### Pergunta sem informação documental

```text
Qual é o telefone da clínica?
```

### Resposta

```text
Não encontrei informações suficientes nos documentos.
```

Nesse caso, o guardrail impede que o modelo tente inventar uma resposta.

---

# Tecnologias utilizadas

* **Python**
* **Flask**
* **Supabase**
* **Embeddings**
* **LLM local**
* **JavaScript**
* **HTML**
* **Git / GitHub**

---

# 📦 Instalação

## 1. Clonar o projeto

```bash
git clone <URL_DO_REPOSITORIO>
```

Entrar no diretório:

```bash
cd medguideai
```

---

## 2. Criar ambiente virtual

No Windows:

```bash
python -m venv .venv
```

Ativar:

```powershell
.venv\Scripts\Activate.ps1
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Configuração

O projeto utiliza variáveis de ambiente para configurar o acesso ao Supabase.

Crie um arquivo:

```text
.env
```

com as configurações necessárias.

Exemplo:

```env
SUPABASE_URL=seu_supabase_url
SUPABASE_KEY=sua_supabase_key
```

> Nunca publique credenciais reais no GitHub.

O projeto também possui um `.env.example` para indicar quais variáveis são necessárias sem expor informações sensíveis.

---

# Supabase

O projeto utiliza o Supabase para armazenar os chunks dos documentos e seus embeddings.

A tabela principal utilizada pelo pipeline é:

```text
document_chunks
```

Os dados armazenados incluem:

```text
id
filename
type
chunk_id
text
embedding
```

A busca semântica utiliza a função RPC:

```text
match_document_chunks
```

---

# Ingestão dos documentos

Após configurar o ambiente e o Supabase, os documentos podem ser ingeridos através do pipeline de ingestão.

O fluxo utilizado é:

```text
data/
   ↓
load_all_documents()
   ↓
create_chunks()
   ↓
add_embedding()
   ↓
save_document_chunk()
```

Quando documentos forem alterados, é necessário executar novamente o processo de ingestão para que os novos conteúdos sejam representados no banco vetorial.

O projeto possui também o script auxiliar:

```text
reingest.py
```

para facilitar esse processo.

---

# Executando a aplicação

Com o ambiente virtual ativado:

```bash
python run.py
```

O Flask iniciará o servidor local.

Depois, abra no navegador o endereço indicado pelo Flask, normalmente:

```text
http://127.0.0.1:5000
```

---

# Estrutura do fluxo de uma pergunta

Uma pergunta percorre as seguintes etapas:

```text
1. Usuário envia pergunta
          ↓
2. Flask recebe POST /chat
          ↓
3. Answer Service recebe pergunta
          ↓
4. Guardrail valida pergunta
          ↓
5. Busca semântica gera embedding
          ↓
6. Supabase retorna documentos relevantes
          ↓
7. Guardrail valida resultados
          ↓
8. Context Service constrói contexto
          ↓
9. Guardrail valida contexto
          ↓
10. LLM recebe pergunta + contexto
          ↓
11. Resposta é gerada
          ↓
12. Flask retorna JSON
          ↓
13. Interface exibe resposta
```

---

# Objetivo técnico

O principal objetivo técnico do projeto foi desenvolver uma aplicação capaz de combinar:

* processamento de documentos;
* embeddings;
* busca semântica;
* banco de dados vetorial;
* construção de contexto;
* modelo de linguagem local;
* guardrails;
* API HTTP;
* interface web.

O projeto também foi estruturado de forma modular para facilitar manutenção, testes e futuras evoluções.

---

# Possíveis melhorias futuras

Algumas evoluções possíveis para versões futuras:

* Melhorar a estratégia de chunking;
* Implementar busca híbrida (semântica + lexical);
* Melhorar o ranking dos resultados;
* Utilizar reranking;
* Adicionar mais formatos de documentos;
* Implementar autenticação de usuários;
* Adicionar histórico de conversas;
* Melhorar a interface web;
* Adicionar observabilidade e logging estruturado;
* Criar testes automatizados com `pytest`;
* Adicionar testes de carga;
* Melhorar o tratamento de erros da API;
* Configurar HTTPS com domínio próprio;
* Adicionar avaliação automatizada da qualidade das respostas.

---

# Status do projeto

**Status: MVP funcional e disponível online**

O fluxo principal está implementado e a aplicação está hospedada em uma instância Oracle Cloud Infrastructure (OCI).

```text
Documentos
   ↓
Ingestão
   ↓
Chunks
   ↓
Embeddings
   ↓
Supabase
   ↓
Busca semântica
   ↓
Guardrails
   ↓
Contexto
   ↓
LLM local
   ↓
Resposta
   ↓
Interface Web
```

O projeto possui testes funcionais e de integração para validar as principais etapas do pipeline. 

---

## Aplicação

A aplicação está hospedada no Oracle Cloud Infrastructure (OCI).

### Live Demo

**[Acessar o MedGuide AI](http://132.145.140.202/)**

A demonstração fornece um assistente clínico baseado em RAG utilizando:

- Flask
- Supabase + pgvector
- Sentence Transformers
- Ollama
- Qwen3 1.7B
- Gunicorn
- Nginx
- Oracle Cloud Infrastructure

---

#  Autor

**Lucas Ruan da Silva Santos**

Projeto desenvolvido como parte da formação em desenvolvimento de software, com foco em Python, integração de serviços, inteligência artificial e arquitetura de aplicações.

---

# Licença

Este projeto foi desenvolvido para fins educacionais e de demonstração.

Adicione uma licença específica ao repositório caso o projeto seja posteriormente distribuído ou utilizado comercialmente.
