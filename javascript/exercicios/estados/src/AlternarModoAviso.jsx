/*
9.Crie um componente que exibe uma mensagem de aviso e um botão
 “Alternar modo de aviso”. Em um modo, o aviso deve aparecer 
 como um parágrafo simples. No outro modo, o mesmo texto deve 
 aparecer como um título (por exemplo, em um elemento <h2>) 
 com estilo mais chamativo. O componente deve alternar entre 
 essas duas formas de exibição ao clicar.
*/
import { useState } from "react";

export default function ModoAlerta(props){
    const texto = props.texto
    const[alerta, setAlerta] = useState(false)

    function acionaAlerta(){
        setAlerta(!alerta)
    }
    return(<div>
        {alerta == false? <p>{texto}</p> : <h2 style={{color:"red", background:"yellow"}}>{texto}</h2>}
        <button onClick={acionaAlerta}>Alternar modo de aviso</button>
        </div>
    )
}