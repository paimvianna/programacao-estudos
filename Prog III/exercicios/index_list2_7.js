/*map: Extraia a propriedade nome de um array de objetos.
    Exemplo: [{nome: "Alice"}, {nome: "Bob"}] → ["Alice", "Bob"] */
let Exemplo= [{nome: "Alice"}, {nome: "Bob"}]

function nomeObjetos(array){
   return array.map(nome => nome.nome)
}
console.log(nomeObjetos(Exemplo))