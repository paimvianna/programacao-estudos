/*map: Dobre os valores dos números pares de um array (deixe os ímpares inalterados).
    Exemplo: [1, 2, 3] → [1, 4, 3] */
let Exemplo= [1, 2, 3, 5, 6, 7, 8, 9, 10, 11];

function dobrarPar(array){
    return array.map(numero => numero%2==0? numero*2 : numero)
}
console.log(dobrarPar(Exemplo))