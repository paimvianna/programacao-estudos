/*
10.Jogo do número secreto
Defina um número secreto fixo (ex.: 7).
Peça um palpite.
Se acertar, “Acertou!”; senão, “Errou, o número era 7”.
*/
import readlineSync from 'readline-sync';

function validaValor(mensagem){
    let numero;
    let valor;
    do{
        valor = readlineSync.question(mensagem);
        numero = Number(valor);
        if((!valor)||isNaN(numero)){
            console.log(`Você tem que utilizar somente numeros.`);
        }
    }while((!valor)||isNaN(numero));
    return numero
}

//jogo numero secreto
function numeroScreto(){
    console.log(`---Jogo do numero secreto---
        \nEste e o jogo do numero secreto,
        \n a dinamica e a seguinte. Sera
        \n preciso dois usuarios, um deve
        \n escolher um numero, o outro 
        \n deve tentar decobrir o valor.
        \n- Sera somente 3 tentativas.
        \n- O numero digitado deve ser entre 0 e 10`)
    let numero = validaValor(`Informe o numero a ser adivinhado: `)
    for (let i = 1; i < 4; i++){
        let chute = validaValor(`Você tem ${4-i} chance pra adivinha o numero, faça uma tentativa: `);
        if (chute === numero){
            console.log(`Você acertou, parabens!!!`);
            break
        }else{
            console.log(`Você errou, tente novamente.`);
        }
    }
}
numeroScreto();
console.log(`Programa encerrado.`);