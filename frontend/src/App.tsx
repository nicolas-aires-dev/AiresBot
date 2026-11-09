import { useEffect, useRef, useState } from 'react'
import type { KeyboardEvent, SubmitEvent } from 'react'
import './App.css'

type Message = { id: number; role: 'bot' | 'user'; text: string }
type ApiResponse = { answer: string }

const suggestions = ['Quem é Nícolas?', 'Qual é a stack dele?', 'Como entrar em contato?']
const apiUrl = `${import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:8000'}/api/chat/`

function App() {
  const [messages, setMessages] = useState<Message[]>([
    { id: 1, role: 'bot', text: 'Oi! Eu sou o AiresBot, um chatbot feito para apresentar o Nícolas. O que você gostaria de saber?' },
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [apiError, setApiError] = useState(false)
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
        <a className="top-link" href="https://github.com/" target="_blank" rel="noreferrer">ver projeto <span aria-hidden="true">↗</span></a>
      </header>

      <section className="chat-layout" id="inicio">
        <aside className="intro-panel">
          <div className="eyebrow"><span className="eyebrow-line" /> PORTFÓLIO INTERATIVO</div>
          <h1>Uma conversa<br />sobre <span>mim.</span></h1>
          <p className="intro-copy">Conheça minha trajetória, minhas tecnologias e o que estou buscando. Pode perguntar direto ao ponto.</p>
          <div className="profile-card">
            <div className="avatar">N<span className="avatar-spark">✳</span></div>
            <div><div className="profile-name">Nícolas Santos</div><div className="profile-role">Desenvolvedor · Brasil</div></div>
            <span className="profile-arrow">↗</span>
          </div>
          <div className="topics-label">EXPERIMENTE PERGUNTAR</div>
          <div className="topic-list">
            <button onClick={() => void sendMessage('Quem é Nícolas?')}><span>01</span> Quem é Nícolas?</button>
            <button onClick={() => void sendMessage('Qual é a stack de tecnologias?')}><span>02</span> Qual é a stack?</button>
            <button onClick={() => void sendMessage('Onde encontro o currículo?')}><span>03</span> Ver currículo</button>
            <button onClick={() => void sendMessage('Como posso entrar em contato?')}><span>04</span> Como entrar em contato?</button>
          </div>
          <div className="aside-footer"><span>FEITO COM CURIOSIDADE</span><span>✳</span></div>
        </aside>

        <section className="chat-card" aria-label="Conversa com AiresBot">
          <div className="chat-header">
            <div className="bot-avatar"><span>✳</span></div>
            <div className="chat-title"><strong>AiresBot</strong><span><i /> online agora</span></div>
            <button className="more-button" aria-label="Mais opções">···</button>
          </div>
          <div className="chat-context"><span className="context-icon">✧</span><span>Sou um chatbot baseado em regras. Pergunte sobre o Nícolas!</span></div>
          <div className="messages" aria-live="polite">
            <div className="day-label"><span /> HOJE <span /></div>
            {messages.map((message) => (
              <div className={`message-row ${message.role}`} key={message.id}>
                {message.role === 'bot' && <div className="mini-avatar">✳</div>}
                <div className="message-content"><div className="bubble">{message.text}</div><span className="message-time">{message.role === 'bot' ? 'AiresBot' : 'Você'} · agora</span></div>
              </div>
            ))}
            {loading && <div className="message-row bot"><div className="mini-avatar">✳</div><div className="bubble typing"><i /><i /><i /></div></div>}
            {apiError && <div className="connection-note">A conexão com o backend falhou.</div>}
            <div ref={bottomRef} />
          </div>
          <div className="quick-questions"><span>PERGUNTAS RÁPIDAS</span><div>{suggestions.map((item) => <button key={item} onClick={() => void sendMessage(item)} disabled={loading}>{item}<span>↗</span></button>)}</div></div>
          <form className="composer" onSubmit={onSubmit}>
            <input aria-label="Sua mensagem" placeholder="Escreva sua pergunta..." value={input} onChange={(event) => setInput(event.target.value)} onKeyDown={onKeyDown} disabled={loading} />
            <button type="submit" aria-label="Enviar mensagem" disabled={loading || !input.trim()}><span>↑</span></button>
          </form>
          <div className="chat-footnote">AiresBot pode cometer erros. Confirme as informações importantes.</div>
        </section>
      </section>
      <footer className="page-footer"><span>© 2026 NÍCOLAS SANTOS</span><span>UM PROJETO DE PORTFÓLIO <b>✳</b></span><span>REACT <i>·</i> DJANGO REST FRAMEWORK</span></footer>
    </main>
  )
}

export default App
