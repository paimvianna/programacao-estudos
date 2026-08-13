import {useState} from "react";


export default function itemAvaliado(props){
    const item = props.objetoItem;
    const[resposta,setResposta]=useState(null);
    const[ruim, setRuim]=useState(0);
    const[neutro, setNeutro]=useState(0);
    const[bom, setBom]=useState(0);
    
    
    return(
        <>
        <h1>nao sei se vai.</h1>
        {item.pergunta}
        </>
    )
}