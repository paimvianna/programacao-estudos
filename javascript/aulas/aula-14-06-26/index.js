import * as readline from "node:readline/promises";
import {stdin as input , stdout as output} from 'node:process';
import CrudAPI from "./CrudAPI.js";

const leitor = readline.createInterface({input,output});

async function listarTodos(){
    let contatos = await CrudAPI.lerTodos();
    if (contatos){
        console.log(contatos);
        contatos.forEach(contato => 
        console.log(contato.id +' - '+ contato.nome+' - '+contato.email))  
    }else{
        console.log('Registro não encontrado.');
    }
    
    }

async function criarContato() {
    //nome não pode ser vazio 
    //o email tem que ter @
    let nome = await leitor.question('Digite nome: ');
    //if(!nome) 
    if (nome == ""){
        console.log('Nome não pode ser um campo vazio!')
    }else{
        let email = await leitor.question('Digite o email: ')
        if (!email.includes("@")){
            console.log('E-mail deve ter @: ');
        }else{
            let contato = {nome:nome, email:email};
            let contatoBanco = await CrudAPI.criar(contato);//aqui a API vai me retorna o
            console.log ('Cadastro realizado com sucesso, nova ID: '+contatoBanco.id);                                                // objeto inserido com o id ou seja o banco e retorna um novo objeto com mesmos dados e com o ID
        }
    }
}

async function buscarPorId() {
    let id = await leitor.question('Digite o ID: ');// posso usar assim tambem Number (await leitor.question('Digite o ID: '))
    id = Number(id);
    let contato = await CrudAPI.lerPorId(id);//posso usar assim tambem let contato = await CrudAPI.lerPorId(Number(id))
    //console.log (contato)  
    console.log('ID: '+ contato.id);
    console.log('Nome: '+ contato.nome);
    console.log('Email: '+ contato.email);
      
}

let opcao = "";

while(opcao!=9){
    console.log('Menu de opção:')
    console.log('1 - Criar novo registro: ')
    console.log('2 - Lista todos os contatos')
    console.log('3 - Buscar registro')
    console.log('4 - Atualizar Resgistro')
    console.log('5 - Excluir Registro')
    console.log('6 - Tudo Maiúsculo')
    console.log('7 - Sobrenome Primeiro')
    console.log('8 - Pesquisa por Nome')
    console.log('9 - Sair')
    opcao = await leitor.question('Escolhe uma opção: ')
    console.log(opcao)
    switch(opcao){
            case "1":
                console.log("Criar novo registro");
                await criarContato();
                break;
            case "2":
                console.log("Listar todos os registros")
                await listarTodos();
                break;
            case "3":
                console.log("Listar todos os registros")
                await buscarPorId();
                break;
            case '4':
                console.log('Atualizar registro: ')

                break;
            case '5':
                console.log('Excluir registro: ')

                break;
            case '6':
                console.log('Imprimir tudo em maiusculo');

                break;
            case '7':
                console.log('Sobrenome primeiro')
                break;
            case '8':
                console.log('Pesquisa por nome')
                break;
            case "9":
                console.log('Encerrando o aplicativo')
                opcao = 9;
                break;

    }
}
leitor.close()