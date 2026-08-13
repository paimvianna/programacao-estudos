function usandoLet(){
    let lista = [4,6,5,3];
    for (let index = 0; index < lista.length; index++) {
        const element = array[index];
        let valorTotal = lista[index] + 10;
        let func=()=>console.log("valor no setTime: "+valorTotal)
        setTimeout(func, 3000);
        console.log("item: "+index);
        console.log(valorTotal);
    }
    console.log("Terminal a função");
}
usandoLet();