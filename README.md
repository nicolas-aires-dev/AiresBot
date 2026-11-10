# AiresBot

Chatbot de portfólio criado para apresentar a trajetória, as tecnologias e os projetos do Nícolas de forma interativa.

## Versão atual: v1

A v1 usa regras e palavras-chave para identificar a intenção da pergunta e retornar uma resposta cadastrada. O frontend oferece uma interface de chat, perguntas sugeridas, indicador animado de digitação e links clicáveis nas respostas.

Esta versão **não possui autenticação** e não usa IA para gerar respostas: o conteúdo é definido no backend.

## Tecnologias

- **Frontend:** React, TypeScript e Vite
- **Backend:** Python, Django e Django REST Framework
- **Comunicação:** API REST com CORS configurado para desenvolvimento local

## Como executar localmente

Na raiz do projeto, abra um terminal e inicie o backend:

```powershell
.\venv\Scripts\Activate.ps1
cd backend
python manage.py runserver
```

Em outro terminal, inicie o frontend:

```powershell
cd frontend
npm install
npm run dev
```

Acesse o endereço informado pelo Vite, normalmente `http://localhost:5173`. A API fica disponível em `http://127.0.0.1:8000/api/chat/`.

Para usar outra URL de API, crie `frontend/.env.local` e defina `VITE_API_URL` com a origem do backend, sem acrescentar `/api/chat/`:

```env
VITE_API_URL=https://api.exemplo.com
```

O CORS local permite `http://localhost:5173`. Para outro endereço de frontend, atualize `CORS_ALLOWED_ORIGINS` em `backend/backend/settings.py`.

## Personalizar o conteúdo

As informações do perfil e as regras de resposta ficam em `backend/chatbot/knowledge.py`. Edite os dados do perfil e a função `answer_question` para acrescentar ou ajustar assuntos, palavras-chave e respostas.

A API recebe uma pergunta por `POST`:

```json
{
  "message": "Qual é a stack do Nícolas?"
}
```

E retorna uma resposta neste formato:

```json
{
  "answer": "..."
}
```

## Próximos passos

- **Autenticação:** planejo implementar autenticação em sessões numa etapa futura.
- **v2 com IA:** mais adiante, pretendo lançar a v2 integrada com IA para ampliar a experiência de conversa.

Esses itens fazem parte do roadmap e ainda não estão disponíveis na versão atual.
