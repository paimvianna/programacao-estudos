//6. Filtrar Palavras Longas
let palavras = ["maçã","banana","abacaxi","uva"]
//usando array com metodo filter.
function FiltroTamanhoPalavra(lista){
return lista.filter((palavra) => palavra.length > 5);
}
console.log(FiltroTamanhoPalavra(palavras));