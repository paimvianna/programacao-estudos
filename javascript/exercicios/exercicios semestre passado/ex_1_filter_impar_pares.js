//equação para definir numeros pares e impares.

let lista_de_numeros = [1,2,3,4,17,18,20,21,23,25,27];
//let lista_str = ["a","ab","abc","abcd",'ana','bruna']

function filtro_impares(valores){
    return valores.filter(valores => valores % 2 != 0);
}
console.log(filtro_impares(lista_de_numeros));

function filtro_impares(valores){
    return valores.filter (!(valores => valores % 2 != 0));
}
let impar = filtro_impares(valores);
let par = !impar;
console.log(par(lista_de_numeros));

