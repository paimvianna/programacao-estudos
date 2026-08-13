import input_teclado from "readline-sync"

function ler_numero(parametro_funcao){
    let numeroInvalido = true;
    let a;
    while(numeroInvalido){
        a = input_teclado.question(parametro_funcao);
        if (a != '' && !isNaN(a)){
            numeroInvalido = false;
        }else{
            console.error('Valor informado não e um numero.');
        }
    }
    return Number(a);
}
let numero_de_valores_para_somar = ler_numero('informe a quantidade de numeros que deseja somar: ')
console.log(numero_de_valores_para_somar)
let total = 0;
/*function calculo(){
for (let valor = 1; valor <= numero_de_valores_para_somar; valor++) {
    let numero = ler_numero("Informe o "+ valor +"° numero que vai somar: ");
    console.log(numero);
    total += numero;
    console.log(total);
}return total
}*/
for (let valor = 1; valor <= numero_de_valores_para_somar; valor++) {
    let numero = ler_numero("Informe o "+ valor +"° numero que vai somar: ");
    console.log(numero);
    total += numero;
    
}
console.log(total);
//let resultado = calculo()
//console.log(resultado)