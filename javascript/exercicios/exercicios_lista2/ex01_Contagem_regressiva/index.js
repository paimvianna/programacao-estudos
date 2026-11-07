/*
1)Contagem regressiva
Peça um número N e faça contagem regressiva até 0 com while, mostrando cada número com alert.
*/
import readlineSync from 'readline-sync';

//Criação da função alert para o ambiente Node.js conforme o gemini
function alert(mensagem){
    readlineSync.question(`${mensagem} \n[Pressione ENTER para continuar]`)
}

function validaNumero(mensagem){
    let valor;
    let numero;
    do{
        valor = readlineSync.question(mensagem);
        numero = Number(valor);
        if((!valor) || isNaN(numero)){
            console.log(`O valor digitado, deve ser um numero.`);
        }
    }while((!valor) || isNaN(numero))
    return numero;
}

function contagemRegressivaPositiva(valor){
    let N = valor
    while(N>=0){
        //console.log(N);
        alert(N);
        N--;
    }
}

function contagemRegressivaNegativa(valor){
    let N = valor
    while(N<=0){
        //console.log(N);
        alert(N);
        N++;
    }
}
function verificaPositvoNegativo(){
    let valor = validaNumero(`Informe um numero N: `);
    if (valor>=0){
        contagemRegressivaPositiva(valor)
    }else{
        contagemRegressivaNegativa(valor)
    }
}
verificaPositvoNegativo();
console.log(`Contagem regressiva finalizada.`)