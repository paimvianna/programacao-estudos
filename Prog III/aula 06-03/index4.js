let novo = [2,3,4].forEach((valor, indice,lista)=>console.log(indice+":"+valor+" toda a lista:"+lista));//terceiro item ou parametro passa a lista
console.log(novo)
let listanova =[-1,2-510,0].filter((valor)=>{
    if(valor>0){return true}
    else{
        return false
    }
});
console.log(listanova);