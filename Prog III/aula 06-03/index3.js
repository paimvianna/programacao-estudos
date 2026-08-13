listaantiga =[3,6,8,0,9];
function mapear(listaantiga,funcao){
    let novalista=[];
    for(let x=0;x<listaantiga.length; x++){
        let itemantigo=listaantiga[x];
        //let itemnovo=itemantigo*10;
        let itemnovo=funcao(itemantigo)
        novalista[x]=itemnovo;
    }
    return novalista;//ele sempre finaliza a execução
}
console.log(listaantiga);
//console.log(mapear(listaantiga))
console.log(mapear(listaantiga,function(itemantigo){return itemantigo*5}));
console.log(mapear(listaantiga,(valorantigo)=>valorantigo*20));