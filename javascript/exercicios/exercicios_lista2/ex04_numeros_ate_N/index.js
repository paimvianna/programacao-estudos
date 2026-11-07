/*
4)Números pares até N
Peça um número e mostre todos os pares de 1 até N com while.
*/
import readlineSync from 'readline-sync';

//Criação da função para verificar os numeros
function validaNumero(mensagem){
    let habilita = true;
    let valor = 0;
    let numero = 0;

    while (habilita){
        valor = readlineSync.question(mensagem);
        numero = parseInt(valor);
        /*
        if ((!valor) || isNaN(numero)){
            console.log(`O valor de entrada deve ser um numero inteiro.`)
        }else{
        habilita = false
        }
        */
       //Se Nao for NaN e a strin digitada não for só espaços vazios
        if (!isNaN(numero) && valor.trim() !== ""){
            return numero; //retorna o numero e encerra o laço
        }
    }
    return numero;
}

//Criação de função para verificar pares no array

function numerosPares(){
    let numero = validaNumero(`Informe o numero 'N', que se verificará os pares de 0 a 'N': `);
    /*for (let i =0 ; i <= numero; i++){
        if(i % 2 == 0 && i != 0){
            console.log(i)
        }       
    }*/
    while (i<=numero){
        if (i%2 === 0 ){
            console.log(i);
        }
   }
}

numerosPares();
console.log(`Programa Encerrado.`)