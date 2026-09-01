let todaLista = [5,8,9,10]
let lista = [5,8,9,10]
let retorno = lista.map(function(elemento, indice,propriaLista){
    return "Novo valor do elemento: "+elemento+" na posição: "+indice;
});
console.log(retorno);

todaLista.forEach(function(tijolo, tv, treco){
        console.log("Elemento: "+tv);
        console.log(tijolo);
        console.log(treco);
});

let total= 0;
todaLista.forEach(function(elemento){
    total=total+elemento;
});
console.log("Total: "+total);
//o filter recebe uma função que retorna um booleno e o 
// filter em si retorna um arry novo so com os verdadeiros da função
let lista2 =[2,5,6,-4,8,31,-2,4,1];
let positivos = lista2.filter(function(valor){
    if (valor>0){
        return true;
    }else{ 
        return false;
    }
});
lista2.filter(function(valor){
    return valor>0?true:false;
});
lista2.filter(valor => valor>0?true:false);
console.log(lista2);
console.log(positivos);
console.log(lista2.filter(a=>a<0));// a função passad para o filter retorna verdaeiro ou falso para o filter.

console.log(lista2.find(a=>a>0));
console.log(lista2.find(a=>a<0));
console.log("some");
console.log(lista2.some(a=>a>0));
console.log(lista2.some(a=>a<0));
console.log(lista2.some(a=>a==0));

console.log("every")
console.log(lista2.every(a=>a>0));
console.log(lista2.every(a=>a<0));
console.log(lista2.every(a=>a!=0));
console.log([].every(a=>a>0));//para listas vazias evitar pq ele procura algo que quebre a regra,
console.log([].every(a=>a<0));// ou seja como nada quebra a regra tudo e verdadeiro.
console.log([].every(a=>a!=0));
console.log([].every(a=>a==0));

console.log("reduce");
//console.log(lista2.reduce(a=>a>0));
let resultado = lista.reduce(function(acumulador, elemento, indice, array){
    return acumulador+elemento;
},0);//o zero e o valor que inicia o acumulador, devo sempre dizer qual e o valor inicial
console.log(resultado);
console.log(lista.reduce((acumulador,valor)=>acumulador*valor,1));//para multiplicações o valor neutro e o 1