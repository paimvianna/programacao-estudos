/*find: Encontre o primeiro objeto em um array com id igual a 2.
    Exemplo: [{id: 1}, {id: 2}] → {id: 2}
     */
let Exemplo= [{id: 1}, {id: 2},{id: 3},{id: 4}, {id: 0}]

function primeiroID2(array){
    return array.find(id => id.id==0)
}
console.log(primeiroID2(Exemplo))