/*
6.Calculadora simples
Peça dois números e uma operação (+, -, *, /).
Use if para decidir a operação e exiba o resultado no console.
*/
/*MINHA VERSÃO */
import readlineSync from 'readline-sync';

function validaNumero(mensagem){
    let valor;
    let numero;
    do{
        valor = readlineSync.question(mensagem);
        numero = Number(valor);
        if ((!valor) || isNaN(numero)){
            console.log(`O valor informado tem que ser numerico.`);
        }
    }while ((!valor) || isNaN(numero));
    return numero
}

function validaOperador(mensagem){
    let operador;
    do{
        operador = readlineSync.question(mensagem)
        if (!['+', '-', '*', '/'].includes(operador)){
            console.log(`Operador deve ser um das 4 operações basicas:\n Soma => +\n Subtração => -\n Multiplicação => *\n Divisão => /`);
        }
    }while(!['+', '-', '*', '/'].includes(operador))
    return operador
}

function calculadora(){
    console.log(`\n---Esta é a calculadora das 4 operações basicas, para ate 2 numeros.---`)
    let a = validaNumero(`\nInforme o 1º valor: `);
    let b = validaNumero(`\nInforme o 2º valor: `);
    console.log(`---Estes são os 4 operadores basicos: ---\n Soma => +\n Subtração => -\n Multiplicação => *\n Divisão => /`)
    let operador = validaOperador(`Por favor informe o operado que deseja: `);
    if (operador == '+'){
        console.log(`O resultado da soma de ${a} e ${b} e igual a ${a+b}.`);
    }else if(operador == '-'){
        console.log(`O resultado da subtração de ${a} e ${b} e igual a ${a-b}.`);
    }else if (operador == '*'){
        console.log(`O resultado da multiplicação de ${a} e ${b} e igual a ${a*b}.`);
    }else if (operador == '/'){
        console.log(`O resultado da divisão de ${a} e ${b} e igual a ${a/b}.`)
    }
}
calculadora();
console.log('Programa encerrado.');
/*VERSÃO DO OLLAMA COM MELHORIAS SEGUNDO ELE TENHO QUE VERIFICAR*/
/*
import readlineSync from 'readline-sync';

function validaNumero(mensagem) {
    let valor;
    let numero;
    do {
        valor = readlineSync.question(mensagem);
        numero = Number(valor);
        if (!valor || isNaN(numero)) {
            console.log(`O valor informado tem que ser numérico.`);
        }
    } while (!valor || isNaN(numero));
    return numero;
}

function validaOperador(mensagem) {
    let operador;
    do {
        operador = readlineSync.question(mensagem);
        if (!['+', '-', '*', '/'].includes(operador)) {
            console.log(`Operador deve ser um das 4 operações básicas: +, -, *, /`);
        }
    } while (!['+', '-', '*', '/'].includes(operador));
    return operador;
}

function calculadora() {
    console.log(`\n---Esta é a calculadora das 4 operações básicas, para até 2 números.---`);
    let a = validaNumero(`\nInforme o 1º valor: `);
    let b = validaNumero(`\nInforme o 2º valor: `);
    let operador = validaOperador(`Por favor informe o operador que deseja (+, -, *, /): `);

    if (operador == '+') {
        console.log(`O resultado da soma de ${a} e ${b} é igual a ${a + b}.`);
    } else if (operador == '-') {
        console.log(`O resultado da subtração de ${a} e ${b} é igual a ${a - b}.`);
    } else if (operador == '*') {
        console.log(`O resultado da multiplicação de ${a} e ${b} é igual a ${a * b}.`);
    } else if (operador == '/') {
        if (b === 0) {
            console.log(`Erro: Divisão por zero.`);
        } else {
            console.log(`O resultado da divisão de ${a} e ${b} é igual a ${a / b}.`);
        }
    }
}

calculadora();
console.log('Programa encerrado.');
*/