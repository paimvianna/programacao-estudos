import * as readline from "node:readline/promises";
import {stdin as input , stdout as output} from 'node:process';
import CrudAPI from "./CrudAPI.js";

const leitor = readline.createInterface({input,output});

async function listarTodos(){
    let contatos = await CrudAPI.lerTodos();
    if (contatos){
        //console.log(contatos);
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

async function atualizarRegistro(){
    console.log('Informe o ID e os dados solicitados para atualização do registro.');
    let habilitaId = true;
    let habilitaNome = true;
    let habilitaEmail = true;
    let id = undefined;
    let nome = undefined;
    let email = undefined;
    while(habilitaId){
        id = await leitor.question('Digite o ID:');
        if (id.trim()===''){
            console.log('Erro: O ID não pode ser um vazio ou apenas espaço!')
        }else {
            id = Number(id);
            if (id == isNaN){
                console.log('O ID deve ser um numero!');
            }else{
                //console.log(typeof(id)) aqui to imprimindo o tipo de id
                habilitaId = false
                //console.log(habilitaId) aqui to imprimindo
                //  o valor atribuido a habilitaId neste caso false
            }
        }
    }
    //console.log(habilitaId);
    while(habilitaNome){
        nome = await leitor.question('Digite o Nome:');
        if (!nome.trim() || !Number.isNaN(Number(nome))){
            console.log('Nome deve ser alfabetico, ano pode ser vazio espaço vazio ou somente numeros!')
        }else{
            habilitaNome = false;
            //console.log(nome);
        }
    }
    //console.log(habilitaNome);
    while(habilitaEmail){
        email =await leitor.question('Digite o E-mail: ')
        if (!email.includes('@')){
            console.log('E-mail deve conter @: ');
        }else{
            habilitaEmail = false;
            let dadosAtualizados = {nome:nome, email:email};
            let registroAtualizado = await CrudAPI.atualizar(id,dadosAtualizados);
            //console.log(registroAtualizado);
            console.log('ID: '+registroAtualizado.id);
            console.log('Nome: '+registroAtualizado.nome);
            console.log('E-mail: '+registroAtualizado.email);
        }
    }
    /*
    }else{
        let nome = await leitor.question('Digite o Nome:');

        //if (!nome || nome != " " || nome || nome == isNaN)
        if (!nome){
            console.log('Nome deve ser alfabetico.')
        }else{
            let email = await leitor.question('digite o E-mail: ')
            if (!email.includes("@")){
                console.log('E-mail deve ter @: ');
            }else{
                let dadosAtualizados = {nome:nome, email:email}
                let registroAtualizado = await CrudAPI.atualizar(id,dadosAtualizados);
                //console.log(registroAtualizado)
                console.log('ID: '+registroAtualizado.id)
                console.log('Nome: '+registroAtualizado.nome)
                console.log('E-mail: '+registroAtualizado.email)
            }
        }
    }*/
    
}

async function excluirRegistro(){
    //console.log('Informe o ID que deseja excluir: ')
    let id = await leitor.question('Informe o ID que deseja excluir: ')
    id = Number(id);
    //await buscarPorId();
    let excluido =  await CrudAPI.excluir(id);
    //console.log(excluido);
    console.log('O registro que foi excluido: ');
    console.log('ID: '+excluido.id);
    console.log('Nome: '+excluido.nome);
    console.log('E-mail: '+excluido.email);
}

async function nomeMaiusculo(){
    let contatos = await CrudAPI.lerTodos();
    if (contatos){
        //console.log(contatos);
        contatos.forEach(contato => 
        console.log(contato.id +' - '+ contato.nome.toUpperCase()+' - '+contato.email))  
    }else{
        console.log('Registro não encontrado.');
    }
}

async function sobreNome(){
    let contatos = await CrudAPI.lerTodos();
    if (contatos){
        //console.log(contatos);
        contatos.forEach(contato => {
            let sobreNome = contato.nome.trim().split(" ");
            let nome = sobreNome[0];
            sobreNome = sobreNome[sobreNome.length-1]
            //console.log(sobreNome.length)
            
            console.log(contato.id +' - '+ sobreNome+' '+nome+' - '+contato.email)
        })
        
    }else{
        console.log('Registro não encontrado.');
    }
}

async function buscarPorNome(){
    let nome = await leitor.question("Informe o nome ou texto que inicia o nome a ser buscado: ")
    let contatos = await CrudAPI.lerTodos();//nao posso esquecer o await
    //console.log(contatos);
    contatos.forEach(contato => {
        if (contato.nome.startsWith(nome)){
            console.log(contato.id +' - '+contato.nome+' - '+contato.email)
        }
    })
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
    //console.log(opcao)
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
                await atualizarRegistro();
                break;
            case '5':
                console.log('Excluir registro: ')
                await excluirRegistro();
                break;
            case '6':
                console.log('Imprimir tudo em maiusculo');
                await nomeMaiusculo();
                break;
            case '7':
                console.log('Sobrenome primeiro')
                await sobreNome();
                break;
            case '8':
                console.log('Pesquisa por nome')
                await buscarPorNome()
                break;
            case "9":
                console.log('Encerrando o aplicativo')
                opcao = 9;
                break;

    }
}
leitor.close()