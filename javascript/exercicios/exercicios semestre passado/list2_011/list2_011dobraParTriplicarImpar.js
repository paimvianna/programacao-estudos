/*list2_011map: Dobre os números pares e triplique os números ímpares de um array.
    Exemplo: [1, 2, 3] → [3, 4, 9]*/

let numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

function dobraParTriplicarImpar(parametro){
    let listaNova = parametro.map(numero => numero % 2 == 0 ? numero*2 : numero*3)
    return console.log(listaNova)
}
dobraParTriplicarImpar(numeros)