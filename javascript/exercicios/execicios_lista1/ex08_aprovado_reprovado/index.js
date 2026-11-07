/*
8.Aprovado ou reprovado
Peça duas notas.
Calcule a média.
Se média ≥ 7, mostre “Aprovado”; senão, “Reprovado”.
*/

import readlineSync from 'readline-sync';


function validaNota(mensagem){
    let valor;
    let numero;
    do{
        valor =  readlineSync.question(mensagem);
        numero = Number(valor);
        if ((!valor)|| isNaN(numero) || numero < 0 || numero > 10){
            console.log('A nota tem que ser um numero valido entre 0 e 10.')
        }
    }while((!valor) || isNaN(numero) || numero < 0 || numero > 10)
    return numero
}



function obterQtdAvaliacoes(mensagem){
    let valor;
    let numero;
    do{
        valor =  readlineSync.question(mensagem);
        numero = Number(valor);
        if ((!valor)|| isNaN(numero) || numero <= 0){
            console.log('O numero de avaliações tem que ser um numero maior que zero.');
        }
    }while((!valor) || isNaN(numero) || numero <= 0)
    return numero;
}
//lembrar nao posso usar o nome da função e variavel igual exemplo função casa(), variavel let casa e uma chama a outra: casa = casa().
function obterNotas(){
    let qtAvaliacoes = obterQtdAvaliacoes('Por favor informe a quantidae de notas: ');
    let listaNotas = [];
    for (let i =1; i<=qtAvaliacoes; i++){
        listaNotas.push(validaNota(`Informe a ${i}º nota: `));
    }
    return {listaNotas,qtAvaliacoes};
}

function calcularMedia(){
    let dados = obterNotas();
    //soma do array usando .reduce()
    let soma = dados.listaNotas.reduce((acumulador, nota) =>  acumulador +nota,0);//nao preciso de {} ou return pq no fim e uma função simple e insignificante ou seja simples.
    let media = soma/dados.qtAvaliacoes;
    console.log(`A media é: ${media.toFixed(2)}`);
    if (media >= 7){
        return 'Aprovado';
    }else{
        return 'Reprovado';
    }

}
console.log(`Status: ${calcularMedia()}`);
console.log(`Encerrando programa.`);