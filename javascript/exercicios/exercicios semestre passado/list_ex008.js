//produto de todos os numeros com reduce

let numeros=[1,2,3,4];

function produto (parametro){
   return parametro.reduce((parametro,numero) => parametro*numero)
}
console.log(produto(numeros))