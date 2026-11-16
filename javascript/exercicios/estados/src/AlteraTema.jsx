/*
2.Crie um componente que exibe uma área de conteúdo 
com um texto e um botão “Alternar tema”. Ao clicar, 
o componente deve alternar entre dois temas visuais 
(por exemplo: fundo claro com texto escuro e fundo 
escuro com texto claro), modificando o estilo dessa área.
*/
import { useState } from "react";

export default function AlterarTema(props){
    const[tema, setTema] = useState("claro")
    function temaEscolhido(){
        setTema(tema ==="claro" ? "escuro":"claro");
    }
    return(<div className={`caixa caixa-${tema}`}>
            <p>{props.texto}</p>
            <button onClick = {temaEscolhido}>Alterna tema</button>
         </div>

    )
}