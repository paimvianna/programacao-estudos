/*
3.Crie um componente que mostra o valor de um “volume” 
e dois botões: “Aumentar” e “Diminuir”. Os botões devem 
alterar o valor do volume, respeitando um limite mínimo 
(0) e máximo (100), e o valor atual deve ser exibido na tela.
*/
import { useState } from "react";

export default function ControleVolume(){
    const[volume, setVolume] = useState(0)
    function aumentaVolume(){
        if(volume < 100){
            setVolume(volume + 1)
        }
    };
    function diminuiVolume(){ 
        if(volume > 0){
            setVolume(volume- 1)
        }
    };
    return(<div>
        <p>Volume {volume}</p>
        <button onClick={aumentaVolume}>Aumenta</button> 
        <button onClick={diminuiVolume}>Diminui</button>
        {volume === 100 && <p>Volume está no máximo.</p>}
        {volume === 0 && <p>Volume está no mínimo.</p>}
    </div>

    );
}