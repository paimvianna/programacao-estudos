import { useState } from "react"
import Questao from "./Questao"
export default function Questionario(props){
    const listaPerguntas=props.listaPerguntas;
    const [acertos, setAcertos]=useState(0);
    const [erros, setErros]=useState(0);
    const nota = acertos/(acertos+erros)*10;
    const notaString=new Intl.NumberFormat(
        "pt-BR",{style:"decimal", maximaFractionDigits:2}).format(nota);//e um derivado de nota que vem a ser um derivado de erros e acertos que são estados.
    
    function respondeu(acertou){
        let novoEstadoDoAcertos=acertos;
        let novoEstadoDoErros=erros;

        acertou?novoEstadoDoAcertos=novoEstadoDoAcertos+1:novoEstadoDoErros++;

        setAcertos(novoEstadoDoAcertos);
        setErros(novoEstadoDoErros);
    }
    return(
        <div>Total de Acertos:
        <span className="acertou">{acertos}</span>
        /
        <span className="errou">{erros}</span>
        /
        <span>{acertos+erros}</span>
        <br />
        {listaPerguntas.map((objetoPergunta)=> <Questao
            key={objetoPergunta.id}
            pergunta={objetoPergunta.pergunta}
            resposta={objetoPergunta.resposta?"sim":"não"}
            onRespondeu={respondeu}
            />)
        } <br />
        {((acertos+erros)>=listaPerguntas.length) && <span>Nota: {notaString}</span>}
        </div>
    )
    
}