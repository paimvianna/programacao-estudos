/*7. Somar Todos os Elementos de um Array

Crie uma função que use reduce para somar todos os números de um array.

Entrada: [1, 2, 3, 4, 5]

Saída esperada: 15*/

let numeros=[1,2,3,4,5];
let soma = numeros.reduce((acumulador, numero) => acumulador+numero,0)//o numero 0 e pra defini o inicio.
console.log(soma);