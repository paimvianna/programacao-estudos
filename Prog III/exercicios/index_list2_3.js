/*filter: Filtre strings com mais de 3 caracteres de um array.
    Exemplo: ["a", "abc", "abcd"] → ["abcd"] */
let Exemplo= ["a", "abc", "abcd","abcdef"]

function palavraMaiorQ3(array){
    let palavrao = array.filter(palavra => palavra.length > 3)
    return palavrao

}
console.log(palavraMaiorQ3(Exemplo))