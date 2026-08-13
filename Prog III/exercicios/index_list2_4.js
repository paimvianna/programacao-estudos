/*filter: Filtre objetos de um array onde a propriedade ativo seja true.
    Exemplo: [{ativo: true}, {ativo: false}] → [{ativo: true}] */

let Exemplo= [{nome:"joao", ativo: true}, {nome:"maria",ativo: false}];

function objetoAtivo(array){
    return array.filter(objeto => objeto.ativo ==true)
}
console.log(objetoAtivo(Exemplo))