/*map: Converta cada número de um array para uma string com o sufixo "kg".
Exemplo: [2, 5] → ["2kg", "5kg"]*/

let numeros = [1,2,3,4,5,6,7,8,9,10]

function conversorComSufixo(parametro){
    return parametro.map(numero=>String(numero+'kg'))
}
console.log(conversorComSufixo(numeros))