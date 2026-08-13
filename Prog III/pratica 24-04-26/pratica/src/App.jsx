import GestaoQuestoes from "./GestaoQuestoes/index.jsx";
import listaPerguntas from "./listaPerguntas.js";
import Questionario from "./Questinario";
//import CadastroQuestoes from "./CadastroQuestoes";
import { useState } from "react";
/*o estado ele e o interno que e o caso aqui. ja a propriedade e so auterado pelo pai.*/
export default function App() {
  const[modo,setModo]=useState();//"", "cadastro", "teste"
  const [listaPerguntasMock, setlistaPerguntasMock] = useState(listaPerguntas);
  //const listaPerguntasMock = listaPerguntas;

  /*function cadastroQuestao(questao){
    //alert("A questão chegou aqui: "+ questao.pergunta);
    questao.id = Math.round [Math.random()*1000]
    //let novaLista = [...listaPerguntasMock];
    let novaLista= [...listaPerguntasMock,questao];
    //let novaLista = strutucturedClone(listaPerguntasMock)
    //novaLista.push(questao);
    setlistaPerguntasMock(novaLista)
  }*/
  return (<>
    <button onClick={()=>setModo("cadastro")}>Gestão de Questão A</button>
    <button onClick={()=>setModo("teste")}>Teste Questionário</button>
    {/*modo=="cadastro" && <CadastroQuestoes/>*/}
    {/*modo=="teste" && <Questionario listaPerguntas={listaPerguntasMock}/>*/}
    
    {modo=="cadastro"? <GestaoQuestoes 
                        listaPerguntas={listaPerguntasMock} 
                        onChange={(novalistaPerguntas) => setlistaPerguntasMock(novalistaPerguntas)}
                        />:
    (modo=="teste"?<Questionario listaPerguntas={listaPerguntasMock}/>:null)
    }
    </>
  )
}