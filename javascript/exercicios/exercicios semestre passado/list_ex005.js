//5. Filtrar Números Pares
let numeros = [1,2,3,4,5,6];
let numeros_pares = numeros.filter((numero => numero % 2 === 0));
console.log(numeros_pares);

function Pares(parametro){
    return parametro.filter((numero => numero % 2 ===0));
}
console.log(Pares(numeros));