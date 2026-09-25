/*
2.Soma de dois números
Peça dois números.
Converta com Number e mostre a soma no console.
*/
import readlineSync from 'readline-sync';

/*
function sumNumbers(a, b) {
  return Number(a) + Number(b);
}

const numero1 = readlineSync.question('Por favor informe o primeiro numero: ');
const numero2 = readlineSync.question('Por favor informe o segundo numero: ');

console.log(`O resultado da soma de ${numero1} + ${numero2} = ${sumNumbers(numero1, numero2)}`);
*/
function soma(a,b){
      a = Number(a);
      b = Number(b);
      return a + b;
}

let numero1 = readlineSync.question('Por favor informe o primeiro numero: ');
//numero1 = Number(numero1);

let numero2 = readlineSync.question('Por favor informe o segundo numero: ');
//numero2 = Number(numero2);

console.log(`O resultado da soma de ${numero1} + ${numero2} = ${soma(numero1,numero2)}`);