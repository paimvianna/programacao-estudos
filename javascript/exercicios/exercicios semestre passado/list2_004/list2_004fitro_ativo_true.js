/*4filter: Filtre objetos de um array onde a propriedade ativo seja true.
    Exemplo: [{ativo: true}, {ativo: false}] → [{ativo: true}*/
    let objetos = [
        {nome:'ze', ativo:'true'},
        {nome:'maria', ativo:'false'},
        {nome:'caca', ativo:'true'}
    ]
    function ativos(parametro){
        let arrayFiltrado = parametro.filter(objeto => objeto.ativo == 'true')
        arrayFiltrado.forEach(objeto => {
            console.log('Nome: '+objeto.nome+', ativo: '+objeto.ativo)
            
        });
    return arrayFiltrado
    }
    ativos(objetos);
    //console.log(ativos(objetos))