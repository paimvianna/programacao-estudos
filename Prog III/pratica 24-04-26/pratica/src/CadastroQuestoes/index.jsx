import { useState } from "react";

export default function CadastroQuestoes(props){
    const [pergunta, setPergunta]=useState("");
    const [resposta, setResposta]=useState("");
    const [justificativa, setJustificativa]=useState("");

    function enviar(formulario){
        let questao={};
        questao.pergunta = formulario.get('pergunta');
        questao.resposta = formulario.get('pergunta')=='sim';
        questao.justificativa = justificativa
        console.log(questao);
        props.onCadastrar(questao);

        alert("Foi enviado o form");
    }
    function mudarPergunta(event){
        console.log(event);
        console.log(event.target.value);
        setPergunta(event.target.value);
    }
    function mudarResposta(event){
        let novaResposta = event.target.value;
        console.log(event.target.value);
        setResposta(event.target.value)
        if(novaResposta=="sim"){
            setJustificativa("")
        }
    }
    return<>
        <form action={enviar}>
            <br />
            <br />
            <label>Pergunta: 
                <input 
                type="text"
                name="pergunta" 
                value= {pergunta} 
                onChange={mudarPergunta}
                requerid/> </label>
            <br />
            <br />
            <label>Resposta: </label>
            <label><input name="resposta" onChange={mudarResposta} checked= {resposta=="sim"} required type="radio"value="sim"/>Sim</label>

            <label><input name="resposta" onChange={mudarResposta}    checked= {resposta=="não"} required type="radio"value="não"/>Não</label>
            <br /><br />
            {resposta == "não"?<>
            Exibir campo novo.
            <label >Justificativa: 
                <input
                    name="justificativa"
                    value={justificativa}
                    onChange={(event) => setJustificativa(event.target.value)}/> </label>
            </>:null }
            <button type="submit">Cadastrar</button>
            {pergunta} <br />{resposta}
        </form>
        aqui vai o cadastro
        
    </> 
    }