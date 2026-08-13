//12. Filtrar Nomes que Começam com uma Letra Específica e Contar Caracteres

let nomes =["Ana", "João", "Amanda", "Carlos", "Alberto"];
let filtro =[];
let nome = 0;
let letras;
function filtraConverteSoma(parametro){
    let filtro =parametro.filter( nome => nome.startsWith("A"))
    let converte = filtro.map(tamanho => tamanho.length)
    let soma = converte.reduce((acumulador, tamanho) => acumulador + tamanho)
    return soma
}
console.log(filtraConverteSoma(nomes))