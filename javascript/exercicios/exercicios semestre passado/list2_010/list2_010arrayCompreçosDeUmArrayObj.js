/*map: Crie um array com a propriedade preço de um array de objetos de produtos.
Exemplo: [{nome: "apple", preco: 2}, {nome: "banana", preco: 3}] → [2, 3]*/

let obj = [{nome: "apple", preco: 2}, {nome: "banana", preco: 3}, {nome:"maça", preco: 5}]

function listaPreco(parametro){
    //return parametro.map(produto => produto.preco)
    let valor = parametro.map(produto => produto.preco)
    return console.log(valor)
}
//console.log(listaPreco(obj))
listaPreco(obj)