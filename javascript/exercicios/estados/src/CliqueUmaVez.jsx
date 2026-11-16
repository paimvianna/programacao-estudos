/*
5.Crie um componente com um botão “Clique uma vez”. Ao 
clicar pela primeira vez, o texto do botão deve mudar 
para algo como “Botão bloqueado” e, a partir daí, novos 
cliques não devem causar mais nenhuma alteração.
*/
import { useState } from "react";
export default function BloqueioBotao() {
    const[respostaDoUsuario, setRespostaDoUsuario] = useState(null);
    function responder(){
        setRespostaDoUsuario(true)
    }

return <div>
    <button
    disabled = {respostaDoUsuario != null}
    onClick = {responder}> {respostaDoUsuario == null? "Clique uma vez." : "Botão Bloqueado."}
    </button>
</div>
}