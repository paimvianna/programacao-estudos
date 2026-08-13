import {input, select} from '@inquirer/prompts';
import CrudAPI from './CrudAPI.js';

/*//aqui e o CruAPI sem funçoes
let pessoas = await CrudAPI.lerTodos(); 
console.log(pessoas)
async function lerDadosPessoa() {
    const nome = await input({message:"Nome: "});
    const idade = await input({message:"Idade: "});
    console.log("Olá, "+nome+"você tem "+idade);    
}
const pessoa = await lerDadosPessoa();
console.log(pessoa);*/
async function cadastrar() {
    let nome;
    let email;
    while(!nome){
        nome = await input({message:"Nome: "});
    }
    while(!email){
        email = await input({message:"Email: "});
    }
    let pessoa = {nome: nome, email:email};
    let cadastrado = await CrudAPI.criar(pessoa);
    console.log("Cadastrado com sucesso! id: "+cadastrado.id)
}

async function listarTodos(){
    let todos = await CrudAPI.lerTodos();
    todos.forEach((pessoa) =>{
    console.log(pessoa.id+"-"+pessoa.nome+"-"+pessoa.email)
})
}
async function buscarPorId() {//tenho que me ligar pra ver o que estou comparando. neste caso foi o id q e um numero.
    let id;
    while(!id){
        id = await input({message:"Informe o ID para pesquisa: "});
    }
    let numeroId = Number(id);
    let resultadoBuscaId = await CrudAPI.lerPorId(numeroId);
    if (!resultadoBuscaId){
        console.log("Registro nao encontrado.")
} else {
        console.log("ID: "+resultadoBuscaId.id);
        console.log("Nome: "+resultadoBuscaId.nome);
        console.log("Email: "+resultadoBuscaId.email);
}
}

async function atualizarRegistro(){
    //recebe e valida o id
    let id = true;
    let idRegistroNovo;
    while(id){
        id = await input({message:"Informe o ID para modificação: "});
        idRegistroNovo = Number(id);
        if(idRegistroNovo > 0 && idRegistroNovo != isNaN){
            id = false
        }else{
            console.log("Opção invalida, digite um numero.")
            id  = true
        }
        
    }

    //autenticação de nome e recebimento
    let nome = true
    let nomeRegistroNovo;
    while(nome){
        nome = await input({message:"Informe o novo nome para modificação: "});
        // verifico o tipo de entrada sabendo que iria ser um str console.log(typeof nome)
        if(isNaN(nome)){
            nomeRegistroNovo = nome;
            nome = false;
            //verifico o que esta sendo rcebido por nome apos if console.log(nome)
        }else{
            console.log("Nome deve ser composto pelo alfabeto.")
        }
    }

    //recebe e autentica o email.
    let email = true;
    let emailRegistroNovo;
    while(email){
        email = await input({message:"Informe o novo email para modificação: "});
        if(email != '' && email !=' '){
            emailRegistroNovo = email;
            email = false;
        }else{
            console.log("Email deve ser composto como alfanumerico sem espaços.")
            email = true;
        }
    }
     let dadosNovos  = {nome:nomeRegistroNovo,email:emailRegistroNovo};
        await CrudAPI.atualizar(idRegistroNovo,dadosNovos);
}

async function excluirRegistro() {
     let id = true;
    let idRegistroExcluir;
    while(id){
        id = await input({message:"Informe o ID para modificação: "});
        idRegistroExcluir = Number(id);
        if(idRegistroExcluir > 0 && idRegistroExcluir != isNaN){
            id = false
        }else{
            console.log("Opção invalida, digite um numero.")
            id  = true
        }
        
    }
    await CrudAPI.excluir(idRegistroExcluir)
}

async function tudoMaiusculo(){
   let todos = await CrudAPI.lerTodos();
    todos.forEach((pessoa) =>{
    let linha = (pessoa.id+"-"+pessoa.nome+"-"+pessoa.email);
    let linhaMaiuscula = linha.toUpperCase();
    console.log(linhaMaiuscula);
}) 
}

function quebraNome(nome){
    let quebra = nome.split(" ");
    if(quebra.length <= 1){
        return nome;
    }
    let sobrenome =quebra[quebra.length -1];//aqui o quebra  aplica o split, com isso entre os [] fica o indice que vai ser o length -1 que sera o ultimo endereço do array quebra.
    let nomePrimeiro = quebra[0];
    return sobrenome+","+nomePrimeiro;
}

async function sobrenomePrimeiro() {
    let todos = await CrudAPI.lerTodos();
    todos.forEach((pessoa) =>console.log(quebraNome(pessoa.nome))
)
}

async function pesquisaPorNome(){
    let pessoa = await CrudAPI.lerTodos()
    let nome = true
    let nomeValido;
    while(nome){
        nome = await input({message:"Informe o novo nome para modificação: "});
        if(isNaN(nome)){
            nomeValido = nome;
            nome = false;
            //verifico o que esta sendo rcebido por nome apos if console.log(nome)
        }else{
            console.log("Nome deve ser composto pelo alfabeto.")
        }
    }
    let nomeBusca = nomeValido.toLowerCase()
    let resultado = pessoa.filter(pessoa => {
        let nomeMinusculo = pessoa.nome.toLowerCase();
        return nomeMinusculo.includes(nomeBusca);
    });
    if (resultado.length ===0){
        console.log("Nenhum resultado encontrado.");
    }else{
        console.log("Resultado da busca: ");
        resultado.forEach(pessoa => {console.log(pessoa.id+" - "+pessoa.nome+" - "+pessoa.email);
    });
    }
    return resultado

}

//menu interativo com switch
let opcao = "";
while (opcao != "sair"){
    opcao = await select({
    message: 'Opção: ',
    choices:[
        {name:'cadastrar', value:'cadastrar'},
        {name:'listar todos', value:'listar todos'},
        {name:'buscar por id', value:'buscar por id'},
        {name:'atualizar registro', value:'atualizar registro'},
        {name:'excluir registro', value:'excluir registro'},
        {name:'tudo maiusculo', value:'tudo maiusculo'},
        {name:'sobrenome primeiro', value:'sobrenome primeiro'},
        {name:'pesquisa nome', value:'pesquisa nome'},
        {name:'sair', value:'sair'},
    ]});
    switch(opcao){
        case "cadastrar":
            await cadastrar();
        break
        case "listar todos":
            await listarTodos();
        break
        case "buscar por id":
            await buscarPorId();
        break
        case "atualizar registro":
            await atualizarRegistro();
        break
        case "excluir registro":
            await excluirRegistro();
        break
        case "tudo maiusculo":
            await tudoMaiusculo();
        break
        case "sobrenome primeiro":
            await sobrenomePrimeiro();
        break
        case "pesquisa nome":
            await pesquisaPorNome();
        break
    }
}
console.log(opcao);