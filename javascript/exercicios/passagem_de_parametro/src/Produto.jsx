/*
4. Componente Produto

Crie um componente chamado Produto que receba:

    nome: nome do produto.
    preco: preço do produto.
    emPromocao: valor booleano que indica se o produto está em promoção.

O componente deve sempre exibir o nome e o preço. 
Quando emPromocao for true, também deve exibir a mensagem Em promoção!.
Exemplo de chamada

<Produto nome="Teclado" preco={120} emPromocao={true} />
<Produto nome="Mouse" preco={80} emPromocao={false} />

Exemplo de resultado esperado

Teclado - R$ 120,00 - Em promoção!

Mouse - R$ 80,00
*/
export default function Produto(props){
    const nome = props.nome
    const preco = props.preco.toFixed(2).replace('.',',')
    const emPromocao = props.emPromocao
    
    /*return(emPromocao == true ?
        <p>{nome} - R$ {preco} - Em promoção</p>
        :<p>{nome} - R$ {preco}</p>
        );
    */
    //codigo mais otimizado, pois emPromoção já e um booleano.
    return(
        <p>{nome} - R$ {preco} {emPromocao ? " - Em promoção" : ""}</p>
    )
}