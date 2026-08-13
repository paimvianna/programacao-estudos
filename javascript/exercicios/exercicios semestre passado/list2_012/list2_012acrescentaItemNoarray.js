/*list2_012map: Adicione o prefixo "Item: " a cada string de um array.
    Exemplo: ["maçã", "banana"] → ["Item: maçã", "Item: banana"]*/

let listaStr = ["maçã", "banana", "laranja","ovo"]

function listaItens(parametro){
    let listaAtualizada = parametro.map(itens => "Item: "+ itens)
    return console.log(listaAtualizada)
}
listaItens(listaStr)