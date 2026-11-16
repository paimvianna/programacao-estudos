/*
8.Crie um componente que simula um player simples, exibindo 
o título de uma música, se ela está tocando ou pausada, e um
 valor de volume. Deve haver um botão “Play/Pause” que alterna
o estado exibido (tocando ou pausado) e um botão para aumentar
 o volume. A interface deve mostrar claramente o estado atual 
 (por texto ou ícone) e o valor do volume.
*/
import { useState } from "react"
export default function PlayerSimples(props){
    const musica = props.musica
    const [direcao, setDirecao] = useState(true)
    const[play, setPlay] = useState(false)
    const[volume, setVolume] = useState(0)
    function player(){
        setPlay(play === false? true : false)
    }
    /*
    metodo com bloqueio
    function aumentaVolume(){
        if(volume <100){
            setVolume(volume + 10)
        }
    };*/

    /*
    metodo loop
    function aumentaVolume(){
        if(volume <100){
            setVolume(volume + 10)
        }else if(volume == 100){
            setVolume(0)
        }
    };*/

    /*metodo ping-pong que eu fiz onde precisa de um clique a mais para mudar
     o valor apos a direção ja ter mudado
    function aumentaVolume(){
        if(direcao){
            if(volume < 100 && volume >= 0){
                setVolume(volume + 10)
            }else if(volume == 100){
                setDirecao(false)
            }
        }else if(!direcao){
            if(volume > 0 && volume <= 100){
                setVolume(volume-10)
            }else if (volume == 0){
                setDirecao(true)
            }
        }
    }*/

   /*metodo ping-pong com os ajustes do gemini sugeriu, no caso eu adaptei*/
    function aumentaVolume(){
        if(direcao){
            if(volume < 100 && volume >= 0){
                setVolume(volume + 10)
                if(volume +10 == 100){
                    setDirecao(false)
                } 
            }
        }else if(!direcao){
            if(volume > 0 && volume <= 100){
                setVolume(volume-10)
                if (volume - 10 == 0){
                    setDirecao(true)
                }
            } 
        }
    }
    /*codigo puro do gemini 
     function aumentaVolume() {
    if (direcao) {
        const proximoVolume = volume + 10;
        setVolume(proximoVolume);

        if (proximoVolume === 100) {
            setDirecao(false); // Já vira a bússola no mesmo clique!
        }
    } else {
        const proximoVolume = volume - 10;
        setVolume(proximoVolume);

        if (proximoVolume === 0) {
            setDirecao(true);  // Já vira a bússola de volta no zero!
        }
    }
}*/
     
    return(<div style={{padding:"15px", 
                        borderRadius: "6px", 
                        marginBottom: "16px",  
                        border:"2px solid #ccc",
                        background: play === true ?"#fff8dc":"#333",
                        color:play === true ?"#000":"#fff",
                        }}>
                        <p>{musica}</p>
                        <button onClick ={player}>
                            Play/Pause   
                        </button><br />
                        {play === true ? <p>Tocando</p> : <p>Pausado</p>}
                        {/*<button disabled = {volume == 100} onClick={aumentaVolume}>Volume + </button>*/}
                        <button onClick = {aumentaVolume}>Volume +</button>
                        <p>{volume == 100 ? "Volume Max. - " : (volume == 0 ? "Volume Min. - " : "Volume - ")}{volume}</p>
    </div>

    )
}