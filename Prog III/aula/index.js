import { input, select } from '@inquirer/prompts';
import CrudAPI from './CrudAPI.js';

async function listarTodos(){
    //formato id - nome - email
    let todos = await CrudAPI.lerTodos();
    todos.forEach((pessoa) => {
        console.log(pessoa.id + " - "+pessoa.nome+" - "+pessoa.email)
    })
}
function quebraNome(nome){
    let quebra = nome.split(" ");
    if(quebra.length <= 1){
        return nome;
    }
    let sobrenome = quebra[quebra.length -1];
    let nommePrimeiro =quebra[0]; 
    return sobrenome +", "+nommePrimeiro;
}/*
console.log(quebraNome("João Silva"));
console.log(quebraNome("Maria do Exemplo"))
console.log(quebraNome(Marisa));
exit();*/
async function listarTodosSobrenome() {
    let todos = await CrudAPI.lerTodos();
    todos.forEach((pessoa)=> console.log(quebraNome(pessoa.nome)))
    
}
async function cadastrarPessoa(){
    let nome;
    let email;
    while(!nome){
        nome = await input({message: "Nome: "});
    }
    while(!email){
        email = await input({message: "Email: "});
    }
    let pessoa = {nome:nome, email:email};
    let cadastrado = await CrudAPI.criar(pessoa);
    console.log("Cadastrado com sucesso! id: "+cadastrado.id)
}
let opcao = "";
while(opcao != "sair"){
  opcao = await select({
  message: 'Opção: ',
  choices: [
    {name: 'cadastrar',value: 'cadastrar'},
    {name: 'listar', value: 'listar'},
    {name: 'sobrenome', value: 'sobrenome'},
    {name: 'sair', value: 'sair'},
  ]});
  switch (opcao) {
    case "listar":
        await listarTodos();
    break
    case "cadastrar":
        await cadastrarPessoa();
    break
    case "sobrenome":
        await listarTodosSobrenome();
    break
  }
}
console.log(opcao);