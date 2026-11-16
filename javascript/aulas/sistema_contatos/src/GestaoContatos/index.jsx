import Tabela from "./Tabela"
import axios from "axios"
import { useEffect,useState } from "react";
import DialogFormulario from "./DialogFormulario";

export default function GestaoContatos(){
    const [exibirCadastroContato, setExibirCadastroContato] = useState(false)
    const [contatos, setContatos] = useState([]);
    async function buscarContatos(){
        let retorno = await axios.get("http://localhost:3000/contatos");
        setContatos(retorno.data);
        console.log("Executou")
    }

    useEffect(()=>{
        console.log("Inicio do useEffect")
        buscarContatos();
        console.log("Fim do useEffect");
        return ()=>{
            console.log("Componente Destruido!");
        }
    },[])//teste neste caso sem () eu estou passando a função. e quando esta como teste() estou executando
    
    async function enviar(novoContato){
        console.log(novoContato)
        let retorno = await axios.post("http://localhost:3000/contatos",novoContato);
        console.log(retorno)
        setExibirCadastroContato(false)
        buscarContatos();
    }

    return<>
        <button onClick={()=>setExibirCadastroContato(true)}>Cadastrar Novo Contato</button>
        {exibirCadastroContato &&
            <DialogFormulario onEnviar = {enviar} onFechar = {()=>setExibirCadastroContato(false)}/>
        }
       <Tabela contatos = {contatos}/>{/*estou passando o estado propriedade para tabela. */}
    </>
}
/*
este e um codigo com uso de rederisação condicional
onde o && e um and que verifica o primeiro termo que se verdadeiro verifica o segundo
como um componente e sempre verdadeiro vai redenrisar o componente.
{exibirCadastroContato&&  
        <dialog open>
            Teste
        </dialog>:null}
aqui e um metodo menos comercial
<button onClick={()=>setExibirCadastroContato(true)}>Cadastrar Novo Contato</button>
        {exibirCadastroContato?
        <dialog open>
            Teste
        </dialog>:null}
*/