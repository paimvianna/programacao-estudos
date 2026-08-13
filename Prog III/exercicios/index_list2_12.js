/*map: Adicione o prefixo "Item: " a cada string de um array.
    Exemplo: ["maçã", "banana"] → ["Item: maçã", "Item: banana"] */
    let Exemplo= ["maçã", "banana", "pera"]
    function prefixo(array){
        return array.map(palavra => "Item: "+ palavra)
    }
    console.log(prefixo(Exemplo));