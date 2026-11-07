import { useState } from 'react';
import listaPerguntas from './listaPerguntas.js'
import sim_img from './assets/sim.png'
import nao_img from './assets/nao.png'
import acertou_img from './assets/acertou.png'
import errou_img from './assets/errou.png'
//props e o objeto que tem todos os atributos e propriedades do componente/ objeto


function Pergunta(props){
  const [respostaDoUsuario, setRespostaDoUsuario] = useState(null);
  function responder(informacaoBotao){
    let novaRespostaDoUsuario = informacaoBotao;
    if(novaRespostaDoUsuario == props.resposta){
      props.onResponder(true);
    }else{
      props.onResponder(false);
    }
    setRespostaDoUsuario(novaRespostaDoUsuario);
  }
  let resultdo = "";
  if (respostaDoUsuario){
    if(props.resposta == respostaDoUsuario){
      resultdo = acertou_img
    }else{
      resultdo = errou_img
    }
  }
  return <div>
    
    <h3>{props.texto}</h3>
    {/*usando arrow function */}
    <button
    disabled = {respostaDoUsuario != null}
    onClick = {()=> responder("verdadeiro")}>
      <img src = {sim_img}/>
    </button>
    {/*<button onClick = {function(){
          //exemplo com função anonimo
          responder('falso');
    }}>Falso</button>*/}
    <button 
    disabled = {respostaDoUsuario != null}
    onClick = {()=> responder("falso")}>
      <img src = {nao_img}/>
    </button>
    {
      respostaDoUsuario?
      <span>
        <img src = {props.resposta == respostaDoUsuario? acertou_img:errou_img}/> - Você respondeu: {respostaDoUsuario}, a resposta certa é {props.resposta}
      </span>
      :""
    }
  </div>
}

export default function App() {
  const [acertos, setAcertos] = useState(0);
  const [total, setTotal] = useState(0);

  function responder(acertou){
    //alert(acertou)
    setTotal(total+1);
    if (acertou){
      setAcertos(acertos+1);
    }
  }

  const nota = acertos/listaPerguntas.length*10;

  return <div>
    <h1>Quiz</h1>
    {total == listaPerguntas.length?
    <h3>Acertos: {acertos} Nota: {nota} {nota >= 7?"Parabéns":"Boa sorte da próxima vez!"}</h3>
    :
    listaPerguntas.map(function(elemento){
      return <Pergunta
        key = { elemento.id}
        texto = {elemento.pergunta}
        resposta = {elemento.resposta?"verdadeiro":"falso"}
        onResponder = {responder}
        />
    })}
  </div>;
}

