import { contaArray, exibeValor, PI, contaArray,exibeValor as outroNOme } from "./biblioteca.js";
import listaDePessoas from "./pessoas.js";
import usuario from "./usuario.js";
import fornecedores from "./subpasta/fornecedores.js";

import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

functionquandoResponder(resposta){
    console.log("Respondeu, com o valor "+resposta);
}
const entradaDeDados = readline.createInterface({input, output});
let promessaDoNome = entradaDeDados.question("Qual o seu nome");
promessaDoNome.then(quandoResponder);

exibeValor(1);
exibeValor(0);
contaArray([3,5]);
console.log(PI);
console.log(pessoasExemplo.nome)
console.log(listaDePessoas);
UserActivation.teste();

//entradaDeDados.close();