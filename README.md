# API LLM — Backend em Python

Este repositório contém uma API em Python que faz chamadas a uma LLM (modelo de linguagem). O projeto ainda está em desenvolvimento.

**Status**: Em desenvolvimento

## Estrutura (resumo)
- `api.py`: Ponto de entrada da API com rotas FastAPI.
- `llm.py`: Abstração das chamadas à LLM.
- `config.py`: Configurações e carregamento de variáveis de ambiente.
- `prompts.py`: Templates de prompts usados nas chamadas à LLM.
- `requeriments.txt`: Dependências do projeto.

## Pré-requisitos
- Python 3.10+ instalado
- Variáveis de ambiente necessárias (ex.: chave de API do provedor de LLM)

## Instalação das dependências

```bash
python -m pip install -r requeriments.txt
```

## Configuração

- Defina a chave/endpoint do provedor de LLM no ambiente: `OPENAI_API_KEY` ou outra variável usada em `config.py`.
- Você pode ajustar parâmetros no arquivo `config.py` conforme necessário.

Exemplo (Windows PowerShell):

```powershell
$env:OPENAI_API_KEY = "sua_chave_aqui"
```

## Como executar

Inicie a API com Uvicorn:

```bash
python api.py
```

A API será executada em `http://localhost:8000`

## Endpoints disponíveis

### GET /health
Verificação de saúde do serviço.

```bash
curl http://localhost:8000/health
```

**Resposta esperada:**
```json
{
  "status": "Ok",
  "service": "backend"
}
```

### POST /ai/beginner
Gera uma resposta em modo iniciante (mais simples e didático).

**Request:**
```bash
curl -X POST http://localhost:8000/ai/beginner \
  -H "Content-Type: application/json" \
  -d '{"situation":"Como começar a programar em Python?"}'
```

**Resposta:**
```json
{
  "mode": "beginner",
  "answer": "..."
}
```

### POST /ai/advanced
Gera uma resposta em modo avançado (mais técnico e detalhado).

**Request:**
```bash
curl -X POST http://localhost:8000/ai/advanced \
  -H "Content-Type: application/json" \
  -d '{"situation":"Qual é a diferença entre async/await e callbacks?"}'
```

**Resposta:**
```json
{
  "mode": "advanced",
  "answer": "..."
}
```

### POST /ai/trustable
Gera uma resposta em modo confiável (respostas bem fundamentadas e seguras).

**Request:**
```bash
curl -X POST http://localhost:8000/ai/trustable \
  -H "Content-Type: application/json" \
  -d '{"situation":"Como estruturar uma arquitetura de microserviços?"}'
```

**Resposta:**
```json
{
  "mode": "trustable",
  "answer": "..."
}
```

## Observações de desenvolvimento
- As integrações com a LLM estão centralizadas em `llm.py`.
- Os templates de prompt ficam em `prompts.py`; altere-os para ajustar o comportamento do modelo.
- `config.py` consolida variáveis de ambiente e ajustes de timeout/retry.
- Todos os endpoints POST esperam um JSON com um campo `situation` contendo a situação/pergunta para a IA processar.

## Testes e validação
- Adicione testes unitários para `llm.py` e rotas em `api.py` conforme o projeto evolui.

## Contribuição
- Abra pull requests com pequenos commits e descrições claras.

## Licença
- Escolha e adicione uma licença ao repositório (ex.: MIT) se desejar publicar.



