export default function CadastroQuestoes(props){

    function enviar(formulario){
        let questao={};
        questao.pergunta = formulario.get('pergunta');
        questao.resposta = formulario.get('pergunta')=='sim';
        console.log(questao);
        props.onCadastrar(questao)
        alert("Foi enviado o form");
    }
    return<>
        <form action={enviar}>
            <br />
            <br />
            <label>Pergunta: <input type="text" name="pergunta"/> </label>
            <br />
            <br />
            <label>Resposta: </label>
            <label><input name="resposta" type="radio"/>Sim</label>
            <label><input name="resposta" type="radio"/>Não</label>
            <br /><br />
            <button type="submit">Cadastrar</button>
        </form>
        aqui vai o cadastro
    </> 
    }