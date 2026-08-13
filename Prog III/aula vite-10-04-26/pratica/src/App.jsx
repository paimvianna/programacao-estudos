import listaPerguntas from "./listaPerguntas.js"
import Questionario from "./Questionario"
export default function App(){
  
  const listaPerguntasMock = listaPerguntas
  /*[
    {
        pergunta : "a grama e verde?",
        resposta : true
    },
  {
        pergunta: "a terra e plana?", 
        resposta : false
  }
  ];*/

  return (
    <Questionario listaPerguntas={listaPerguntasMock}/>
  )
}
//ou defini primeiro e depois exporta