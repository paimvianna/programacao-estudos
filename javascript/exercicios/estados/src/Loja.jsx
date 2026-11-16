/*7.Crie um componente que mostra as informações de um produto 
(nome e preço) e dois botões: “Aplicar desconto” e 
“Remover desconto”. Ao aplicar o desconto, o preço exibido 
deve ser reduzido (por exemplo, em 10%) e aparecer em 
destaque (cor ou estilo diferente). Ao remover o desconto, 
o preço deve voltar ao valor original e ao estilo normal.
 */
import { useState } from "react";

export default function Desconto(props){
    const produto = props.nome
    const preco = props.preco
    const desconto = props.desconto/100
    const [aplicarDesconto, setAplicarDesconto] = useState("naoaplicar")
    

    function selecionarDesconto(){
        setAplicarDesconto(aplicarDesconto=="naoaplicar"? "aplicar" : "naoaplicar")
    };

    function aplicarPromocao(){
        if(aplicarDesconto == "aplicar"){
            const precoDesconto = preco -(preco * desconto);
            return precoDesconto;
        }else if(aplicarDesconto =="naoaplicar")
            return preco
    };
    return(<div>
        <p style={{
            color:aplicarDesconto == "naoaplicar"? "black" : "blue",
            fontWeight:aplicarDesconto == "naoaplicar"? "normal" : "bold"
        }/*vou colocar 3 formas abaixo para nao ter erro*/}>
            {/*{aplicarDesconto === "naoaplicar" ? `Preço: R$ ${aplicarPromocao()}` : `Preço em promoção: R$ ${aplicarPromocao()}`}
            {aplicarDesconto === "naoaplicar" ? <span>Preço: {aplicarPromocao()}</span>  : <span>Preço em promoção: {aplicarPromocao()}</span>}*/}
            {produto} - {aplicarDesconto === "naoaplicar" ? "Preço" : "Preço em promoção"}: R$ {aplicarPromocao()}
        </p>
        <button disabled = {aplicarDesconto == "aplicar"}
            onClick = {selecionarDesconto}>Aplicar Desconto</button>
        <button disabled ={aplicarDesconto == "naoaplicar"}
            onClick={selecionarDesconto}>Remover Desconto</button>    
    </div>
    );
}
