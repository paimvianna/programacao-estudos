/*
9.Login simples
Variáveis fixas: usuario = "admin" e senha = "1234".
Peça usuário e senha utilizando o readline-sync.
Se ambos corretos, “Acesso permitido”; caso contrário, “Acesso negado”.
*/
import readlineSync from 'readline-sync';

const usuario = 'admin';
const senha = '1234';

function validaUsuario(mensagem){
    let loginDoUsuario = readlineSync.question(mensagem);
    do{
        if (!loginDoUsuario || !isNaN(loginDoUsuario)){
            console.log('O usuaro do login deve ter somente letras e não pode ser vazio.');
        };
    }while((!loginDoUsuario) || !isNaN(loginDoUsuario));
    return loginDoUsuario;
}

function validaSenha(mensagem){
    let valor;
    let loginSenhaUsuario
    do{
        valor = readlineSync.question(mensagem);
        loginSenhaUsuario = Number(valor);
        if((!valor) || isNaN(loginSenhaUsuario)){
            console.log('A senha do login deve ter somente numeros e não pode ser vazia.');
        }
    }while((!valor) || isNaN(loginSenhaUsuario));
    return loginSenhaUsuario
}

function login(){
    let userName = validaUsuario(`Informe seu usuario: `);
    let userSenha = validaSenha(`Informe sua senha: `);
    let senhaNumero = Number(senha);
    if ((userName == usuario) && (userSenha == senha)){
        return 'Acesso permitido';
    }else{
        return 'Acesso Negado';
    }
}
console.log(login());
console.log(`Encerrando Programa`);