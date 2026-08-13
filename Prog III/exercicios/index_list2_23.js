/*every: Verifique se todas as strings de um array têm pelo menos 1 caractere.
    Exemplo: ["a", "bc", ""] → false */
let Exemplo= ["a", "bc", ""];

function strgMaiorQ1(array){
    return array.every(palavra => palavra.length > 0);
}
console.log(strgMaiorQ1(Exemplo))