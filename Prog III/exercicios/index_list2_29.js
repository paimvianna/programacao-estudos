/*find: Encontre o primeiro número que é par e positivo.
    Exemplo: [-4, 3, 8, -2] → 8
     */
let Exemplo= [-4, 3, 8, -2]

function primeiroPar(array){
    return array.find(numero => (numero > 0) && (numero %2 == 0) )
}
console.log(primeiroPar(Exemplo))