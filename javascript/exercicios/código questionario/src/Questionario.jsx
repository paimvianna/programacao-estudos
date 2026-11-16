import { useState } from 'react';
import Questao from './Questao';
export default function Questionairo(props) { 
    const [listaPerguntas, setListaPerguntas]= useState(props.listaPerguntas);
    const respondeu=(id,acertou)=>{
        setListaPerguntas(listaPerguntas.map( 
            pergunta=>pergunta.id==id?{...pergunta, acertou:acertou}:pergunta
        ));        
    }
    const acertos= listaPerguntas.filter((pergunta)=>pergunta.acertou===true);
    const erros= listaPerguntas.filter((pergunta)=>pergunta.acertou===false);
    const naoRespondidas= listaPerguntas.filter((pergunta)=>pergunta.acertou===undefined);
    return <div>
        <h1>Questões</h1>  
        
        {listaPerguntas.map( perguntaDaLista =>
            <Questao 
                pergunta={perguntaDaLista.pergunta} 
                resposta={perguntaDaLista.resposta} 
                onRespondeu={(acertou)=>respondeu(perguntaDaLista.id,acertou)}
                /> )}
        <h1>Resumo</h1>  
        <label>Acertos: </label>{acertos.length}<br/>
        <label>Erros: </label>{erros.length}<br/>
        <label>Não respondidas: </label>{naoRespondidas.length}<br/>
    </div>

}