/*reduce: Calcule a soma de todos os números de um array.
    Exemplo: [1, 2, 3] → 6 */
let Exemplo= [1, 2, 3]

function somaArray(array){
    return array.reduce((acumulador, numero) => acumulador + numero,0)
}
console.log(somaArray(Exemplo))