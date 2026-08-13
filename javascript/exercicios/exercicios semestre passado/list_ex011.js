//11. Somar Valores Pares
let numeros = [1,2,3,4,5,6,7,8,9,10]

function somaPares(parametro){
    let pares = parametro.filter(filtro => filtro % 2 == 0).reduce((acumulador,numero) => acumulador + numero);
    return pares
}
console.log(somaPares(numeros));