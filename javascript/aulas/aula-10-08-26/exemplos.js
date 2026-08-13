let nome;//variavel declarada de forma dinamica, outro tipo e o var é estatico.
let sobrenome;
console.log("Olá Mundo!");//Primeiro codigo da aula 10/08/26
//devo usar ; para separa coamndos ou enter ou os dois juntos
nome="anderson";//usnado aspas duplas ou simples
sobrenome='paim';
nome='Carlos'
nome = nome +sobrenome;
console.log(nome);
nome=2;
sobrenome=3;
console.log(nome);

let a=1;
let b='1';
let c=a+b;
console.log(c);//resultado sera uma string pois vai concatenar e converte o numero para uma string
console.log(typeof(c)); 

a='2';
b=3;
c=a*b;
console.log(c);//como nao tem dualidade na * e nos valores ele converte a string em numero.

a=2;
b='ola';
c=a*b;
console.log(c);//a string não tem correspondente em numeros e por isso da NaN

a="";//se converte para 0
b=2;
c=a*b;
console.log(c);//vai ser 0, pois ""e convertido pra zero.

const PI = 3.14 // constante
console.log(PI)