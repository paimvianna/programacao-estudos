export function exibeValor(valor){
    if(valor>0){
        console.log(valor);
    }else{
        console.log("sem valor") ;   }
}
//exibeValor(1)
//console.log("executou aqui"); uma boa pratica e nao fazer funções em bibliotecas. mais aconselhavel fazer para constantes e objetos
export function contaArray(lista){
    console.log("Tamanho: "+ lista.lentgh);

}
export const PI =3.1415;
//export const pessoaExemplo;