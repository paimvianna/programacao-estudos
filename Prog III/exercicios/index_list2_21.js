/*reduce: Concatene todas as strings de um array em uma única string.
    Exemplo: ["Hello", " ", "World"] → "Hello World"*/
let Exemplo= ["Hello", " ", "World"," ","lindos."]

function concatena(array){
    return array.reduce((concatena,strg) => concatena + strg,"")
}
console.log(concatena(Exemplo))