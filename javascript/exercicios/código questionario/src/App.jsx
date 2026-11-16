import { useState } from 'react'
import './App.css'
import Questionairo from './Questionario'
import listaPerguntas from './listaPerguntas'

function App() {
  return (
    <>
     <Questionairo listaPerguntas={listaPerguntas} />
    </>
  )
}

export default App
