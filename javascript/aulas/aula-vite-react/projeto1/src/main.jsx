import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
//explicação da linha 6 createRoot e uma função que recebe document.getElementById('root') como parametro onde a gente vai renderizar o render que tem o bloco StrictMode
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
