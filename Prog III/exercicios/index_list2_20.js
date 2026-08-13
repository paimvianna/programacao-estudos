/*reduce: Encontre a string mais longa de um array.
    Exemplo: ["a", "abc", "ab"] → "abc" */
let Exemplo= ["a", "abc", "ab"]

function maiorString(array){
    return array.reduce((maiorPalavra,palavra) => palavra > maiorPalavra? palavra: maiorPalavra, "");
}
console.log(maiorString(Exemplo))