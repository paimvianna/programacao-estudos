/*find: Encontre a primeira string que começa com a letra "a" (case insensitive).
    Exemplo: ["Apple", "banana", "Orange"] → "banana"
     */
let Exemplo= ["Apple", "banana", "Orange"];

function primeiroComLetraa(array){
    return array.find(palavra => palavra.toLowerCase().startsWith("a"))
}
console.log(primeiroComLetraa(Exemplo))