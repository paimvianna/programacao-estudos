/*
3.Média simples
Peça três notas.
Calcule a média aritmética e exiba no console.
*/
import readlineSync from 'readline-sync';


/*function media(){
    let soma = 0
    console.log(`---Seja bem vindo ao sistema de notas.---`)
    for(let i = 0; i<3; i++){
        let nota = Number(readlineSync.question(`Informe a nota do ${i+1}º semestre: `));
        soma += nota;
    }
    let media = soma/3
    console.log(`A media dos três semestres é ${media.toFixed(2)}.`);
}*/

function validaNota(mensagem){
    let nota;
    do{
        nota = Number(readlineSync.question(mensagem));
        if(isNaN(nota) || nota < 0 || nota > 10){
            console.log(`A nota deve ser um numero entre 0 e 10!`)
        }
    }while(isNaN(nota) || nota < 0 || nota > 10);
    return nota
}

function media(){
    let soma = 0
    console.log(`---Seja bem vindo ao sistema de notas.---`)
    for(let i = 0; i < 3 ; i++){
        let nota = validaNota(`Informe a nota do ${i+1}º semestre: `);
        soma += nota;
    }
    let media = soma/3;
    console.log(`A media dos três semestres é ${media.toFixed(2)}.`);
}

media();       