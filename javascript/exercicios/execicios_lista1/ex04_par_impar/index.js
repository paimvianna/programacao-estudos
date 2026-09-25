/*
4.Par ou ímpar
Peça um número.
Use % para verificar se é par ou ímpar e mostre o resultado.
*/
import readlineSync from 'readline-sync';


function validaNumero(mensagem){
    let valor;
    let numero;
    do{
        valor = readlineSync.question(mensagem);
        numero = Number(valor)
        if (isNaN(numero) || (!valor) ){
            console.log(`O valor informado deve ser um numero.`)
        }
        console.log(typeof valor)
    }while(isNaN(numero) || (!valor));
    return valor;
}

function numeroParOuImpar(){
    let numero = validaNumero('Informe o numero que deseja verificar se e par ou impar: ')
    if (numero%2 == 0){
        console.log(`O numero ${numero} é par.`);
    }else {
        console.log(`O numero ${numero} é impar.`);
    }
}
numeroParOuImpar();
console.log(`Programa encerrado.`)