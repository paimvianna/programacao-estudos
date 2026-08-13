/*map: Converta cada número de um array para uma string com o sufixo "kg".
    Exemplo: [2, 5] → ["2kg", "5kg"] */
let Exemplo= [2, 5];

function sufixoValor(array){
    return array.map(valor => valor +'kg')
}
console.log(sufixoValor(Exemplo))