import { useState } from "react";
//o setStat ele agenda uma mudança de estado no futuro, ou seja no carregamento do proximo ciclo sera atualizado. primeira coisa que devemos fazer e criar um variavel com o novo estado do componente, para ter o estado futuro.
let contadorResposta = 0;
export default function Questao(props){
    const [respostaDoUsuario, setRespostaDoUsuario] = useState(null);//espraimento de um alista array uso [] 
    const respondeu = respostaDoUsuario != null; // constante que recebe o valor diferentede null
    //const {pergunta, resposta} = props; // estou fazendo o espraiamento de propriedades de um objeto sendo assim importante o nome uso{}.
    const{pergunta, resposta, onRespondeu} =props;
    function clicar(respostaDoClick){
        //alert("respostaclick") para verificar se estava chegando aqui
        let novoEstadoDoUsuario=respostaDoUsuario;
        //let numeroDeQuestoes = 3
        novoEstadoDoUsuario = respostaDoClick;
        setRespostaDoUsuario(novoEstadoDoUsuario);
        onRespondeu(novoEstadoDoUsuario==resposta);

        //console.log (onRespondeu)
    }
    return <div> {pergunta}
            {respondeu?<>
                Resposta: {respostaDoUsuario} - 
                <span style={{color:resposta==respostaDoUsuario?"green":"red"}}>
                    {resposta == respostaDoUsuario?"Acertou":"Errou"}
                </span>
            </>:/*no onClick, a gente tem evento do componente button que recebe uma função*/<>
                <button
                    onClick={()=>clicar("sim")}>Sim</button>
                <button
                    onClick={()=>clicar("não")}>Não</button>
            </>}
    </div>
}

/* codigo desenvolvido
export default function Questao(props){
    console.log(props);//vai carregar todas as propriedades do objeto pq a ordem em html não importam.
    /*const pergunta = props.pergunta;
    const resposta = props.resposta;
    o props e um objeto com tres valores.
    podemos usar os valores direto do objeto, e para isso usaremos {}.
    exemplo: export default function Questao({pergunta, resposta})
    

    const arrayDoEstado = useState(false);
    const respondeu = arrayDoEstado[0];//esta atual do componente na verdade o iicial
    const funcaoParaMudarEstado = arrayDoEstado[1];//chama uma função que neste caso pode mudar o estado do componente.
    //userei espalhamento
    const [respondeu, setRespondeu //o prefixo para set por convenção e para mudança, sendo o segundo o valor para do array
    ] = useState(false);
    const [respostaDoUsuario, setRespostaDoUsuario] = useState(null);//criando um estado pra guarda a resposta do usuario, se inicia como null pq representa auxencia de estado.
    //const [respondeu, funcaoParaMudarEstado] = arrayDoEstado;//valor e função, esta inicial e função

    //const {resposta,pergunta} =props; //aqui tenho mudança de contexto pq agora estou puxando do javascript para o html e esta tecnica e um espraiamento
    const pergunta = props.pergunta;
    const resposta = props.resposta;
    function clicar(respostaDoClick){
        //alert(1);
        //alert(pergunta)
        //alert(resposta)
        if(resposta === respostaUsuario){
        setRespondeu(true);
        setRespostaDoUsuario(respostaDoClick);
        if (respondeu){
            if 
            return <div>
                {pergunta} resposta:{respostaDoUsuario} - 
                <span style={{color:resposta == respostaDoUsuario?}}></span>
                {resposta==respostaDoClick?"Acertou";"Errou"}
            </div>
        }
    }
//aqui o onclick esta sendo atribuido a função clicar, ou seja quando ela clica o botam executa a função.
    return<div>{pergunta}
        <button disabled = {respondeu} onClick={()=>clicar("sim")}>Sim</button>
        <button disabled = {respondeu} onClick={()=>clicar("não")}>Não</button>
    </div>
}*/