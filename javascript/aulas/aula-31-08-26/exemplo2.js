let produtos =[
    {
        nome:"TV",
        valor:2000,
        tipo:"eletro"
    },

    {
        nome:"abacate",
        valor:4,
        tipo:"fruta"
    },

    {
        nome:"batedeira",
        valor:200,
        tipo:"eletro"
    },

    {
        nome:"manga",
        valor:5,
        tipo:"fruta"
    },

    {
        nome:"sabão",
        valor:2,
        tipo:"limpeza"
    }
]

let total = produtos.reduce(function(acumulador,produto){
    return acumulador+produto.valor
},0);
console.log(total);

let eletro= produtos.filter(function(produto){
    if (produto.tipo =="eletro"){
        true;
    }else{
        return false;
    }
});
console.log(eletro);
console.log(produtos.filter(function(produto){
    return produto.tipo=="eletro"
}));
console.log(produtos.filter(produto=>produto.tipo == "eletro"));
let totalEletro = produtos
        .filter(produto=>produto.tipo == "eletro")
        .reduce((acumulador,produto)=>acumulador+produto.valor,0);
console.log(totalEletro);

console.log(produtos.sort(function(produtoA, produtoB){
    return produtoA.valor-produtoB.valor
}));

console.log(produtos.sort(function(produtoA, produtoB){
    return produtoB.valor-produtoA.valor
}));