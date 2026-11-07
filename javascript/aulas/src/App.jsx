import { useState } from "react"
import listaPerguntas from "./listaPerguntas"

function Pergunta(props){
  const [respostaDoUsuario, setRespostaDoUsuario] = useState(null)
  
  function responder(informacaoBotao){
    setRespostaDoUsuario(informacaoBotao)
    let novaRespostaDoUsuario = informacaoBotao
    if(novaRespostaDoUsuario == props.resposta){
      props.onResponder(true)
    }else{
      props.onResponder(false)
    }    
  }


  let resultado =""
  if(respostaDoUsuario){
    if(props.resposta == respostaDoUsuario){
      resultado = "Você Acertou!"

    } else {
      resultado = "Você errou!"
    }
  }
  
  return <div>
    <h3>{props.texto}</h3>
    <button disabled={respostaDoUsuario!==null} onClick={()=>responder("verdadeiro")}>Verdadeiro</button>
    <button disabled={respostaDoUsuario!==null} onClick={()=>responder("falso")}>Falso</button>
  {respostaDoUsuario?<span> {resultado} - Sua resposta foi {respostaDoUsuario}, e a resposta certa é {props.resposta}</span>:null} 
  </div>
}

export default function App(){
  const [acertos,setAcertos] = useState(0)

  function responder(acertou){
    if(acertou){
      setAcertos(acertos+1)
  }}

  return <div>
    <h1>Quiz</h1>
    <h3>Acertos: {acertos}</h3>
    <h3>Nota: {acertos/listaPerguntas.length*10}</h3>
  {listaPerguntas.map((elemento)=><Pergunta key={elemento.id} onResponder={responder} texto={elemento.pergunta} resposta={elemento.resposta?"verdadeiro":"falso"}/>)}
    </div>

}
