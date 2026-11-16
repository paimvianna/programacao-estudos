/*2.Componente Carta:

    Servir como a representação visual de cada carta no jogo e permitir que o usuário interaja com ela.
    O componente deve ser renderizado como um botão que:
        Apresenta uma borda vermelha se a carta estiver selecionada.
        Apresenta um fundo verde se a carta já foi encontrada.
        Exibe o nome da carta caso tenha sido selecionada ou já tenha sido achada, 
        caso contrário, mostra um asterisco (*). */
export default function Carta(props){
    //const id = props.id nao esta sendo usado apesar de ser um parametro de carta
    const nome = props.nome
    const selecionada = props.selecionada
    const achada = props.achada
    const onSelecionar = props.onSelecionar

    function Estado(){
        let estado = ""
        if(!selecionada && !achada){
            estado = "padrao"
        }else if(selecionada && !achada){
                estado = "selecionado"
        }else if(!selecionada && achada){
                estado = "achado"
        }
        return estado    
    }
    const estados = {
        padrao:{texto:"*", color:"white", background: "black"},
        selecionado:{texto: nome, color:"white", background:"black", border:"2px solid red"},
        achado:{texto: nome, color:"white", background:"green" }
    }
    const estadoAtual = estados[Estado()]
    return(
    <button style={{color:estadoAtual.color,
        background: estadoAtual.background,
        border:estadoAtual.border}} 
        disabled = {achada}
        onClick={onSelecionar}>{estadoAtual.texto}</button>//o gemini disse que o pai vai passar os parametros entao nao preciso por no onSelecionar
    )
} 