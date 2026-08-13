/* every: Verifique se todos os números de um array são pares.
    Exemplo: [2, 4, 6] → true*/
let Exemplo= [2, 4, 6, 8];

function strgPar(array){
    return array.every(numero => numero%2==0)
}
console.log(strgPar(Exemplo))