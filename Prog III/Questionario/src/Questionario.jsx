import { useState } from "react";
import Questao from "./Questao";

export default function Questionario(props){
    const [listaPerguntas, setListaPerguntas] = useState(props.listaPerguntas);
    const respondeu = (id, acertou)=>{
        const novaListaPerguntas =listaPerguntas.map(pergunta=>{
            if(id==pergunta.id){
                const novoObjetoPergunta= {...pergunta,acertou:acertou};//se eu por pergunta.acertou = acertou, não estarei mudando o objeto que no fim fica não sendo uma boa pratica no react poor isso a construção de um novo objeto com espraiamento.

                return novoObjetoPergunta;
            }else{
                return pergunta;
            }
        });
        setListaPerguntas(novaListaPerguntas);
    }
    //console.log(listaPerguntas);
    const acertos= listaPerguntas.filter((pergunta)=>pergunta.acertou === true);
    const erros= listaPerguntas.filter((pergunta)=>pergunta.acertou === false);
    const naoRespondidos = listaPerguntas.filter((pergunta)=>pergunta.acertou===undefined);
    console.log("acertos");
    console.log(acertos);
    console.log("erros");
    console.log(erros);
    console.log("naoRespondidos");
    console.log(naoRespondidos);
    //const respostas=naoRespondidos.length
    return<>
    <h2>Questões</h2>
    <br />
    {listaPerguntas.map(pergunta=> <>
        {/*abaixo estou implementando os eventos que ocorreram no componente filho*/}
        <Questao 
            pergunta={pergunta.pergunta} 
            resposta={pergunta.resposta}
            onRespondeu={(acertou)=>respondeu(pergunta.id,acertou)}            
            />
    <hr />
    </>)}

    {/*
    <Questao pergunta="1+2=3" resposta={true}/><br />
    <Questao pergunta="8+2=3" resposta={false}/>
    acima esta o processo ondeusaria manualmente para cada pergunta.
    */}
    <br />
    <h1>Resumo</h1>
    <label>Acertos: </label> {acertos.length} <br />
    <label>Erros: </label> {erros.length} <br />
    <label>Não Respondidas: </label> {naoRespondidos.length} <br />
    </>
}