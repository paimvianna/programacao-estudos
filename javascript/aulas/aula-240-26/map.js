let lista =[2,4,7,5];

console.log(lista.map(valor=>"texto: "+valor));
console.log(lista.map(valor=>[valor,valor+2,valor+3]))
console.log(lista.map(valor=>0));
//array de objetos
console.log(lista.map(valor=>({
    valor:valor,
    negativo:valor*-1,
    vezes100:valor*100
})));
let pessoas = [
    {nome:"Jezer", email:"jezer@aaa"},
    {nome:"Carlos", email:"calos@exemplo"},
    {nome:"Maria", email:"maria@exemplo"}
];

console.log(pessoas.map(pessoa=>pessoa.nome+" - "+pessoa.email));
