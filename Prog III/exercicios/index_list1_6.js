/*6. Filtrar Palavras Longas

Dado um array de palavras, crie uma função que retorne apenas as palavras que tenham mais de 5 letras.

Entrada: ["maçã", "banana", "abacaxi", "uva"]

Saída esperada: ["banana", "abacaxi"]
*/
let palavras =["maçã", "banana", "abacaxi", "uva"];
let palavrasLongas
let palavrasLongas1=[]
function filtroPalavras(array){
    return array.filter(palavra=>{
        return palavra.length>5
    })
}
console.log(filtroPalavras(palavras))
//palavrasLongas.push(filtroPalavras(palavras))

palavrasLongas = palavras.filter(palavra => {
    return palavra.length>5
})

console.log(palavrasLongas)

//função em arrow function
function filtroPalavrasArrow(array){
    return array.filter(palavra => palavra.length>5)
}
console.log(filtroPalavrasArrow(palavras))

//usando um forEach
palavras.forEach(palavra =>{
    if(palavra.length>5){
        palavrasLongas1.push(palavra);
    }
})
console.log(palavrasLongas1)