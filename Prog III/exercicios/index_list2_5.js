/*map: Crie um array com o quadrado dos números de um array original.
    Exemplo: [2, 3, 4] → [4, 9, 16] */

let Exemplo= [2, 3, 4];

function quadradoArray(array){
    return array.map(valor => valor*valor)
}
console.log(quadradoArray(Exemplo))