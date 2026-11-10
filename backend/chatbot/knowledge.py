"""Personal data used by the rule-based chatbot.

Replace the PROFILE values with verified information before publishing the project.
"""
import unicodedata

PROFILE = {
    "name": "Nícolas Aires",
    "headline": "Desenvolvedor de software",
    "summary": "Nícolas é desenvolvedor de software com foco em Python desenvolvimento backend, APIs REST e automação de processos. Possui experiência na criação de soluções para problemas operacionais e integração de sistemas, buscando unir tecnologia e necessidades reais do negócio.",
    "age": 23,  # Example: 25
    "education": "Cursando Engenharia de Software, com previsão de formação para Jul 2028.",
    "stack": ["Python", "Django", "APIs REST", "Git", "Github", "Autenticação JWT", "Docker", "Celery", "Redis", "Linux", "Pytest", "AWS EC2", "SQL", "React", "TypeScript"],  # Example: ["Python", "Django REST Framework", "React", "TypeScript"]
    "resume_url": "https://1drv.ms/b/c/4111fe76ed94f350/IQDSNgn7u9mZQKF1MR_27OlLAd68KRelRzUlMet_QsOXJnU?e=2V5tow",
    "experience": "Estudante de Análise e Desenvolvimento de Sistemas, em transição para Engenharia de Software, com experiência na identificação de oportunidades de melhoria e desenvolvimento de soluções tecnológicas para problemas operacionais. Atuação prática com Python, automação de processos, desenvolvimento backend, APIs REST e integração de sistemas. Experiência na iniciativa e implantação de automações departamentais, incluindo ferramentas de processamento de arquivos técnicos e soluções com Inteligência Artificial. Conhecimentos em bancos de dados relacionais, Git/Github, Docker e desenvolvimento de aplicações. Perfil investigativo, curioso e movido à resolução de problemas, com facilidade para aprender novas tecnologias e utilizar ferramentas assistidas por IA como apoio ao desenvolvimento e à produtividade.",
    "email": "ni_colasaires@hotmail.com",
    "github_url": "https://github.com/nicolas-aires-dev",
    "linkedin_url": "https://br.linkedin.com/in/nairesdev",
    "location": "Sorocaba - SP, disponível para vagas remotas em todo o Brasil, e Híbridas a depender do modelo.",
    "looking_for": "Oportunidades que me permitam focar exclusivaente em tecnologia!",
    "projects": ["AiresBot: Projeto portfólio interativo via chatbot.",
                 "DxfReafer: Projeto de automação de processamento de projetos CAD.",
                 "UrlShortener: API de encurtador de link com processamento assincrono, testes e dockerização.",
                 "CarsSale: Sistema CRUD fullstack com integração à OpenAI e deploy via AWS EC2.",
                 "FlixAPI: API REST com autenticação JWT, organização de endpoints."]
}

FALLBACK = (
    "Ainda não tenho uma resposta cadastrada para essa pergunta. Você pode perguntar "
    "sobre quem é o Nícolas, sua stack, idade, currículo, contato, GitHub ou LinkedIn."
)

def normalize(text):
    text = unicodedata.normalize("NFD", text)
    return "".join(
        char for char in text
        if unicodedata.category(char) != "Mn"
    ).lower()

def _has_any(text, *keywords):
    normalized_text = normalize(text)

    return any(
        normalize(keyword) in normalized_text
        for keyword in keywords
    )

def _value_or_pending(value, label: str) -> str:
    if not value:
        return f"Essa informação ainda não foi adicionada ao perfil do Nícolas."
    return f"{label}: {value}"


def answer_question(message: str) -> str:
    """Match common Portuguese questions to a small set of profile intents."""
    text = " ".join(message.casefold().replace("?", " ").replace("!", " ").split())
    name = PROFILE["name"]

    if _has_any(text, "contato", "contatar", "email", "e-mail", "falar com", "telefone"):
        email = PROFILE["email"]
        return f"Você pode entrar em contato com {name} pelo e-mail {email}." if email else _value_or_pending(email, "Contato")
    if "github" in text:
        url = PROFILE["github_url"]
        return f"O GitHub de {name} está em {url}." if url else _value_or_pending(url, "GitHub")
    if "linkedin" in text or "linked in" in text:
        url = PROFILE["linkedin_url"]
        return f"O LinkedIn de {name} está em {url}." if url else _value_or_pending(url, "LinkedIn")
    if _has_any(text, "currículo", "curriculo", "cv", "resume", "formação", "formacao"):
        url = PROFILE["resume_url"]
        return f"Você pode acessar o currículo de {name} aqui: {url}" if url else _value_or_pending(url, "Link do currículo")
    if _has_any(text, "stack", "tecnologias", "tecnologia", "linguagens", "framework", "ferramentas"):
        stack = PROFILE["stack"]
        return f"A stack de {name} inclui: {', '.join(stack)}." if stack else _value_or_pending(stack, "Stack")
    if _has_any(text, "projetos", "projeto", "projetos de", "projetos do"):
        projects = "\n".join(
            f"•{project}" for project in PROFILE["projects"]
        )
        return f"Os principais projetos de {name} são: \n\n{projects}"
    if _has_any(text, "quem é", "quem e", "sobre", "apresenta"):
        return PROFILE["summary"]
    if _has_any(text, "Experiência", "profissional", "experiência profissional"):
        return PROFILE["experience"]
    if _has_any(text, "formação", "formacao", "faculdade", "graduação", "graduacao", "formatura"):
        return f"{name} está {PROFILE['education']}"
    if _has_any(text, "oi", "olá", "ola", "bom dia", "boa tarde", "boa noite") and len(text.split()) <= 3:
        return f"Oi! Sou o AiresBot. Posso contar um pouco sobre {name} e seus projetos."
    if _has_any(text, "vaga", "oportunidade", "trabalho", "buscando", "procura"):
        return f"{name} está buscando {PROFILE['looking_for']}."
    if _has_any(text, "idade", "quantos anos", "anos tem"):
        age = PROFILE["age"]
        return f"{name} tem {age} anos." if age else _value_or_pending(age, "Idade")
    if _has_any(text, "local", "mora", "cidade", "onde fica"):
        return f"{name} está em {PROFILE['location']}."
    if _has_any(text, "ajuda", "perguntas", "o que sabe", "o que posso perguntar"):
        return "Você pode perguntar sobre apresentação, tecnologias, idade, currículo, contato, GitHub, LinkedIn ou oportunidades."
    return FALLBACK
