# AiresBot

Chatbot rule-based para apresentar Nícolas Aires. O frontend usa React + Vite e conversa com uma API Django REST Framework.

## Rodar localmente

Em um terminal, inicie a API:

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

Abra o endereço exibido pelo Vite (por padrão `http://localhost:5173`). A API fica em `http://127.0.0.1:8000/api/chat/`.

Para apontar o frontend para outra API, defina `VITE_API_URL` no arquivo `frontend/.env.local`, por exemplo `VITE_API_URL=https://api.exemplo.com` (sem `/api/chat/`).

## Personalizar respostas

Edite `backend/chatbot/knowledge.py`: atualize o resumo e preencha idade, stack, currículo, e-mail, GitHub e LinkedIn. As respostas sobre os campos vazios informam que o dado ainda não foi cadastrado. O endpoint aceita `POST` com `{"message":"Qual é a stack?"}` e responde com `{"answer":"..."}`. As regras e frases estão em `answer_question`.

O CORS local permite `http://localhost:5173`; ajuste `CORS_ALLOWED_ORIGINS` em `backend/backend/settings.py` para outro endereço do frontend.
