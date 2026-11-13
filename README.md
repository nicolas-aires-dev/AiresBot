
# AiresBot

**Conversas no ritmo das pessoas. Conversas que geram valor.**

O AiresBot é um portfólio interativo desenvolvido para apresentar a trajetória profissional, as competências técnicas e os projetos de Nícolas Aires por meio de uma experiência conversacional.

Em vez de navegar por seções tradicionais de um currículo, o visitante pode explorar diferentes assuntos, escolher o que deseja conhecer e descobrir informações no próprio ritmo.

## Versão atual: v1.0.0

A primeira versão utiliza um mecanismo de respostas baseado em regras e palavras-chave (*rule-based*), responsável por identificar intenções a partir das mensagens recebidas e retornar conteúdos previamente cadastrados.

O conteúdo é processado no backend, enquanto o frontend oferece uma interface conversacional com:

- Perguntas sugeridas para facilitar a exploração.
- Indicador animado de digitação.
- Respostas com links clicáveis.
- Interação dinâmica sem necessidade de recarregar a página.

A aplicação não utiliza IA generativa nem autenticação nesta versão. As respostas são definidas e controladas pelo backend.

## Tecnologias

| Camada | Tecnologias |
| --- | --- |
| Frontend | React, TypeScript e Vite |
| Backend | Python, Django e Django REST Framework |
| Comunicação | API REST |
| Hospedagem | Vercel (frontend) e Render (backend) |

## Arquitetura

O projeto utiliza uma arquitetura separada entre frontend e backend:

- **Frontend:** responsável pela interface, interação com o visitante e apresentação das respostas.
- **Backend:** recebe as mensagens, processa as regras de correspondência e retorna as respostas cadastradas.
- **API REST:** estabelece a comunicação entre as duas aplicações.

## Demonstração

- **Aplicação:** [AiresBot](https://aires-bot-l9t1.vercel.app/)
- **Repositório:** [GitHub](https://github.com/nicolas-aires-dev/AiresBot)

## Como executar localmente

### Pré-requisitos

- Python 3.12+
- Node.js e npm
- Git

### 1. Backend

Na raiz do projeto, ative o ambiente virtual e acesse a pasta do backend:

```powershell
.\venv\Scripts\Activate.ps1
cd backend
```

Instale as dependências e inicie o servidor:

```powershell
pip install -r requirements.txt
python manage.py runserver
```

A API estará disponível em:

`http://127.0.0.1:8000/api/chat/`

### 2. Frontend

Em outro terminal, acesse a pasta do frontend:

```powershell
cd frontend
npm install
npm run dev
```

Acesse o endereço informado pelo Vite, normalmente:

`http://localhost:5173`

### 3. Configuração da API

Por padrão, o frontend utiliza a API local.

Para configurar outra origem, crie o arquivo `frontend/.env.local`:

```env
VITE_API_URL=https://api.exemplo.com
```

Informe somente a origem do backend, sem acrescentar `/api/chat/`.

Para permitir a comunicação com outro endereço de frontend, ajuste a variável `CORS_ALLOWED_ORIGINS` na configuração do backend.

## Personalização do conteúdo

As informações do perfil e as regras de resposta estão centralizadas em:

`backend/chatbot/knowledge.py`

Nesse arquivo, é possível adicionar ou modificar informações, palavras-chave, assuntos reconhecidos e respostas.

### Contrato da API

A API recebe mensagens por meio de uma requisição `POST`:

**Endpoint:** `/api/chat/`

**Payload:**

```json
{
  "message": "Qual é a stack do Nícolas?"
}
```

**Resposta:**

```json
{
  "answer": "..."
}
```

## Roadmap

As próximas evoluções planejadas incluem:

- **Persistência de perguntas não respondidas:** registrar perguntas sem correspondência para identificar oportunidades de melhoria na base de conhecimento.
- **Painel administrativo:** consultar perguntas pendentes, analisar recorrências e cadastrar respostas sem alterar diretamente o código-fonte.
- **Autenticação:** implementar controle de acesso para funcionalidades administrativas.
- **Aprimoramento do mecanismo de busca:** avaliar estruturas de dados e estratégias de correspondência conforme o crescimento da base de regras.
- **AiresBot v2:** explorar integração com IA para ampliar a flexibilidade e a capacidade de interação.

*Os itens acima representam funcionalidades planejadas e não fazem parte da versão atual.*
