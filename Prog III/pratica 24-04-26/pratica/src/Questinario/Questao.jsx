import { useState } from "react";
import "./questionario.css";
import imgSim from "../assets/sim.png";
import imgNao from "../assets/nao.png";
import imgErrou from "../assets/errou.png"
import imgAcertou from "../assets/acertou.png"
let contadorResposta=0;
export default function Questao(props){
    const [respostaDoUsuario, setRespostaDoUsuario] = useState(null);//espraimanto de uma lista array uso []
    const respondeu = respostaDoUsuario != null;//constante que recebe o valor diferente de null
    const {pergunta, resposta, onRespondeu}=props;
    function clicar(respostaDoClick){
        let novoEstadoDoUsuario=respostaDoUsuario;
        novoEstadoDoUsuario=respostaDoClick;
        setRespostaDoUsuario(novoEstadoDoUsuario);
        onRespondeu(novoEstadoDoUsuario==resposta);
    }
    const traducao ={
                        "sim":imgSim,
                        "não":imgNao,

    }
    return <div> {pergunta}
                {respondeu?<>
                    Resposta: <img src={imgSim}/> - <img src={resposta==respostaDoUsuario?imgAcertou:imgErrou}/> - 
                    <span style ={{color:resposta==respostaDoUsuario?"green":"red"}}>{resposta == respostaDoUsuario?"Acertou":"Errou"}
                    </span>
                    </>:/*no onClick, a gente tem um evento do componente button que recebe uma função*/<>
                    {/*<button
                        onClick={()=>clicar("sim")}>Sim</button>
                    <button
                        onClick={()=>clicar("não")}>Não</button>*/}
                    <img
                        src={imgSim}
                        title='Sim'
                        onClick={()=>clicar("sim")}/>
                    <img
                        src={imgNao}
                        title='Não'
                        onClick={()=>clicar("não")}/>
                    </>}
    </div>
}