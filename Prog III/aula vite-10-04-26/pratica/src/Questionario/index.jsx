import { useState } from "react"
import Questao from "./Questao"
export default function Questionario(props){
  const listaPerguntas = props.listaPerguntas;//derivação para facilitar o codigo, reduzindo. se a propriedade e obrigatorio tem que tratar o erro se caso não tem que ver.  
  const [acertos,setAcertos] = useState(0);
  const [erros, setErros] = useState(0);
  const nota = acertos/(acertos+erros)*10;
  const notaString = new Intl.NumberFormat("pt-Br", 
    {style:"decimal", maximaFractionDigits:2}).format(nota); //e um derivado de nota que é derivado de erros e acertos que sao estados.
  
    function respondeu(acertou){
    //alert("verfica") verificação se chegou aqui.
    let novoEstadoDoAcertos = acertos;
    let novoEstadoDoErros = erros;

    if(acertou){
      novoEstadoDoAcertos=novoEstadoDoAcertos+1;
    }else{
      novoEstadoDoErros++;
    }
    setAcertos(novoEstadoDoAcertos);
    setErros(novoEstadoDoErros);
  }
  listaPerguntas.map((objetoPergunta => <Questao 
      pergunta={objetoPergunta.resposta} 
      resposta={objetoPergunta.resposta? "sim":"não"}
      onRespondeu={respondeu}

      />
    
  ))
 /* function nota(acertos,erros){
    if (acertos + erros == 3){ (acertos*10)/3}
    alert("verifica se chega em nota.")
  }*/
  
  return (//componentes se comunicão somente com o pai, para ter comunicação entre eles deve se comunicar para o pai e o pai retorno para o outro componente.
    <div>
      Total de acertos: 
      {/*<span style={{color:"green"/*quando se munda de contexto para saber se uma expressão ou bloco de codigo}}>{acertos}</span>
      /
      <span style={{color:"red"}}>{erros}</span>
      */}
      <span className="acertou">{acertos}</span>
      /
      <span className="errou">{erros}</span>
      /
      <span>{acertos+erros}</span>
      <br />
      {listaPerguntas.map((objetoPergunta) =><Questao 
    key={objetoPergunta.id/*propriedade especifica do react onde ela se reorganiza se mudar a chave na lista e se mudar o componente e a chave for unica ele so redesenha o mesmo.*/}
      pergunta={objetoPergunta.pergunta} 
      resposta={objetoPergunta.resposta? "sim":"não"}
      onRespondeu={respondeu}
      />)
      }
      {/*<Questao 
        pergunta = "a grama e verde?"
        resposta = "sim"
        onRespondeu = {respondeu}
        />
        
      <Questao 
        pergunta = "a terra e plana?" 
        resposta = "não"
        onRespondeu = {respondeu}
        />
        
      <Questao 
        pergunta = "o ovo vem da galinha? " 
        resposta = "sim"
        onRespondeu = {respondeu}
        />
        <br />
        {/*Nota Final:descobri hj que o .jsx não aceita comentarios.}
        */}
        <br />
        
        
        <span>{acertos+erros==3? (acertos*10/3).toFixed(2): ""/*é funcional mas para fica pleno o certo seria colocar o Nota final dentro do span, exemplo:  acertos+erros==3?Nota Final: (acertos*10/3).toFixed(2): ""*/}</span><br />
        <span style={{display:(acertos+erros==3? "inline": "none")}}>nota</span><br />
        <br />
        {((acertos+erros)>=3)? <span>Nota: {notaString/*quando e feito a parti de um teste a rederização o termo e rederização condicional*/}</span>:null} <br />
        {((acertos +erros)>=3)&&<span>Notas: {notaString/*aqui estou usando o and pq ele verifica o primeiro elemento neste caso o teste logico e se verdadeiro verifica o segundo elemento e com isso se verdadeiro exibe o segundo elemento. Este e o modo ideal de utilização de rederização condicional.*/}</span>}

    </div>
  )
}
/*vou mudar para index pois fica nome padrao que e uma boa pratica
codigo anterior

      <button>Botão</button>

      <input/>
      Componente inicial
      <div>
        A terra e azul? 
        <label><input type="radio" value="sim" name="qt1" />Sim</label>
        <label><input type="radio" value="nao" name="qt1" />Não</label>
      </div>
      <div>
        A terra e redonda? 
        <label><input type="radio" value="sim" name="qt2" />Sim</label>
        <label><input type="radio" value="nao" name="qt2" />Não</label>
      </div>
*/
/*hoje vamos ver formas de ver a media que se solicitou na ultima aula, 24/04/26.
debito tecnico e quando temos funções e ou metas que não estão plenamente aplicados. pode vir a ser de mal feito ou não implementação do de parte da função, sendo um codigo de baixo desempenho.
debito cognitivo e quando temos um codigo que não é de facil intendimento pois foi feito em parte ou total por IA com isso não temos ninguem que consiga explicar o codigo

*/