/*
1.Olá, usuário!
Peça o nome do usuário utilizando o readline-sync.
Mostre uma mensagem de boas-vindas com console.log usando concatenação.
         */
import readlineSync from 'readline-sync';

let nome = readlineSync.question(`Digite seu nome: `);
//aqui não e uma concatenação tradicional e uma interpolação de strings
console.log(`Olá, ${nome}!`);

//concatenação pura
let mensagem1 = ('Olá, ');
console.log('Ola, '+nome+'!');
console.log(mensagem1+nome+'!');

//metodo .concat()
let boasVindas = 'Ola, '.concat(nome, '!');
console.log(boasVindas);

//metodo operador de atribuição combinado
let mensagem = 'Olá, ';
mensagem += nome;
mensagem += '!';
console.log(mensagem);

// usando Array.prototype.join()
let mensagem2 = ['Olá, ', nome, '!'].join('');
console.log(mensagem2)

/*
2.Soma de dois números
Peça dois números.
Converta com Number e mostre a soma no console.
    */