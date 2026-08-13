/*13map: Calcule o preço total (preço × quantidade) de um array de objetos com preço e quantidade.
    Exemplo:    
    Entrada: [{preco: 5, quantidade: 2}, {preco: 10, quantidade: 3}]
    Saída: [10, 30]*/
    let listaObj = [{preco: 5, quantidade: 2}, {preco: 10, quantidade: 3}, {preco:20, quantidade:5}]

    function calculaValorObj(parametro){
       return console.log(parametro.map((valor)=> valor.preco*valor.quantidade))
    }
    calculaValorObj(listaObj)