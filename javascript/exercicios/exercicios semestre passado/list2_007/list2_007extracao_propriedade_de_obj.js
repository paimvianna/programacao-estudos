/*map: Extraia a propriedade nome de um array de objetos.
Exemplo: [{nome: "Alice"}, {nome: "Bob"}] → ["Alice", "Bob"]*/
let objetos = [{nome: "Alice"}, {nome: "Bob"}, {nome:"Sandro"}]

function retornaNome(parametro){
    let nomes = parametro.map(obj => obj.nome)
    return console.log(nomes)
}
retornaNome(objetos)