"""Personal data used by the rule-based chatbot.

Replace the TODO values with verified information before publishing the project.
"""

PROFILE = {
    "name": "Nícolas Santos",
    "headline": "Desenvolvedor de software",
    "summary": "Sou desenvolvedor de software. Estou organizando este espaço para compartilhar minha trajetória e meus projetos.",
    "age": None,  # Example: 25
    "stack": [],  # Example: ["Python", "Django REST Framework", "React", "TypeScript"]
    "resume_url": None,
    "email": None,
    "github_url": None,
    "linkedin_url": None,
    "location": "Brasil",
    "looking_for": "oportunidades na área de desenvolvimento de software",
}

FALLBACK = (
    "Ainda não tenho uma resposta cadastrada para essa pergunta. Você pode perguntar "
    "sobre quem é o Nícolas, sua stack, idade, currículo, contato, GitHub ou LinkedIn."
)


def _has_any(text: str, *terms: str) -> bool:
    return any(term in text for term in terms)


def _value_or_pending(value, label: str) -> str:
    if not value:
        return f"Essa informação ainda não foi adicionada ao perfil do Nícolas."
    return f"{label}: {value}"


def answer_question(message: str) -> str:
    """Match common Portuguese questions to a small set of profile intents."""
    text = " ".join(message.casefold().replace("?", " ").replace("!", " ").split())
    name = PROFILE["name"]

    if _has_any(text, "oi", "olá", "ola", "bom dia", "boa tarde", "boa noite") and len(text.split()) <= 3:
        return f"Oi! Sou o AiresBot. Posso contar um pouco sobre {name} e seus projetos."
    if _has_any(text, "quem é", "quem e", "sobre", "apresenta", "fale de", "me fale"):
        return f"{name} é {PROFILE['headline']}. {PROFILE['summary']}"
    if _has_any(text, "stack", "tecnologias", "tecnologia", "linguagens", "framework", "ferramentas"):
        stack = PROFILE["stack"]
        return f"A stack de {name} inclui: {', '.join(stack)}." if stack else _value_or_pending(stack, "Stack")
    if _has_any(text, "idade", "quantos anos", "anos tem"):
        age = PROFILE["age"]
        return f"{name} tem {age} anos." if age else _value_or_pending(age, "Idade")
    if _has_any(text, "currículo", "curriculo", "cv", "resume", "experiência", "experiencia", "formação", "formacao"):
        url = PROFILE["resume_url"]
        return f"Você pode acessar o currículo de {name} aqui: {url}" if url else _value_or_pending(url, "Link do currículo")
    if _has_any(text, "contato", "contatar", "email", "e-mail", "falar com", "telefone"):
        email = PROFILE["email"]
        return f"Você pode entrar em contato com {name} pelo e-mail {email}." if email else _value_or_pending(email, "Contato")
    if "github" in text:
        url = PROFILE["github_url"]
        return f"O GitHub de {name} está em {url}." if url else _value_or_pending(url, "GitHub")
    if "linkedin" in text or "linked in" in text:
        url = PROFILE["linkedin_url"]
        return f"O LinkedIn de {name} está em {url}." if url else _value_or_pending(url, "LinkedIn")
    if _has_any(text, "vaga", "oportunidade", "trabalho", "buscando", "procura"):
        return f"{name} está buscando {PROFILE['looking_for']}."
    if _has_any(text, "local", "mora", "cidade", "onde fica"):
        return f"{name} está em {PROFILE['location']}."
    if _has_any(text, "ajuda", "perguntas", "o que sabe", "o que posso perguntar"):
        return "Você pode perguntar sobre apresentação, tecnologias, idade, currículo, contato, GitHub, LinkedIn ou oportunidades."
    return FALLBACK
