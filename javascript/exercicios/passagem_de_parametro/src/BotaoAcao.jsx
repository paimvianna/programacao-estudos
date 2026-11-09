/*
7. Componente BotaoAcao

Crie um componente chamado BotaoAcao que receba:

    texto: texto apresentado dentro do botão.
    desabilitado: valor booleano que indica se o botão está desabilitado.

Quando desabilitado for true, o botão deverá possuir o atributo disabled. Quando for false, o botão deverá permanecer habilitado.
Exemplo de chamada

<BotaoAcao texto="Salvar" desabilitado={false} />
<BotaoAcao texto="Excluir" desabilitado={true} />

Exemplo de resultado esperado
Salvar Excluir
*/
import { useState } from "react";

export default function BotaoAcao(props){
    return <>
        <button disabled={props.desabilitado}>{props.texto}</button>
    </>
}