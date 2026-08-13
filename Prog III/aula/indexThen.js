import { input } from '@inquirer/prompts';


const perguntar = input({ message: 'nome: ' });//sem o await da um resultado diferente de "enter your name"
function retornaQuandoResponder(oQueFoiRespondido){
    
    console.log("Olá, "+oQueFoiRespondido);

}
perguntar.then (retornaQuandoResponder);//then e um metodo que recebe uma função, que confirma se a promeça foi respondida.
console.log("chegou aqui!");
//console.log(answer);

