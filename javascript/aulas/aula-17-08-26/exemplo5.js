function teste(){
    console.log("Chamei a função");
}
teste();
teste();//aqui esta evocando a função.
teste;//aqui esta somente referenciado

function teste2(a){
    console.log(a+2);
}
teste2(4);
teste2(8);

function teste3(a,b){
    console.log(a+b);
    if (a<0){

    }
}
teste3(2,5);
teste3(9,7);
let retorno = teste3(9,7);

console.log(retorno)// para ter algo em retorno tenho que ter um return 

function teste4(valor){
    while(true)
        
}