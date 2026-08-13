/*11. Somar Valores Pares

Dado um array de números, crie uma função que filtre apenas os números pares e, em seguida, use reduce para somar esses valores.

Entrada: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Saída esperada: 30 // (2 + 4 + 6 + 8 + 10 = 30) */

let Entrada= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

let produtoFinal= Entrada.filter(numero => numero%2==0).reduce
    ((acumulador,numero)=> acumulador+numero,0)
console.log(produtoFinal)