import{useState} from "react";

export default function Questao(props){
    /*o componente a baixa vai ser um hulk ou gancho que vai armazenar que e o useState, sendo dois elementos principais.*/
    const [resposta, setResposta] = useState(null);
    const [textoResposta, setTextoResposta] = useState(""); 

    const responder=(respostaUsuario)=>{
        setResposta(respostaUsuario);
        if(respostaUsuario==props.resposta){
            setTextoResposta("Correto!");
            props.onRespondeu(true);
        }else{
            setTextoResposta("Incorreto!");
            props.onRespondeu(false);
        }
    }
    return <div>
        {props.pergunta} <br />
        <button disabled={resposta!==null} onClick={()=>responder(true)}>Verdadeiro</button>
        <button disabled={resposta!==null} onClick={()=>responder(false)}>Falso</button> <br />
        {textoResposta}
    </div>
}