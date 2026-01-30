
# API LLM — Backend em Python

Este repositório contém uma API em Python que faz chamadas a uma LLM (modelo de linguagem). O projeto ainda está em desenvolvimento, mas o README abaixo ajuda a configurar, executar e entender os pontos principais do código.

**Status**: Em desenvolvimento

**Estrutura (resumo)**
- `api.py`: Ponto de entrada da API (server / rotas).
- `llm.py`: Abstração das chamadas à LLM.
- `config.py`: Configurações e carregamento de variáveis de ambiente.
- `prompts.py`: Templates de prompts usados nas chamadas à LLM.
- `requeriments.txt`: Dependências do projeto (note o nome do arquivo).

**Pré-requisitos**
- Python 3.10+ instalado
- Variáveis de ambiente necessárias (ex.: chave de API do provedor de LLM)

Instalação das dependências:

```bash
python -m pip install -r requeriments.txt
```

Configuração (exemplo)
- Defina a chave/endpoint do provedor de LLM no ambiente: `OPENAI_API_KEY` ou outra variável usada em `config.py`.
- Você pode ajustar parâmetros no arquivo `config.py` conforme necessário.

Exemplo (Windows PowerShell):

```powershell
$env:OPENAI_API_KEY = "sua_chave_aqui"
```

Como executar

- Inicie a API (ajuste o comando se `api.py` usar outro servidor/framework):

```bash
python api.py
```

- Se `api.py` expõe uma rota de geração, um exemplo de requisição (ajuste o endpoint conforme `api.py`):

```bash
curl -X POST http://localhost:8000/generate \
	-H "Content-Type: application/json" \
	-d '{"prompt":"Escreva uma saudação curta"}'
```

Endpoints (exemplos genéricos)
- `POST /generate` — recebe JSON com `prompt` e retorna o texto gerado.
- `GET /health` — opcional, checagem de saúde do serviço.

Observações de desenvolvimento
- As integrações com a LLM estão centralizadas em `llm.py`.
- Os templates de prompt ficam em `prompts.py`; altere-os para ajustar o comportamento do modelo.
- `config.py` consolida variáveis de ambiente e ajustes de timeout/retry.

Testes e validação
- Adicione testes unitários para `llm.py` e rotas em `api.py` conforme o projeto evolui.

Contribuição
- Abra pull requests com pequenos commits e descrições claras.

Licença
- Escolha e adicione uma licença ao repositório (ex.: MIT) se desejar publicar.

---

Se quiser, eu posso:
- adaptar o README com instruções específicas do framework usado em `api.py` (Flask/FastAPI/etc.);
- adicionar exemplos de `.env` e um script de desenvolvimento (por exemplo, `run.sh` ou `run.ps1`);
- revisar `config.py` e sugerir variáveis de ambiente concretas.
