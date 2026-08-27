import leitor from "readline-sync";
let texto = leitor.question("Digite um valor: ");
console.log("'"+texto+"'");// nesta linha ira imprimir o conteudo de texto
let valor = Number(texto);//aqui imprime o valor apos a conversao
console.log(valor);
//Number.isNaN(valor);
while(Number.isNaN(valor) || texto == "")/*aqui o 'ou' vai compara quando ocorrer um erro*/{
    texto = leitor.question('Numeo invalido, tente novamente: ');
    valor = Number(texto);
}

/*if (valor<0){
    valor = valor*-1;
}*/
//valor = valor<0 ?valor*-1:valor
console.log(valor);
let resultado = (valor = valor<0 ?valor*-1:valo)*2;
console.log(resultado);

/*let positivo = valor<0 ? (valor*-1)*2: valor*2;
console.log(positivo); forma redundante e verboragica*/