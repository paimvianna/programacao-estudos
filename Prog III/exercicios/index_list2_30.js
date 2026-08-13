/*Encadeamento: Filtre números positivos, mapeie para seus quadrados e some-os.
    Exemplo: [-2, 3, 4] → 3² + 4² = 25
     */
let Exemplo= [-2, 3, 4]// → 3² + 4² = 25
    
function positivosSomaQuadrados(array){
    return array
    .filter(numero => numero>0)
    .map(numero =>numero ** 2)
    .reduce((soma, atual) => soma + atual, 0);
}
console.log(positivosSomaQuadrados(Exemplo))