"""Personal data used by the rule-based chatbot.

Replace the PROFILE values with verified information before publishing the project.
"""
import unicodedata

PROFILE = {
    "name": "Nícolas",
    "headline": "Desenvolvedor de software",
    "summary": "Nícolas é desenvolvedor de software com foco em Python desenvolvimento backend, APIs REST e automação de processos. Possui experiência na criação de soluções para problemas operacionais e integração de sistemas, buscando unir tecnologia e necessidades reais do negócio.",
    "age": 23,  # Example: 25
    "education": "aguardando os trâmites da faculdade para transferir o curso para Engenharia de Software, com previsão de formação para Jul 2028.",
    "stack": ["Python", "Django", "APIs REST", "Git", "Github", "Autenticação JWT", "Docker", "Celery", "Redis", "Linux", "Pytest", "AWS EC2", "SQL", "React", "TypeScript"],  # Example: ["Python", "Django REST Framework", "React", "TypeScript"]
    "resume_url": "https://1drv.ms/b/c/4111fe76ed94f350/IQBGuo4ZB35GRZxiDo_kidm0AQTPdA-ywJJDxYOD6kln7ls?e=m379v0",
    "experience": "Estudante de Análise e Desenvolvimento de Sistemas, em transição para Engenharia de Software, com experiência na identificação de oportunidades de melhoria e desenvolvimento de soluções tecnológicas para problemas operacionais. Atuação prática com Python, automação de processos, desenvolvimento backend, APIs REST e integração de sistemas. Experiência na iniciativa e implantação de automações departamentais, incluindo ferramentas de processamento de arquivos técnicos e soluções com Inteligência Artificial. Conhecimentos em bancos de dados relacionais, Git/Github, Docker e desenvolvimento de aplicações. Perfil investigativo, curioso e movido à resolução de problemas, com facilidade para aprender novas tecnologias e utilizar ferramentas assistidas por IA como apoio ao desenvolvimento e à produtividade.",
    "email": "ni_colasaires@hotmail.com",
    "github_url": "https://github.com/nicolas-aires-dev",
    "linkedin_url": "https://br.linkedin.com/in/nairesdev",
    "location": "Sorocaba - SP, disponível para vagas remotas em todo o Brasil, e Híbridas a depender do modelo.",
    "looking_for": "oportunidades que o permitam acelerar sua carreira em tecnologia, buscando projetos cada vez mais desafiantes, e evoluir enquanto contribui com soluções eficientes que impactem verdadeiramente o mercado e a vida dos clientes.",
    "projects": ["AiresBot: Projeto portfólio interativo via chatbot.",
                 "DxfReafer: Projeto de automação de processamento de projetos CAD.",
                 "UrlShortener: API de encurtador de link com processamento assincrono, testes e dockerização.",
                 "CarsSale: Sistema CRUD fullstack com integração à OpenAI e deploy via AWS EC2.",
                 "FlixAPI: API REST com autenticação JWT, organização de endpoints."],
    "DxfReader Resume" : "projeto de automação de processamento de arquivos CAD. ",
    "DxfReader Objective" : "diminuir tempo gasto em um processo sem valor agregado.",
    "DxfReader Technologies" : "Python, Ezdxf, Matplotlib, Pillow, Pyinstaller, Numpy",
    "DxfReader Results" : "considerando a produção por hora ( A cada 3600 segundos, 20 Perfis.), a produção de 20 perfis via Automação leva ~3 minutos (200 segundos). Dividindo 200/3600 e multiplicando por 100, resulta em 94,5% de ganho de performance. ",
    "DxfReader Code" : "https://github.com/nicolas-aires-dev/dxf_reader",

    "AiresBot Resume" : "Chatbot/Portfólio baseado em regras e palavras chave, utilizando lógica de identificação e intenções e respostas automáticas, que permite que o usuário conheça a trajetória de Nícolas de forma interativa.",
    "AiresBot Objective" : "criar um portfólio interativo que fugisse do convêncional feito por grande parte dos desenvolvedores; Estudo de desenvolvimento de Chatbots para um futuro projeto de automação de fluxo de informações interno.",
    "AiresBot Technologies" : "Python, TypeScript, Django, Django Rest Framework, API REST, React, Vite",
    "AiresBot Code" : "https://github.com/nicolas-aires-dev/AiresBot",

    "UrlShortener Resume" : "API REST de encutrtamento de links com BASE62.",
    "UrlShortener Objective" : "criar um projeto utilizado no dia a dia para estudar Dockerização de ambiente e Processamento Assíncrono com documentação de requisições via Postman.",
    "UrlShortener Technologies" : "Python, Django, Django Rest Framework, Celery, Redis, Sqlite, Postman",
    "UrlShortener Code" : "https://github.com/nicolas-aires-dev/url_shortener",

    "CarsSale Resume" : "Projeto CRUD Fullstack de cadastro de carros à venda.",
    "CarsSale Objective" : "Estudar integração com APIs externas (OpenAI), desenvolvimento Frontend e Deploy em com uWSGI+ Nginx em AWS EC2.",
    "CarsSale Technologies" : "Python, Django, Django Templates, OpenAI API, SQL Server, uWSGI/Nginx, Docker",
    "CarsSale Code" : "https://github.com/nicolas-aires-dev/CarsSale",

    "FlixAPI Resume" : "CRUD v1 para gerenciamento de filmes, generos e outras entidades relacionadas utilizando Django puro, e v2 com Django Rest Framework.",
    "FlixAPI Technologies" : "Python, Django, Django REST Framework, Sqlite",
    "FlixAPI Objective" : "estudar o ganho de performance no desenvolvimento com DRF e em relação ao desenvolvimento com Django puro.",
    "FlixAPI Code" : "https://github.com/nicolas-aires-dev/Flix_API",
}

