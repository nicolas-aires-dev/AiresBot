import { useEffect, useRef, useState } from 'react'
import type { KeyboardEvent, SubmitEvent } from 'react'
import heroImg from '../assets/images/hero.png'
import './App.css'

type Message = { id: number; role: 'bot' | 'user'; text: string }
type ApiResponse = { answer: string }

function linkify(text: string) {
  const urlPattern = /https?:\/\/[^\s<]+/g
  const parts = []
  let lastIndex = 0

  for (const match of text.matchAll(urlPattern)) {
    const rawUrl = match[0]
    const url = rawUrl.replace(/[),.!?;:]+$/, '')
    if (!url) continue
    const start = match.index ?? 0
    parts.push(text.slice(lastIndex, start))
    parts.push(
      <a key={start} href={url} target="_blank" rel="noreferrer">
        {url}
      </a>,
    )
    parts.push(rawUrl.slice(url.length))
    lastIndex = start + rawUrl.length
  }

  parts.push(text.slice(lastIndex))
  return parts
}

const suggestions = ['Quem é o Nícolas?', 'Qual é a stack dele?', 'Qual é a idade dele?', 'Onde encontro o currículo?', 'Quais são os projetos dele?', 'Como entro em contato?']
const apiUrl = `${import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:8000'}/api/chat/`

function App() {
  const [messages, setMessages] = useState<Message[]>([
    { id: 1, role: 'bot', text: 'Oi! Eu sou o AiresBot, um chatbot feito para apresentar o Nícolas. O que você gostaria de saber?' },
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [apiError, setApiError] = useState(false)
  const [helpOpen, setHelpOpen] = useState(false)
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, loading])

  async function sendMessage(value = input) {
    const question = value.trim()
    if (!question || loading) return
    setMessages((current) => [...current, { id: Date.now(), role: 'user', text: question }])
    setInput('')
    setLoading(true)
    setApiError(false)
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: question }),
      })
      if (!response.ok) throw new Error('API indisponível')
      const data = (await response.json()) as ApiResponse
      const typingDelay = Math.min(2200, Math.max(700, data.answer.length * 18))
      await new Promise<void>((resolve) => window.setTimeout(resolve, typingDelay))
      setMessages((current) => [...current, { id: Date.now() + 1, role: 'bot', text: data.answer }])
    } catch {
      setApiError(true)
      setMessages((current) => [...current, { id: Date.now() + 1, role: 'bot', text: 'Não consegui falar com o servidor agora. Confira se o backend Django está rodando e tente de novo.' }])
    } finally {
      setLoading(false)
    }
  }

  function onSubmit(event: SubmitEvent<HTMLFormElement>) {
    event.preventDefault()
    void sendMessage()
  }

  function onKeyDown(event: KeyboardEvent<HTMLInputElement>) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault()
      void sendMessage()
    }
  }

  return (
    <main className="page-shell">
      <header className="topbar">
        <a className="brand" href="#inicio" aria-label="AiresBot, início"><span className="brand-mark">a.</span><span>aires<span className="brand-light">bot</span></span></a>
        <div className="topbar-note"><span className="status-dot" /> chatbot pessoal <span className="topbar-divider">·</span> v1.0</div>
        <a className="top-link" href="https://github.com/nicolas-aires-dev/airesbot" target="_blank" rel="noreferrer">Ver Projeto<span aria-hidden="true">↗</span></a>
      </header>

      <section className="chat-layout" id="inicio">
        <aside className="intro-panel">
          <div className="eyebrow"><span className="eyebrow-line" /> PORTFÓLIO INTERATIVO</div><div className="hero-portrait"><img src={heroImg} alt="Nícolas em uma ilustração com referências a tecnologia e desenvolvimento" /></div>
          <h1>Uma conversa<br />sobre <span>mim.</span></h1>
          <p className="intro-copy">Conheça minha trajetória, minhas tecnologias e o que estou buscando. Pode perguntar direto ao ponto.</p>
        </aside>

        <section className="chat-card" aria-label="Conversa com AiresBot">
          <div className="chat-header">
            <div className="bot-avatar"><span>α</span></div>
            <div className="chat-title"><strong>AiresBot</strong><span><i /> online agora</span></div>
            <button className="more-button" aria-label="Mais opções">···</button>
          </div>
          <div className="chat-context"><span className="context-icon">✧</span><span>Sou um chatbot baseado em regras. Pergunte sobre o Nícolas!</span></div>
          <div className="messages" aria-live="polite">
            <div className="day-label"><span /> HOJE <span /></div>
            {messages.map((message) => (
              <div className={`message-row ${message.role}`} key={message.id}>
                {message.role === 'bot' && <div className="mini-avatar">α</div>}
                <div className="message-content"><div className="bubble">{message.role === 'bot' ? linkify(message.text) : message.text}</div><span className="message-time">{message.role === 'bot' ? 'AiresBot' : 'Você'} · agora</span></div>
              </div>
            ))}
            {loading && <div className="message-row bot"><div className="mini-avatar">α</div><div className="bubble typing" role="status" aria-label="AiresBot está digitando"><i /><i /><i /></div></div>}
            {apiError && <div className="connection-note">A conexão com o backend falhou.</div>}
            <div ref={bottomRef} />
          </div>
          <div className="suggestion-launcher"><span>PRECISA DE UMA IDEIA?</span><button className="help-button" type="button" aria-label="Abrir perguntas sugeridas" onClick={() => setHelpOpen(true)}>?</button></div>
          <form className="composer" onSubmit={onSubmit}>
            <input aria-label="Sua mensagem" placeholder="Escreva sua pergunta..." value={input} onChange={(event) => setInput(event.target.value)} onKeyDown={onKeyDown} disabled={loading} />
            <button type="submit" aria-label="Enviar mensagem" disabled={loading || !input.trim()}><span>↑</span></button>
          </form>
          <div className="chat-footnote">AiresBot pode cometer erros. Confirme as informações importantes.</div>
        </section>
      </section>
      {helpOpen && (
        <div className="modal-backdrop" onClick={() => setHelpOpen(false)}>
          <section className="suggestions-modal" role="dialog" aria-modal="true" aria-labelledby="suggestions-title" onClick={(event) => event.stopPropagation()}>
            <button className="modal-close" type="button" aria-label="Fechar perguntas" onClick={() => setHelpOpen(false)}>×</button>
            <span className="modal-kicker">AIRESBOT · SUGESTÕES</span>
            <h2 id="suggestions-title">O que você quer saber?</h2>
            <p>Escolha uma pergunta para começar a conversa.</p>
            <div className="suggestion-list">
              {suggestions.map((question) => (
                <button key={question} type="button" onClick={() => { setHelpOpen(false); void sendMessage(question) }}>
                  {question}<span aria-hidden="true">↗</span>
                </button>
              ))}
            </div>
          </section>
        </div>
      )}
      <footer className="page-footer"><span>© 2026 NÍCOLAS AIRES</span><span>UM PROJETO DE PORTFÓLIO <b>α</b></span><span>REACT <i>·</i> DJANGO REST FRAMEWORK</span></footer>
    </main>
  )
}

export default App
