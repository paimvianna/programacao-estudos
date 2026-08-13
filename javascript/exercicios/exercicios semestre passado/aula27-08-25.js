//valor e um parmetro da função que neste caso e soma2 que retorna a operação
function soma2(valor){
    return valor + 2;
}

function soma3(valor){
    return valor +3;
}

//
let lista = [2,3,4];
function somaLista(lista,funcao){
    let lista2=[];
    for (let index = 0; index < lista.length; index++) {
        lista2.push(funcao(lista[index]));
    }
    return lista2;
}
console.log(lista)
console.log(somaLista(lista,soma2));
console.log(somaLista(lista,soma3));

//outra função que vai ser usada como parametro aqui estou imprimindo uma str
function concatenaComCasa(valor){
    return "Casa: "+valor;
}
console.log(concatenaComCasa(2));//imprimi o retorno da função que esta como parametro que tem como valor o valor 2
console.log(somaLista(lista,concatenaComCasa));//obj console, chama metodo log para imprimir, onde carrego a função somaLista como parametro onde somaLista tem dois parametros que o primeiro e um array lista e o segundo e a função concatenaComCasa que vai receber lista como valor na função concatenaComCasa.

console.log(somaLista(lista,(valor)=> valor+50));//aqui somaLista vai determinar quantos elementos temos neste array como no anterior e valor sera o que vai estar no index +50 resultando no que deu print se tornoando um arrow tenho que estudar mais isso.

let novaLista= lista.map(soma2); //aatribuo à novaLista o resultado do metodo do obj lista que tem o parametro soma2 que e uma função.
console.log("parte nova"); //aqui vamos ver nos prints a resultante do map e do novaLista
console.log(lista);// temos a lista
console.log(novaLista);//temos o resultado da atribuição de nova lista
console.log([5,6,7,8].map(soma3)); // temos o obj array [5,6,7,8] usando o metodo .map que por ser um metodo pode ter parametros que neste caso tem o parametro e uma function que é soma3 aqui ele esta sendo somente sendo sitado.

//neste caso vamos usar o .map no obj, que tem uma function onde valor que e o parametro function sera a lista. Fazendo  com que a lista se torne uma lista de objetos com um unico atributo.
console.log(["Maria","João","Pedro"].map(
    function(valor){
            let objeto = {nome:valor};
            return objeto
        }
    
));

//agora vou tentar fazer na forma de arrow o mesmo codigo anterior.
console.log(["Maria","João","Pedro"].map( valor =>( {nome : valor})));//aqui nos utilizamos o metodo metodo .map no array. o mesmo vai passar um por um do array assumindo o lugar do valor ou seja na primeira passada Maria assum o lugar de valor e valor e passado para o obj{nome:valor} seria algo assim (Maria => ({nome:Maria})) onde nome seria o parametro do obj que vai ser o primeiro do array de obj que esta sendo produzido.