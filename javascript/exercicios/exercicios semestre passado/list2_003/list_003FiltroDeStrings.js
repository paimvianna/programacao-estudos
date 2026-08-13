/*Filtre strings com mais de 3 caracteres de um array.
    Exemplo: ["a", "abc", "abcd"] → ["abcd"],
    se eu nao usar o foreach eu tenho que usar o return no do arrayFiltrado*/
let array = ["ana","beto","camila","ze","gi"]
function filtroString(parametro){
    let arrayFiltrado = parametro.filter(palavra=>palavra.length >3);
    arrayFiltrado.forEach(palavraFiltrada => {console.log(palavraFiltrada)
    });
return arrayFiltrado;
}
filtroString(array)