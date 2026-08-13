/*map: Dobre os números pares e triplique os números ímpares de um array.
    Exemplo: [1, 2, 3] → [3, 4, 9] */
    let Exemplo= [1, 2, 3,5,6,7,9,10];

    function dobrarParTriplicaImpar(array){
        return array.map(numero => numero%2 ==0 ? numero*2 : numero*3)
    }
    console.log(dobrarParTriplicaImpar(Exemplo))