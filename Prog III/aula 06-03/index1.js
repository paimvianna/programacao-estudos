console.log("Olá, mundo!");

function teste1(param1,param2)/*param1 e param2 da função sao de escobo interno ou seja valido para dentro da função.*/{
    return param1*3 + param2;
    }
    teste1;//somente estou citando a função.
    teste1(2,3);//aqui carrego os valore nos parametros na função mas nao imprimo.
    console.log(teste1(4,5));//aqui imprimo a função com os parametros carregados
    let param1 = 1; //atribuo o valor a variavel de nome param1
    let param2 = 5; //atribuo o valor a variavel de nome param2
    console.log(teste1(param2,param1)); //aqui estou fazendo o carregamento do valor das variaveis nas posições das variaveis da função. ou seja param2 vai ficar na posição de param1 na função e param1 vai ficar na função na posição de param2.

//lista e array são lista ordenadas onde a classe e sera um modelo, assim sendo a lista a classe onde se considera chave e valor.
let lista=[3,4];
let lista2=[4,3];
let objeto1=/*quando nao tem nada e vazio, e pra ser do tipo par chvar r valor. aceita como chave uma string ou um numero, ponto flutuante, ou identificador.*/
{
    nome:"anderson",//cahve e um identificador a esquerda e a direita o valor que e uma string.
    1:"3", //chave e um valor a esquerda e a direita e um valor tipo numero.
    "data de nascimento":"xx/xx/xxxx", //chave e valor sao strings e uma boa pratica deixar todas as chaves como strings.
    endereco:{rua:"exemplo",numero:"123"},//aqui tenho um objeto dentro de outro obj 
};
console.log(objeto1.endereco.rua);//para buscar dados do obj endereco tenho que solicitalo.
console.log(objeto1["nome"]);//para busca tambem posso fazer desta forma como se tivesse consultando um array nao iportando o tipo de chave.
console.log(objeto1["1"]);

contatos = [
    {"nome":"carlos", "email":"carlos@exemplo.com"},
    {"nome":"maria", "email":"maria@gmail.com"},
    
]