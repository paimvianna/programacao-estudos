/*
filter: Crie uma função que retorne um array com números primos de um array.
Exemplo: [2, 3, 4, 5, 6] → [2, 3, 5]
 */
let Exemplo= [2, 3, 4, 5, 6];
function ehPrimos(numero){
    if (numero<=1)
         return false;
    for(let i=2 ; i< numero; i++){
            if(numero%i===0){
                return false;
            }
        }
    return true;
};
function primos(array){
    return array.filter(ehPrimos)
}

console.log(primos(Exemplo));
let numeros = primos(Exemplo);
console.log(numeros)