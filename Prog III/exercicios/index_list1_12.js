/*12. Filtrar Nomes que Começam com uma Letra Específica e Contar Caracteres

Dado um array de nomes, use filter para obter apenas os nomes que começam com a letra "A", depois use map para transformar esses nomes em suas respectivas quantidades de caracteres, e finalmente use reduce para somar todas as quantidades de caracteres.

Entrada: ["Ana", "João", "Amanda", "Carlos", "Alberto"]

Saída esperada: 16 // (Ana (3) + Amanda (6) + Alberto (7) = 16) */
let Entrada= ["Ana", "João", "Amanda", "Carlos", "Alberto"];
/*let saidaEsperada = Entrada.filter(palavra => palavra.toLowerCase().startsWith("a")).map(tamanhoPalavra => tamanhoPalavra+ "("+tamanhoPalavra.length+")")//aqui tenho que usar o "" + para concatenar o () pois perto de uma palavra ele acredita ser uma função, posso usar a mesma palavra para definir a passagem nos array ate o momento usei palavra e tamanhoPalvra pois cada arrow function fica clara.
Entrada.filter(palavra => palavra.toLowerCase().startsWith("a")).reduce((acumulador,numero) => acumulador+numero.length,0);
console.log(Entrada.filter(palavra => palavra.toLowerCase().startsWith("a")).reduce((acumulador,numero) => acumulador+numero.length,0), saidaEsperada);

console.log(Entrada.filter(palavra => palavra.toLowerCase().startsWith("a")).reduce((acumulador,numero) => acumulador+numero.length,0),"// ("+ saidaEsperada[0] + " + "+saidaEsperada[1]+" + "+saidaEsperada[2]+")");*/
//abaixo fiz o codigo baseado nas observações do gemini, pois fiz o codigo acima e apresentei pra ele. Utilizei o join que ajudou bastante.
let filtroNome = Entrada.filter(palavra => palavra.toLowerCase().startsWith('a'));
let formatoApresentacao = filtroNome.map(palavra => `${palavra} (${palavra.length})`);
let somaTamanhoNomes = filtroNome.reduce((acumulador, nome) => acumulador + nome.length,0);//nunca esquecer de colocar o valor inicial.
console.log(filtroNome)
console.log(formatoApresentacao)

console.log(`${somaTamanhoNomes}// (${formatoApresentacao.join("+")} = ${somaTamanhoNomes})`)
