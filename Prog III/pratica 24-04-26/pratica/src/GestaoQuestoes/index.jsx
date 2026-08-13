import { useState } from "react";
import ListaQuestoes from "../ListaQuestoes"
import CadastroQuestoes from "../CadastroQuestoes"

export default function GestaoQuestoes(props){
    console.log(props)
    const [exibirCadastro, setExibirCadastro]=useState(false);
    //props.listaPerguntas
    function cadastrarQuestao(questao){
        let novaListaPerguntas= [...props.listaPerguntas];
        questao.id=Math.round(Math.random()*1000);
        novaListaPerguntas.push(questao);
        props.onChange(novaListaPerguntas);
        setExibirCadastro(false);

    }
    return<div>
        <button onClick= {() => setExibirCadastro(true)}>Cadastrar nova questão</button><br /><br />
        <br /><br />
        lista de questôes
        {exibirCadastro?<dialog open >
            Teste
            <CadastroQuestoes onCadastrar={cadastrarQuestao}/>
            <button onClick={() => setExibirCadastro(false)}>Fechar</button></dialog>:null}
        <ListaQuestoes listaPerguntas={props.listaPerguntas}/>
    </div>
}