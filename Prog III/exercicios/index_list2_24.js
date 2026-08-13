/*every: Verifique se todos os objetos de um array possuem a propriedade id.
    Exemplo: [{id: 1}, {id: 2}] → true */
let Exemplo= [{id: 1}, {id: ""}];

/*function verificaId(array){
    return array.every(numero => numero.id !== undefined);//aqui verifico se o id existe mesmo sendo um campo vazio.
}*/
function verificaId(array){
    return array.every(numero => numero.id === 'number');//aqui verifico se o id existe aceitando somente se for um numero..
}
console.log(verificaId(Exemplo));