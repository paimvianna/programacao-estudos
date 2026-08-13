/*
filter: Crie uma função que retorne um array com todos os números pares de um array.
Exemplo: [1, 2, 3, 4] → [2, 4]
 */
let Exemplo= [1, 2, 3, 4];

function pares(array){
return array.filter(numero => numero%2===0);
}
let resultado = pares(Exemplo);
console.log(resultado)