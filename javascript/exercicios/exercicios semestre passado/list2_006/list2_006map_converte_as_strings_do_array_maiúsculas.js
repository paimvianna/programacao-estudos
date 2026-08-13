/*6map: Converta todas as strings de um array para maiúsculas.
    Exemplo: ["hello", "world"] → ["HELLO", "WORLD"]*/
let stringMinuscula = ["hello","world","how","are","you"]

function stringMaiuscula(parametro){
    let palavrao = parametro.map(palavra => palavra.toUpperCase())
    return console.log(palavrao)
}
//console.log(stringMaiuscula(stringMinuscula))
stringMaiuscula(stringMinuscula)