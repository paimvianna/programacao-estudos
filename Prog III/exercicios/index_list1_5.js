/*5. Filtrar Números Pares

Crie uma função que filtre todos os números pares de um array.

Entrada: [1, 2, 3, 4, 5, 6]

Saída esperada: [2, 4, 6]*/
let numeros = [1, 2, 3, 4, 5, 6];

//usando o console.log direto com filter no array numeros.
console.log(numeros.filter(numero => numero%2==0 ));

//vou fazer uma uma variavel que receba o array e imprimir
let pares = numeros.filter(numero => {return numero%2==0})
console.log (pares)
console.log(...pares)
console.log(pares.join(", "))