//10. map e filter - Filtrar Palavras com 5 Caracteres e Transformar em Maiúsculas

let listaStr = ["maçã","uva","banana","abacaxi","laranja","ameixa","pêra","cinco","sexta"];

function filtroMaiuscula(parametro){
//    let palavraFiltrada = parametro.filter((palavra) => palavra.length < 6 && palavra.length > 4);
    let palavraFiltrada = parametro.filter((palavra) => palavra.length == 5);
    let palavraMaiuscula = palavraFiltrada.map(palavra => palavra.toUpperCase());
    return palavraMaiuscula;
}

console.log(filtroMaiuscula(listaStr));


let palavras = ["maçã","banana","abacaxi","uva"]
//usando array com metodo filter.
function FiltroTamanhoPalavra(lista){
    return lista.filter((palavra) => palavra.length > 5);
}
console.log(FiltroTamanhoPalavra(palavras));