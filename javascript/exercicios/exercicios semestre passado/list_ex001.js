//1. Somar Todos os Elementos de um Array

let lista = [1,2,3,4,5];
//com .reduce
function soma_reduce (lista){
return lista.reduce(function(acumulador,numero){
    return acumulador + numero;
});
}
console.log(soma_reduce(lista));

//usando .reduce com arrow
function soma_reduce_arrow(lista){
return lista.reduce((acumulador,numero) => acumulador + numero);
}
console.log(soma_reduce_arrow(lista));

//usando forEach
function soma_forEach(lista){
let numero1 = 0
lista.forEach(function(numero){
    numero1 = numero1 + numero;
});
return numero1;
}
console.log(soma_forEach(lista))

function soma_forEach_arrow(lista){
let numero1 = 0
lista.forEach(numero => {
    numero1 = numero1 + numero;
});
return numero1;
}
console.log(soma_forEach_arrow(lista))
