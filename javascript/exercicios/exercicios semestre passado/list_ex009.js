//9. Contar Ocorrências de um Valor
let Array=[1,2,2,3,2,4];
let cont
function filtro (parametro){
    //tive a ideia mas fui confirmar no gemini devo aplicar e depois confirmar o resultado.
    return parametro.filter((numero) => numero == 2).length;

}
console.log(filtro(Array))

//outros metodos com forEach
//feito pelo gemini aqui tenho que carregar dois parametros
function filtroContaOcorrencia(lista,valor){
    let contador = 0;
    lista.forEach(function (numero){
        if (numero === valor){
            contador++;
        }
    });
    return contador;
}
console.log(filtroContaOcorrencia(Array,2));

//outro metodo como o reduce este do gemini
let contador = Array.reduce((acumulador, numero) => {
    if (numero === 2) {
        return acumulador + 1;
    } else {
        return acumulador;
    }
}, 0);

console.log(contador);

//vou fazer com arrow e colocar dois parametros que esquecida minha ultima tentativa.
function filtroContaforEchArrow (lista,valor){
    let contador = 0;
    lista.forEach(numero => {
        if(numero == valor)contador++;
    });
    return contador;
}
console.log(filtroContaforEchArrow(Array,2));
