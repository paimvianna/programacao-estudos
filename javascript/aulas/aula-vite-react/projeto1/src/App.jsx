import { useState } from 'react'// o componente no react e uma função que retorna sua representação grafica o que e sua representação grafica, e uma compossição em html e outros componentes
import heroImg from './assets/hero.png'// a pagina que abre e um componente do react
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <h1>Ola Mundo!</h1>
    <button>Teste</button>
    
    </>
  )
}

export default App
