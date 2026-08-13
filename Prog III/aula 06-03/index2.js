let lista=[4,5,6,8];
function percorrer(lista){
    for(let x=0;x<lista.length;x++){
        let item= lista[x];
        //console.log("Valor do item: "+item);
        execucao(item)
    }
}
/*function exibe(item){
    console.log(item)
} posso por este codigo no lugar de exibir*/
//percorrer(lista,exibe);
percorrer(lista,function(item));
percorrer(lista,console.log(item*2));
