/*
1.Crie um componente com um botão “Mostrar/Esconder”. 
Ao clicar, o componente deve alternar entre exibir e 
não exibir uma mensagem de texto na tela.
*/
import { useState } from "react";

export default function Mostra_Esconder(){
    const[visivel,setVisivel] = useState(false);
    return(<div>
            <button onClick = {()=>setVisivel(!visivel)}>
                {visivel ? "Esconder" : "Mostrar"}
            </button>

            {visivel && <p> O botão mostrar foi acionado.</p>}
        </div>
    );
}