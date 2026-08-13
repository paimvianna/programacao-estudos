/*map: Calcule o preço total (preço × quantidade) de um array de objetos com preço e quantidade.
    Exemplo:
    Entrada: [{preco: 5, quantidade: 2}, {preco: 10, quantidade: 3}]
    Saída: [10, 30] */
    let Entrada= [{preco: 5, quantidade: 2}, {preco: 10, quantidade: 3}];

    function precoTotalObjeto(array){
        return array.map(valor => (valor.preco) * (valor.quantidade))
    }
    console.log(precoTotalObjeto(Entrada))