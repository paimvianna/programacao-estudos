/*map: Converta valores booleanos para 1 (true) ou 0 (false).
Exemplo: [true, false, true] → [1, 0, 1] */
let Exemplo= [true, false, true, 'casa', false]

function conversorBooloeano(array){
    return array.map(dado => dado==true? 1 : (dado == false? 0 :"não booleano"))
}
console.log(conversorBooloeano(Exemplo))