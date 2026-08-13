import pessoas from "./pessoas.js";
import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const entradaDeDados = readline.createInterface({input, output});

console.log(pessoas);
let continuar="s"

async function lerPessoa(){
    let nome = await entradaDeDados.question("nome: ")
    let email = await entradaDeDados.question("email: ")
    console.log("nome: "+ nome+" - " +email);
    let novaPessoa={nome:nome, email:email};
    return novaPessoa;
}

while(continuar=="s") {
    let novaPessoa = await lerPessoa();
    pessoas.push(novaPessoa);
    console.log(pessoas);
    continuar= await entradaDeDados.question("Adicionar outra pessoa?(s/n)");
}
entradaDeDados.close();