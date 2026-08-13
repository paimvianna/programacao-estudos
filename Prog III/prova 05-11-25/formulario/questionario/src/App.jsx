import { useState } from 'react'
import Qestionario from './Questionario'
import listaPerguntas from './listaPerguntas'

function App() {
  return (
    <>
      <Qestionario listaPerguntas={listaPerguntas}/>
    </>
  )
}

export default App
