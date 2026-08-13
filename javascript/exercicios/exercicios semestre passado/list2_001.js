//filter: Crie uma função que retorne um array com todos os números pares de um array.
let numeros = [1, 2, 3, 4];

function pares(parametro){
    let par = parametro.filter(filtro => filtro % 2 == 0)
    return par
}
console.log(pares(numeros))
