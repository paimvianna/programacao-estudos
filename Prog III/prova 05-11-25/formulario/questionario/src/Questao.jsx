import { useState } from "react";

export default function Questao(props){
    const [resposta, setResposta] = useState(null);
    const [textoResposta, setTextoResposxta] = useState("");
 
    const responder=(respostaDoUsuario)=>{
        setResposta(respostaDoUsuario);

        if (respostaDoUsuario==props.resposta){
            setTextoResposxta("Correto!");
            props.onRespondeu(true);
            /*alert("Correto!");*/
        }else{
            setTextoResposxta("Incorreto!");
            props.onRespondeu(false);
            /*alert("Incorreto!");*/
        }
    }

    return <div>
        {props.pergunta} <br />
        
        <button disabled = {resposta!==null} onClick={()=>responder(true)}>Verdadeiro</button>
        <button disabled = {resposta!==null} onClick={()=>responder(false)}>Falso</button> <br />
        {textoResposta}
    </div>
}