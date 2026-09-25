/*
5.Maior de idade
Peça a idade.
Se idade ≥ 18, mostre “Maior de idade”; caso contrário, “Menor de idade”.
*/
import readlineSync from 'readline-sync';

function validaNumero(mensagem){
    let valor;
    let numero;
    do{
        valor = readlineSync.question(mensagem);
        //console.log(valor); usei para veificar se recebia o valor digitado na entrada.
        numero = parseInt(valor, 10);
        if ((!valor) || isNaN(numero) || numero < 0 ){
            console.log (`A idade deve ser um numero inteiro positivo.`)
        }
    }while((!valor) || isNaN(numero) || numero < 0 )
    return numero
    }

function verificaMaior18(){
    console.log(`---Seja bem vindo ao sistema de verificação de Maior Idade.---`)
    let idade = validaNumero(`Informe a sua Idade: `);
    //console.log(idade); usei para saber o que esta sendo atribuido a idade, descobri um undefined, pq no fim validaNumero nao retornava numero posi esqueci o return.
    let verificado = idade >= 18 ? "Você é Maior de Idade." : "Você é Menor de Idade.";
    console.log(verificado)
}
verificaMaior18();
console.log('Programa encerrado.')