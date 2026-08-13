/*3. Converter um Array de Celsius para Fahrenheit

Crie uma função que receba um array de temperaturas em Celsius e retorne um novo array com as temperaturas convertidas para Fahrenheit.

Entrada: [0, 20, 30]

Saída esperada: [32, 68, 86]
*/
let Celsius = [0,20,30];
//aqui eu nomeei a function anonima com nome conversao, para usar com declaração anonima ou não eu preciso usar o termo function.
/*let Fahrenheit = Celsius.map(function conversao(temperatura){
    return (temperatura*1.8)+32;
});*/

//para funcionar plenamente tenho que usar chaves aqui.
let Fahrenheit = Celsius.map( temperatura =>{
    return (temperatura*1.8)+32;
});

//aqui eu imprimo um por linha
Fahrenheit.forEach(temperatura=>{
    return console.log(temperatura)
});
//usando o join eu posso usar qualquer separador neste caso a virgula, convertendo tudo em uma string.
console.log(Fahrenheit.join(", "));

//usando o Spread (...) me retorna o array limpo somente com seus elementos.
console.log(...Fahrenheit)

//impressão do arry com colchetes
console.log(Fahrenheit);