FALLBACK = (
    "Ainda não tenho uma resposta cadastrada para essa pergunta. Você pode perguntar "
    f"sobre quem é {PROFILE["name"]}, sua stack, idade, experiência, currículo, projetos, contato, GitHub ou LinkedIn."
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

    #Contact
    if _has_any(text, "contato", "contatar", "email", "e-mail", "falar com", "telefone"):
        email = PROFILE["email"]
        return f"Você pode entrar em contato com {name} pelo e-mail {email}." if email else _value_or_pending(email, "Contato")
    
    #Github / Linkedin
    if "github" in text:
        url = PROFILE["github_url"]
        return f"O GitHub de {name} está em {url}." if url else _value_or_pending(url, "GitHub")
    if "linkedin" in text or "linked in" in text:
        url = PROFILE["linkedin_url"]
        return f"O LinkedIn de {name} está em {url}." if url else _value_or_pending(url, "LinkedIn")

    #Curriculum
    if _has_any(text, "currículo", "curriculo", "cv", "resume"):
        url = PROFILE["resume_url"]
        return f"Você pode acessar o currículo de {name} aqui: {url}" if url else _value_or_pending(url, "Link do currículo")

    #Stack
    if _has_any(text, "stack", "tecnologias", "tecnologia", "linguagens", "framework", "ferramentas"):
        stack = PROFILE["stack"]
        return f"A stack de {name} inclui: {', '.join(stack)}." if stack else _value_or_pending(stack, "Stack")

    #Projects
    if _has_any(text, "projetos", "projeto", "projetos de", "projetos do"):
        projects = "\n".join(
            f"•{project}" for project in PROFILE["projects"]
        )
        return f"Os principais projetos de {name} são: \n\n{projects} \n Todos disponíveis em: https://github.com/nicolas-aires-dev \n\n Caso deseje, poderá perguntar pelo nome dos projetos, e ter mais detalhes sobre cada um.\n\nEx: 'Me fale sobre o DxfReader'"

    #DxfReader
    if _has_any(text, "DxfReader", "projeto CAD", "projeto DXF", "projeto com maior ganho"):
        return f"O projeto DxfReader é um {PROFILE["DxfReader Resume"]} \n\n Com o objetivo de {PROFILE["DxfReader Objective"]} \n\n Utilizando as tecnologias: {PROFILE["DxfReader Technologies"]} \n\n Resultando em, {PROFILE["DxfReader Results"]} \n\n Link do repositório: {PROFILE["DxfReader Code"]} "

    #AiresBot
    if _has_any(text, "AiresBot", "projeto chatbot", "projeto bot", "projeto conversacional"):
        return f"O projeto Airesbot é um {PROFILE["AiresBot Resume"]} \n\n Com o objetivo de {PROFILE["AiresBot Objective"]} \n\n Utilizando as tecnologias: {PROFILE["AiresBot Technologies"]} \n\n Link do repositório: {PROFILE["AiresBot Code"]}" 

    #UrlShortener
    if _has_any(text, "UrlShortener", "projeto encurtador", "projeto encurtador de links", "encurtador de links"):
        return f"O projeto UrlShortener é uma {PROFILE["UrlShortener Resume"]} \n\n Com o objetivo de {PROFILE["UrlShortener Objective"]} \n\n Utilizando as tenologias: {PROFILE["UrlShortener Technologies"]} \n\n Link do repositório: {PROFILE['UrlShortener Code']}"

    #CarsSale
    if _has_any(text, "CarsSale", "projeto de carros", "projeto de venda de carros"):
        return f"O projeto UrlShortener é uma {PROFILE["UrlShortener Resume"]} \n\n Com o objetivo de {PROFILE["UrlShortener Objective"]} \n\n Utilizando as tenologias: {PROFILE["UrlShortener Technologies"]} \n\n Link do repositório: {PROFILE['UrlShortener Code']}"
    #FlixAPI
    if _has_any(text, "FlixAPI", "projeto netflix", "projeto de filmes", "projeto filmes"):
        return f"O projeto FlixAPI é um {PROFILE["FlixAPI Resume"]} \n\n Com o objetivo de {PROFILE["FlixAPI Objective"]} \n\n Usando as tecnologias: {PROFILE["FlixAPI Technologies"]} \n\n Link do repositório: {PROFILE["FlixAPI Code"]}"

    #Who's
    if _has_any(text, "quem é", "quem e", "sobre", "apresenta"):
        return PROFILE["summary"]

    #Experience
    if _has_any(text, "Experiência", "profissional", "experiência profissional"):
        return PROFILE["experience"]

    #Education
    if _has_any(text, "formação", "formacao", "faculdade", "graduação", "graduacao", "formatura"):
        return f"{name} está {PROFILE['education']}"

    #Greetings
    if _has_any(text, "oi", "olá", "ola", "bom dia", "boa tarde", "boa noite") and len(text.split()) <= 3:
        return f"Oi! Sou o AiresBot. Posso contar um pouco sobre {name} e seus projetos."
    
    #Searching for
    if _has_any(text, "vaga", "oportunidade", "trabalho", "buscando", "procura"):
        return f"{name} está buscando {PROFILE['looking_for']}."
    
    #Years old
    if _has_any(text, "idade", "quantos anos", "anos tem"):
        age = PROFILE["age"]
        return f"{name} tem {age} anos." if age else _value_or_pending(age, "Idade")

    #Where you live
    if _has_any(text, "local", "mora", "cidade", "onde fica"):
        return f"{name} está em {PROFILE['location']}."

    #Help
    if _has_any(text, "ajuda", "perguntas", "o que sabe", "o que posso perguntar"):
        return "Você pode perguntar sobre apresentação, tecnologias, idade, currículo, contato, GitHub, LinkedIn ou oportunidades."
    
    return FALLBACK
