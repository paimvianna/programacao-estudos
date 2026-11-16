/*
10.Crie um componente que mostre diferentes tipos de alerta na 
tela (sucesso, erro, aviso), controlados por três botões: “Sucesso”,
“Erro” e “Aviso”. Ao clicar em cada botão, deve aparecer uma caixa 
de alerta com o texto correspondente e um estilo visual diferente 
para cada tipo (por exemplo, fundo verde, vermelho ou amarelo). 
Inicialmente, não deve haver alerta visível.
*/
import { useState } from "react";

export default function SistemaAlerta(props){
    const textosucesso = props.textosucesso
    const textoerro = props.textoerro
    const textoaviso = props.textoaviso
    const[estado, setEstado] = useState(null)

    function acionaAlerta(parametro){
        if(estado != parametro){
            setEstado(parametro)
        }else if (estado == parametro){
            setEstado(null)
        }
    }/*metodo que eu fiz com aninhamento profundo.
    return(<div>
        {estado == "erro" ? <h2 style={{color:"white", background:"red"}}>{textoerro}</h2> : 
            (estado == "sucesso" ? <h2 style = {{color:"black", background:"green"}}>{textosucesso}</h2> :
                (estado == "aviso" && <h2 style={{color:"black", background:"yellow"}}>{textoaviso}</h2>))}
        <button onClick={()=> acionaAlerta("sucesso")}>Sucesso</button>
        <button onClick={()=> acionaAlerta("erro")}>Erro</button>
        <button onClick={()=> acionaAlerta("aviso")}>Aviso</button>
        </div>
    )*/
   // Fica ANTES do return do componente o dicionario chave e vlor:
    const alertas = {
        sucesso: { texto: props.textosucesso, color: "white", background: "green" },
        erro:    { texto: props.textoerro,    color: "white", background: "red" },
        aviso:   { texto: props.textoaviso,   color: "black", background: "yellow" }
    }

    const alertaAtual = alertas[estado] // Se estado for null, alertaAtual vira undefined

    // Agora o return do componente fica limpo e sem ternários encadeados:
    return(
        <div>
            {alertaAtual && (
                <h2 style={{ color: alertaAtual.color, background: alertaAtual.background }}>
                    {alertaAtual.texto}
                </h2>
            )}

            <button onClick={() => acionaAlerta("sucesso")}>Sucesso</button>
            <button onClick={() => acionaAlerta("erro")}>Erro</button>
            <button onClick={() => acionaAlerta("aviso")}>Aviso</button>
        </div>
    )
}
