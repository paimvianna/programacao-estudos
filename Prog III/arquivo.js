function saudacao(){
    alert("Bem-vindo ao nosso site!");
}

//Variáveis de escopo global
var globalVar = "Sou uma variável global";
function exemplo(){
    console.log(globalVar);//acessivel aqui
}

//Variáveis de escopo local
function exemplo(){
    var localVar = "Sou uma variável local";
    console.log(localVar);//acessível apenas nesta função
}
console.log(localVar);//Erro: variável não definida fora da função

//Variáveis de escopo de bloco
function exemplo(){
    if(true){
        var x = 5; //Tem escopo de função
    }
    console.log(x); //Exibe 4, pois a variável é acessível em toda a função
}
exemplo(); //Executa a função exemplo

function exemplo(){
    if (true){
        let x = 5; //Tem escopo de bloco
    }
    console.log(x); //Erro: variável não está disponível fora do bloco
}
exemplo(); // Executa a função exemplo()

//Exemplo de elevação (hoisting) de variáveis
console.log(x); // undefined
var x = 10;
console.log(x); // 10

//Aqui ocorre a elevação, mas ocorre o erro pois eta dentro de um bloco.
function exemplo() {
     console.log(x); // Error: Cannot access 'x' before initialization
     let x = 10; //x inicializa apos a utilização da vairavel.
}
exemplo(); // Executa a função exemplo()

//parseInt()
let str = "10";
let num = parseInt(str); // Resultado: 10

let str = "FF";
let num = parseInt(str,16);

//parseFloat()
let str = "3.14";
let num = parseFloat(str); //Resultado:3.14

//Strinng()
let num = 42;
let str = String(num); // Resultado: "42"

Number
let str = "42";
let num = Number(str); // Resultado: 42

//concatenação

//Operador +(operador de soma)

let saudacao = "Olá";
let nome = "Maria";
let mensagem = saudacao + ", " + nome + "!";
console.log(mensagem); // Saída: "Olá, Maria!"

//Método concat()
let saudacao = "Olá";
let nome = "Maria";
let mensagem = saudacao.concat(", ", nome, "!");
console.log(mensagem); // Saída: "Olá, Maria!"

//Spread Operator


let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
let newArray = [...array1, ...array2];
console.log(newArray); // Saída: [1, 2, 3, 4, 5, 6]
