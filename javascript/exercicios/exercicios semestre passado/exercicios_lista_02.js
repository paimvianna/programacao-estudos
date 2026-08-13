
//equação para definir os numeros primos.

for (let c = 0; c < x.length; c++) {
    let a = 0
    for (let b = 1; b <= x[c]; b++) {
        if(x[c] % b == 0){
            a++;
        }
    }
    if(a == 2){
            w.push(x[c]);
        }
}
console.log(w);

//filtro de array para tamanho de str
for (let c = 0; c < lista_str.length; c++) {
    let palavra = lista_str[c];
    if(palavra.length > 3){
        filtro_str.push(palavra)
    }
}
console.log(filtro_str)

//filtro com ativação de sistema .filter com arrow.
let numerosGrandes = x.filter(function(elemento_lista) { 
    return elemento_lista > 10;    
});
console.log(x); //imprime o array x
console.log(numerosGrandes) //imprime o elementos que satisfazem o filtro
