/*map: Some os elementos de arrays internos e retorne um array com os resultados.
    Exemplo:
    Entrada: [[1, 2], [3, 4, 5], [10]] → [3, 12, 10] */
let Entrada= [[1, 2], [3, 4, 5], [10]]

function somaArrayInterno(array){
    return array.map(arrayInterno => {
        return arrayInterno.reduce((acumulador,numero) => acumulador +numero,0)})
}
console.log (somaArrayInterno(Entrada))