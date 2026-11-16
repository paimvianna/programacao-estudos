import { useState } from "react";

/*
6.Crie um componente que representa uma lâmpada com um 
pequeno painel na tela. Deve haver um botão para ligar/desligar 
a lâmpada e um botão para aumentar a intensidade da luz. 
A aparência visual (por exemplo, a cor de fundo) deve mudar 
quando a lâmpada estiver ligada ou desligada, e a intensidade 
da luz deve ser exibida em algum texto
*/
export default function LampadaPotenciometro(){
    const[ligaLampada, setLigalampada] = useState("claro")
    const[potenciaLampada, setPotenciaLampada] = useState(0)
    function ligar(){
        setLigalampada(ligaLampada === "claro"? "escuro" : "claro")
    }

    function aumentaPotenciaLampada(){
        if(potenciaLampada < 100){
            setPotenciaLampada(potenciaLampada + 10)
        }
    };
    function diminuiPotenciaLampada(){ 
        if(potenciaLampada > 0){
            setPotenciaLampada(potenciaLampada- 10)
        }
    };
   


    return(<div style={{padding:"15px", 
                        borderRadius: "6px", 
                        marginBottom: "16px",  
                        border:"2px solid #ccc",
                        background: ligaLampada === "claro"?"#fff8dc":"#333",
                        color:ligaLampada === "claro"?"#000":"#fff",
                        }}>
                        
                        <button onClick ={ligar}>
                            {ligaLampada === "claro"? "Desligar":"Ligar"}   
                        </button><br />
                        {ligaLampada !== "escuro"&& <p>Potencia Lampada {potenciaLampada}</p>}
                    <button disabled = {ligaLampada === "escuro"} onClick={aumentaPotenciaLampada}>Aumenta</button> 
                    <button disabled = {ligaLampada === "escuro"} onClick={diminuiPotenciaLampada}>Diminui</button>
                    {(ligaLampada == "claro" && potenciaLampada === 100) && <p>Potencia da lampada está no máximo.</p>}
                    {(ligaLampada == "claro" && potenciaLampada === 0) && <p>Potencia da lampada está no mínimo.</p>}
    </div>

    )
}