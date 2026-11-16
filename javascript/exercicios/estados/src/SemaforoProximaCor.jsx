/*
4.Crie um componente que mostra na tela o estado de um 
semáforo (vermelho, amarelo ou verde) e um botão “Próxima cor”. 
Cada clique deve avançar para a próxima cor em uma sequência 
cíclica, e o texto exibido deve mudar de cor de acordo 
com o estado (vermelho, amarelo ou verde).
*/
import { useState } from "react";
export default function ProximaCor(props){
    const[cor, setCor] = useState(0);
    function mudancaCor(){
        if(cor == 3){
            setCor(1)      
        }else{
            setCor(cor +1)
        }

        //setCor(0)
    }
    return(<div>
        {/*da form que esta se dando aqui, os textos ficam visivel mesmo sem acionamento
        conversando com o gemini me aconselhou a por indisponivel o que nao esta acionado.
        {cor == 1 ? <p style= {{color:"red", fontWeight: "bold"}}>VERMELHO</p> : <p>VERMELHO</p> }
        {cor == 2 ? <p style= {{color:"gold", fontWeight: "bold"}}>AMARELO</p> : <p>AMARELO</p> }
        {cor == 3 ? <p style= {{color:"green", fontWeight: "bold"}}>VERDE</p> : <p>VERDE</p> }
        */}
        {cor == 1 && <p style= {{color:"red", fontWeight: "bold"}}>VERMELHO</p>}
        {cor == 2 && <p style= {{color:"gold", fontWeight: "bold"}}>AMARELO</p>}
        {cor == 3 && <p style= {{color:"green", fontWeight: "bold"}}>VERDE</p>}
        {cor === 0 && <p style= {{color:"black", fontWeight: "bold"}}>CEMAFORO DESLIGADO.</p>}
        
        <button onClick = {mudancaCor}>Proxima Cor</button>
    </div>

    )
}