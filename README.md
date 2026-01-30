
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


Endpoints (exemplos genéricos)
- `GET /health` — opcional, checagem de saúde do serviço.

Observações de desenvolvimento
- As integrações com a LLM estão centralizadas em `llm.py`.
- Os templates de prompt ficam em `prompts.py`; altere-os para ajustar o comportamento do modelo.
- `config.py` consolida variáveis de ambiente e ajustes de timeout/retry.



