function teste(){
    console.log("teste!");
}
let teste2 = teste;//teste e teste2 estao apontando para o mesmo bloco de codigo. quando chamadas executam o mesmo bloco.
teste2();
teste();

function testeA(a){
    a();
    a();
    a();
}
testeA(teste);