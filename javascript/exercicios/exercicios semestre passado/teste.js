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
let str1 = "10";
let num1 = parseInt(str); // Resultado: 10

let str2 = "FF";
let num2 = parseInt(str,16);

//parseFloat()
let str3 = "3.14";
let num3 = parseFloat(str); //Resultado:3.14

//Strinng()
let num4 = 42;
let str4 = String(num); // Resultado: "42"

Number
let str = "42";
let num = Number(str); // Resultado: 42

//concatenação

//Operador +(operador de soma)

let saudacao = "Olá";
let nome1 = "Maria";
let mensagem1 = saudacao + ", " + nome + "!";
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

//passagem de pararametros
function saudar(nome) {
    console.log("Olá, " + nome + "!");
}
//Neste exemplo, nome é um parâmetro que a função saudar espera receber quando é chamada.

//passagemm por valor. Neste exemplo, a função adicionarDez recebe o valor de numero como parâmetro e o altera dentro da função, mas essa alteração não tem efeito fora dela. O valor original do parâmetro permanece inalterado porque ele é passado por valor.
function adicionarDez(x) {
    x = x + 10; // Modifica o parâmetro dentro da função
}

let numero = 5;
adicionarDez(numero); // Chama a função com o valor do número
console.log(numero);  // O valor ainda é 5

//passagem por referência. Neste exemplo, a função alterarPropriedade recebe uma referência ao objeto pessoa e altera uma de suas propriedades. Como a função opera em uma referência ao objeto, a modificação é visível fora da função.
function alterarPropriedade(obj) {
    obj.nome = "Maria"; // Modifica a propriedade do objeto
}

let pessoa = { nome: "João" };
alterarPropriedade(pessoa); // Chama a função com uma referência ao objeto
console.log(pessoa.nome);  // O valor é alterado para "Maria"

//valores padrão para parâmetros. Os valores padrão são úteis para garantir que a função tenha um comportamento previsível mesmo quando argumentos são omitidos.
function saudar(nome = "Visitante") {
    console.log("Olá, " + nome + "!");
}

saudar(); // Usa valor padrão, imprime "Olá, Visitante!"
saudar("Ana"); // Usa argumento passado, imprime "Olá, Ana!"

//parâmetros rest. Neste exemplo:
/*
    A função somar usa o parâmetro rest ...numeros para capturar todos os argumentos passados para a função.
    O método reduce é aplicado ao array numeros para somar todos os valores.
    A função somar pode aceitar qualquer quantidade de argumentos, de zero a muitos.

    OBS: Os parâmetros rest devem ser o último elemento na lista de parâmetros da função. Isso garante que todos os argumentos restantes sejam capturados pelo parâmetro rest.
*//*
//Veja um exemplo no quadro abaixo:
function mostrar(nome, ...outros) {
    console.log("Nome:", nome); // Primeiro argumento
    console.log("Outros:", outros); // Demais argumentos
}

mostrar("Alice", "Bob", "Charlie"); // "Nome: Alice", "Outros: ['Bob', 'Charlie']"
//este exemplo, o primeiro argumento é tratado como um parâmetro normal, enquanto o restante é capturado pelo parâmetro rest outros.

//ESCOPO

//escopo de função. Neste exemplo, a variável x foi declarada dentro da função minhaFuncao. Portanto, ela só é acessível dentro dessa função. Tentar acessá-la fora do escopo da função resulta em erro.
/*function minhaFuncao() {
    const x = 10; // Variável local ao escopo da função
    console.log(x);
}

minhaFuncao(); // Imprime 10
console.log(x); // Causa erro, pois `x` está no escopo da função

//escopo global. Neste exemplo, a variável y é declarada no escopo global e é acessível dentro da função outraFuncao. As funções têm acesso ao escopo global, mas não vice-versa.
const y = 20; // Variável global

function outraFuncao() {
    console.log(y); // Acessa a variável global
}

outraFuncao(); // Imprime 20

//escopo de bloco. Desde o ECMAScript 2015 (ES6), variáveis declaradas com let ou const têm escopo de bloco, significando que elas só são acessíveis no bloco onde foram declaradas. Os escopos de bloco são criados por estruturas como if, for, e while. 
function bloco() {
    if (true) {
        let x = 10; // Escopo de bloco
        console.log(x); // Funciona
    }

    // console.log(x); // Causa erro, pois `x` está fora do escopo do bloco
}

//hoisting. Em JavaScript, as declarações de função e variáveis com var sofrem "hoisting". Isso significa que elas são "elevadas" para o início do escopo da função, independentemente de onde são declaradas no código. No entanto, apenas as declarações são elevadas, não as atribuições. 
function exemplo() {
    console.log(a); // undefined, por causa do hoisting da variável `var`
    var a = 10; // Declaração da variável
    console.log(a); // Imprime 10
}
//escopo léxico. Neste exemplo, a função funcaoInterna tem acesso ao escopo da função funcaoExterna, mesmo após funcaoExterna ser chamada e retornada. Isso é possível por causa do escopo léxico, que mantém referências ao contexto original onde a função foi definida.
function funcaoExterna() {
    const valor = "externo";

    function funcaoInterna() {
        console.log(valor); // Acessa a variável do escopo da função externa
    }

    return funcaoInterna; // Retorna uma função que "lembra" do escopo

}

const minhaFuncao = funcaoExterna();
minhaFuncao(); // Imprime "externo", porque lembra do escopo léxico*/