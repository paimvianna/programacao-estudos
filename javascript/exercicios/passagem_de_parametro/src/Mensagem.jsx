/*
5. Componente Mensagem

Crie um componente chamado Mensagem que receba:

    texto: conteúdo da mensagem.
    prioridade: pode receber "alta" ou "baixa".

Quando a prioridade for "alta", a mensagem deve ser apresentada em destaque, por exemplo, utilizando texto em negrito. Quando a prioridade for "baixa", o texto deve ser apresentado normalmente.
Exemplo de chamada

<Mensagem texto="Servidor indisponível." prioridade="alta" />
<Mensagem texto="Atualização disponível." prioridade="baixa" />

Exemplo de resultado esperado

Servidor indisponível.

Atualização disponível.
*/
export default function Mensagem(props){
    const prioridade = props.prioridade;
    const texto = props.texto;
    /*return(prioridade == "alta"?
        <p className={`mensagem-${prioridade}`}>{texto}</p>:
        <p>{texto}</p>
    )*/
    /*
    return(
    <p className={`mensagem-${prioridade}`}>{texto}</p>
    )*/
    const destaquePrioridade= ()=>{
    if (prioridade == "alta"){
        return "mensagem-alta"
    }
    return ""
    }
    return(
        /*não posso esquecer o () */
        <p className={`mensagem ${destaquePrioridade()}`}>{texto}</p>
    )
}