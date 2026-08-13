import { useState } from "react";
import Questao from "./Questao";

export default function Qestionario(props){
    const [listaPerguntas,setlistaPerguntas] = useState(props.listaPerguntas)
    const respondeu=(id,acertou)=>{
        const novalistaPerguntas= listaPerguntas.map(pergunta=>{
            if(id== pergunta.id){
                //pergunta.acertou=acertou;
                const novoObjetoPergunta={...pergunta, acertou:acertou};
                return novoObjetoPergunta;
            }else{
                return pergunta;
            }
        });
        setlistaPerguntas(novalistaPerguntas);
    }
    /*console.log(listaPerguntas);*/
    const acertos= listaPerguntas.filter( (pergunta)=>pergunta.acertou===true);
    const erros= listaPerguntas.filter( (pergunta)=>pergunta.acertou===false);
    const naoRespondidos= listaPerguntas.filter( (pergunta)=>pergunta.acertou===undefined);
    /*controle
    console.log("acertos");
    console.log(acertos);
    console.log("erros");
    console.log(erros);
    console.log("naoRespondidos");
    console.log(naoRespondidos);*/
    return <>
        <h2>Questões</h2>
        <br/>
        {listaPerguntas.map(pergunta=> <>
            <Questao 
                pergunta={pergunta.pergunta}
                resposta={pergunta.resposta}
                onRespondeu={(acertou)=>respondeu(pergunta.id,acertou)}
                />
            <hr />
            </>)}
        <br />
        <h1>Resumo</h1>
        <label>Acertos: </label>{acertos.length}<br />
        <label>Erros: </label>{erros.length}<br />
        <label>Não Respondidas: </label>{naoRespondidos.length}<br />
    </>
}