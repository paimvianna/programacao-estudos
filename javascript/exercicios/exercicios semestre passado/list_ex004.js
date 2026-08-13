//4.Criar um Array de Strings de Saudação
let pesssoas = ["João","Maria","Pedro"];

let saudacao = pesssoas.map((pessoa) => "Olá, "+pessoa+"!" );
console.log(saudacao)

function saudacaoPessoa(pessoas){
    return pessoas.map((pessoa) => "Olá, "+pessoa+"!");
}
console.log(saudacaoPessoa(pesssoas));