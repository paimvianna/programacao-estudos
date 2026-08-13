/* 1. Somar Todos os Elementos de um Array
Crie uma função que some todos os números de um array usando o método forEach.
Entrada: [1, 2, 3, 4, 5]
Saída esperada: 15*/
let valoresArray = [1,2,3,4,5];
let resultadoSoma = 0;//declarei a variavel global aqui para usar o o arrow functio a baixo

valoresArray.forEach((valor)=> resultadoSoma += valor);

function soma(valoresArray)/*para fazer este codigo eu precisei declarar dentro do proprio escopo da função soma uma variavel de acumulo neste caso valor*/{
    let valor = 0;
    for(let x=0;x<valoresArray.length;x++){
        valor += valoresArray[x];
    }
    return valor;
}

console.log(valoresArray);
console.log(soma(valoresArray));
console.log(resultadoSoma);