/*
7.Comparação de dois números
Peça dois números.
Informe qual é o maior ou se são iguais.
*/
import readlineSync from 'readline-sync';

function validaNumero(mensagem){
    let valor;
    let numero;
    do{
        valor = readlineSync.question(mensagem);
        numero = Number(valor);
        if ((!valor) || isNaN(numero)){
            console.log('O valor tem de ser um numero decimal.');
        }
    }while((!valor) || isNaN(numero));
    return numero
}
function comparaNumeros(){
    let numeros = [];
    for (let i = 0;i < 2; i ++){
        numeros.push(validaNumero(`Informe o ${i+1}º para comparar:`));
    }
    let resposta = numeros[0]>numeros[1]? `O numero ${numeros[0]} é o maior.`: 
                    numeros[0]<numeros[1]? `O numero ${numeros[1]} é o maior.` : `Os numeros são iguais.`;
    return console.log(resposta)
}
comparaNumeros();
console.log('Programa encerrado.')
/*
VERSÃO DO OLLAMA BASEADO NO MEU CODIGO

import readlineSync from 'readline-sync';

function validaNumero(mensagem) {
    let valor;
    let numero;
    do {
        valor = readlineSync.question(mensagem);
        numero = Number(valor);
        if ((!valor) || isNaN(numero)) {
            console.log('O valor tem de ser um número decimal.');
        }
    } while ((!valor) || isNaN(numero));
    return numero;
}

function comparaNumeros() {
    let numeros = [];
    for (let i = 0; i < 2; i++) {
        numeros.push(validaNumero(`Informe o ${i + 1}º para comparar:`));
    }
    let resposta = numeros[0] > numeros[1] ? `O número ${numeros[0]} é o maior.` :
                    numeros[0] < numeros[1] ? `O número ${numeros[1]} é o maior.` : `Os números são iguais.`;
    return resposta;
}

let resultado = comparaNumeros();
console.log(resultado);
console.log('Programa encerrado.');
*/