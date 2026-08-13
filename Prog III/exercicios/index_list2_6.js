/* map: Converta todas as strings de um array para maiúsculas.
    Exemplo: ["hello", "world"] → ["HELLO", "WORLD"] */

let Exemplo= ["hello", "world"];

function transformaEmMaiuscula(array){
    return array.map(palavra => palavra.toUpperCase())
}
console.log(transformaEmMaiuscula(Exemplo))