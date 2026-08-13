/*8. Encontrar o Produto de um Array

Crie uma função que use reduce para calcular o produto (multiplicação) de todos os elementos de um array.

Entrada: [1, 2, 3, 4]

Saída esperada: 24 */

let numeros=[1,2,3,4]
let produto = numeros.reduce((produto,numero) => produto*numero,1);//Aqui como e uma multiplicação não podemos começa em 0, sendo necessario o inicio em 1.
console.log(produto);