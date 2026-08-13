import { input } from '@inquirer/prompts';
import CrudAPI from './CrudAPI.js';
/*versao fora da função

const nome = await input({ message:"Nome: " });
const idade = await input({message:"Idade: "});
console.log("Olá, "+nome+" você tem "+idade);
*/
const pessoas = await CrudAPI.lerTodos();
console.log(pessoas)
async function lerDadosPessoa() {
    const nome = await input({ message:"Nome: " });
    const idade = await input({message:"Idade: "});
    console.log("Olá, "+nome+" você tem "+idade);
    return pessoa;
}
const pessoa = await lerDadosPessoa();
console.log(pessoa);