/*4. Criar um Array de Strings de Saudação

Dado um array de nomes, crie uma função que retorne um array de saudações personalizadas, por exemplo: "Olá, João!".

Entrada: ["João", "Maria", "Pedro"]

Saída esperada: ["Olá, João!", "Olá, Maria!", "Olá, Pedro!"]*/
//function anonima.

let nomes = ["João", "Maria", "Pedro"];
let saudacaoComMap = nomes.map(function(nome){
    return "Olá, "+nome+"!"
});
//arrow function
let saudacaoArrow = nome => "Olá, "+nome+"!";
//aqui eu só coloco na primeira parte ou nome da lista.
console.log(saudacaoArrow(nomes))

//com este vou percorrer todos os elemento e imprimir um por linha
nomes.forEach(nome =>{
    console.log("Olá, "+nome+"!")
});
//não fica pleno mas dependendo da pra usar pois o join so coloca no fim do elemento o separador, e não posso colocar mais que um elemento neste caso somente pude por "Olá, "
console.log(nomes.join(" Olá, "))
//impressão de array sem formatação.
console.log(saudacaoComMap)
//impressão  do array com join transfomando em uma string
console.log(saudacaoComMap.join(" "))
//impressão dos elementos da string sem tratamento.
console.log(...saudacaoComMap)