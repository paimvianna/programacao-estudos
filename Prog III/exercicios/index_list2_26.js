/*find: Encontre o primeiro número maior que 10 em um array.
    Exemplo: [5, 8, 12, 3] → 12
     */
let Exemplo= [5, 8, 12, 3];

function maiorQDez(array){
    return array.find(numero => numero > 10)
}
console.log(maiorQDez(Exemplo))