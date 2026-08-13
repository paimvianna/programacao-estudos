let lista =[1,2,3,4];

function multiplicacao_por_2(parametro){
return lista.map(function(numero){
    return numero * 2;
});
}
console.log(multiplicacao_por_2(lista));

function multiplicacao_por_2_arrow(parametro){
return lista.map((numero) => numero*2);
}
console.log(multiplicacao_por_2_arrow(lista));