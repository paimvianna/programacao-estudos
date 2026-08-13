/*2. Multiplicar Cada Elemento por um Valor Específico
Crie uma função que multiplique cada elemento de um array por 2 e imprima o resultado no console.
Entrada: [1, 2, 3, 4]
Saída esperada (no console): 2, 4, 6, 8
OBS: fiz varios console.log para ver e ter controle onde ocorria erro mas no fim o erro estava no for onde eu em vez de colocar length pus de novo valoresArray*/
let valoresArray=[1,2,3,4]
/*
function percorrerLista(valoresArray,funcao){
    let resultadoFuncao = [];
    //console.log(resultadoFuncao+" resultado da função.")
    for(let x=0;x<valoresArray.length;x++){
        //console.log("2")
        let itemArray = valoresArray[x];
        //console.log(valoresArray[x]);
       // console.log(itemArray);

        let itemFuncao = funcao(itemArray);
        //console.log(itemFuncao+" valor do item da função.");
        resultadoFuncao[x] = itemFuncao
    }
    //console.log(resultadoFuncao+"1");
    return resultadoFuncao;
}*/
function multiplicar(itemArray){
    return itemArray*5;
}
function soma(itemArray){
    return itemArray + 5;
}
//agora vou experimentar com duas funções na mesma função basica
function percorrerListaDuasFunções(valoresArray,funcao1,funcao2){
    let resultadoFuncao1 = [];
    let resultadoFuncao2 = [];
    for(let x=0;x<valoresArray.length;x++){
        
        let itemArray = valoresArray[x];
        let itemFuncao1 = funcao1(itemArray);
        let itemFuncao2 = funcao2(itemArray);
        resultadoFuncao1[x] = itemFuncao1 + itemFuncao2;
        resultadoFuncao2[x] = itemFuncao2;
        
    }
    return resultadoFuncao1/*resultadoFuncao2;*/;//nao conseguir ter dois retornos diferentes em uma só function, confirmado so posso fazer um retorno em uma so função.
}

console.log(valoresArray)
//console.log (percorrerLista(valoresArray,multiplicar));
//console.log (percorrerLista(valoresArray,soma));
console.log(percorrerListaDuasFunções(valoresArray,soma,multiplicar));