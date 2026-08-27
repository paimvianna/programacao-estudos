let valor1 = 10;
function soma(valor, valor2)/*aqui o parametro nao substitui o valor da variavel valor1 ou valor pois ela e global.*/{
    let valor1 = valor //neste caso estou criando uma variavel dentro do escopo da função.
    let total = valor1+valor2;
    return valor1+valor2
}
console.log(soma(5,5));
console.log(soma(20 ,5));
//console.log(total);