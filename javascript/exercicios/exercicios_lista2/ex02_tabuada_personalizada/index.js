/*
 Tabuada personalizada
Peça um número e mostre sua tabuada de 1 a 10 usando while.
*/
import readlineSync from 'readline-sync';

function validaNumero(mensagem){
    let valor;
    let numero;
    do{
        valor = readlineSync.question(mensagem);
        numero = parseInt(valor);
        if((!valor) || isNaN(numero)){
            console.log(`O valor de entrada tem de ser um numero.`)
        }
    }while((!valor) || isNaN(numero))
    return numero;
}

function tabuadaPersonalizada(){
    let numero = validaNumero(`Informe o numero que deseja a tabuada: `);
    console.log(`---Tabuada Persoanlizada---`)
    for (let i = 1; i <= 10; i++){
        console.log(numero + ' x '+ i +' = '+ numero * i)
    }
}
tabuadaPersonalizada();
console.log(`Programa Encerrado.`)