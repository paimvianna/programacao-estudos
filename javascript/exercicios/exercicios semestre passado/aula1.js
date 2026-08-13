let x = 5;
console.log(x);

console.log("teste!");

const h= "teste da constate";
console.log(h);

let X = 7

console.log(x+X) // teste de case sensitive onde x tem um valor e X outro.

let a = 2
let b = 3
let c = "2" //tipo string

console.log(a+b)
console.log(a/b)
console.log(a%b)
console.log(a*b)
console.log(c+b) //concatenou termo 'c' e o termo 'b'. Convertendo o 'b' para a string.
console.log(Number(c)+b) //converti o 'c' de string para numero e somei

let z = "Olá,"
let y = " mundo"

console.log(z+""+y); //concatenei sem espaços entre apas duplas.
console.log(z.length) //tamanho da string
console.log(z.substring(1,2))//seleciona parte especifica da string começando em 1 e terminando e 2 pegando a letra l se fosse de 1 a 3 pegaria a letra lá, veja no proximo exemplo.
console.log(z.substring(1,3))

let w =`soma de ${a} + ${b} é ${a+b}`;
console.log(w);

if(a < 3){
    console.log("menor que 3.");
}else{
    console.log("maior ou igual a 3.");
}
//na inplementação a baixo temos uma conversão de tipo e uma comparação
if (a == c){
    console.log("Igual")
}
// na implementação temos uma comparação sem conversão de tipo
if (a === c){
    console.log("igual")
}else{
    console.log("diferente")
}

//switch para seleção de caso. EX.
let alimento = "laranja"
switch(alimento){
    case "maça":
        console.log("É "+alimento);
        break;
    case "banana":
        console.log("É "+alimento);
        break;
    case "batata": // aqui em neste case em sequencia e para situaçoes que são multiplas, tipo batata e beterraba que são legumes.
    case "beterraba":
        console.log("É legume"+alimento);// concatenei a variavel junto ao print.
        break;
    default:// aqui defino caso não se enquadre em nenhum dos anteriores.
        console.log("Não sei");
}
//sistema de teste logico com ?
let t = -1;

let aux = t > 0 ? "maior": "menor";
let texto = "O valor de t é "+aux;
console.log(texto)

//forma de declaração com operador de crase
console.log(`O valor de t é ${t} que é ${t > 0 ? "maior":"menor"} que zero.`)

//trabalhando com array listas
let d = new Array(1,2,3);
let e = Array(1,2,3);
let f = [1,2,2,"3"];
/*console.log(d);
console.log(e);*/
console.log(f);
f.push(4);
f[5] = 5;
console.log(f);
