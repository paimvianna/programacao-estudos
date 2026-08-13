/*every: Verifique se todos os números de um array são positivos.
    Exemplo: [5, -3, 10] → false
     */
let Exemplo= [5, -3, 10];

function positivos(array){
    return array.every(numero => numero >=0)
}
console.log(positivos(Exemplo))