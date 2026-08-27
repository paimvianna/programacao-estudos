import treco from 'readline-sync';
let valor1 = treco.question("Digite um valor: ");
let valor2 = treco.question("Digite outro valor: ");
let valor1ComoNumero = Number(valor1);
let valor2ComoNumero = Number(valor2);
console.log(typeof(valor1));//typeof e somente com um f
console.log(typeof(valor1ComoNumero));

console.log(valor1+valor2);
console.log(valor1ComoNumero+valor2ComoNumero);
