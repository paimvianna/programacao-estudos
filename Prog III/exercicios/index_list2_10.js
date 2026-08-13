/*map: Crie um array com a propriedade preço de um array de objetos de produtos.
    Exemplo: [{nome: "apple", preco: 2}, {nome: "banana", preco: 3}] → [2, 3]*/
let Exemplo= [{nome: "apple", preco: 2}, {nome: "banana", preco: 3}]

function verPreco(array){
    return array.map(objeto => objeto.preco)
}
console.log(verPreco(Exemplo))