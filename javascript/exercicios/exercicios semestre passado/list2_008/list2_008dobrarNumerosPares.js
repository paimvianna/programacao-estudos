/*map: Dobre os valores dos números pares de um array (deixe os ímpares inalterados).obs utilizei operador ternario.
Exemplo: [1, 2, 3] → [1, 4, 3]*/
let numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

function dobraPares(parametro){
    return parametro.map(numero => numero%2 == 0 ? numero*2 : numero)
}
console.log(dobraPares(numeros))