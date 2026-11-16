import { useState } from "react"

export default function Questao(props) {
    const [resposta, setResposta] = useState(null);
    const [textoReposta, setTextoResposta] = useState("");
    const responder=(resp)=>{
        setResposta(resp);
        if(resp===props.resposta)
            setTextoResposta("Correto!");
        else 
            setTextoResposta("Incorreto!");
        props.onRespondeu(resp===props.resposta);

    }
    return <div>
        <label>{props.pergunta}</label><br/>
        <br/>
        <button disabled={resposta!==null} onClick={()=>responder(true)} >Verdadeiro</button>
        <button disabled={resposta!==null} onClick={()=>responder(false)}>Falso</button> 
        <br/>
        {textoReposta}
        <br/>
        <hr/>
    </div>
} 