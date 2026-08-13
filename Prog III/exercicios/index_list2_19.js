/*reduce: Calcule o produto de todos os números de um array.
    Exemplo: [2, 3, 4] → 24 */
let Exemplo= [2, 3, 4]
function arrayProduto(array){
    return array.reduce((acumlador,numero) => acumlador*numero,1)
}
console.log(arrayProduto(Exemplo))