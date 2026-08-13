import { useState } from 'react'
import Questionario from './Questionario'
import listaPerguntas from "./listaPerguntas"
function App() {

  return (
    <>
    <Questionario listaPerguntas = {listaPerguntas}/>{/*o que eu vou por aqui como componente vai ser importado de Questionario.jsx. E consecutivamente o mesmo importa de Questao.jsx o comportamento, sendo que a lista de perguntas vai ser passadocomo parametro para questionario que e o pai desta interação. depois de um tempo vi eque escrevi que listaPerguntas estava errado no caso estava listaPertguntas*/}
    Teste{/*Aqui e somente um teste acima vou colocar como um componente*/}
    </>
  )
}

export default App
