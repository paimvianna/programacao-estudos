/*10. map e filter - Filtrar Palavras com 5 Caracteres e Transformar em Maiúsculas

Dado um array de palavras, crie uma função que filtre as palavras que têm exatamente 5 caracteres e, em seguida, use map para transformar essas palavras em letras maiúsculas.

Entrada: ["maçã", "uva", "banana", "abacaxi", "laranja", "ameixa", "pêra"]

Saída esperada: ["BANANA", "AMEIXA"] OBS: a saída esperada ta errado, pois banana e ameixa tem seis letras. portanto vou colocar com seis letras. */

let Entrada= ["maçã", "uva", "banana", "abacaxi", "laranja", "ameixa", "pêra"];
let maiusculas = Entrada.filter(palavra => palavra.length==6).map(palavra => palavra.toUpperCase());
console.log(maiusculas);