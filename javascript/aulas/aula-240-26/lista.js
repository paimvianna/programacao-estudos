//faça uma função que receba uma lista (array)
//e retorne uma nova lista com os seu valores
//ultiplicado por dois.
let lista = [2,4,6,5];

/*function exercicio1(lista,operarElemento){
    let novaLista = [];
    for (let i=0; i<lista.length;i++){
        let novaVariavel = operarElemento(lista[i]);
        novaLista.push(novaVariavel);
    }
    return novaLista;
}*/
console.log(exercicio1(lista))

//faça uma função que receba uma lista(array)
//e retorne uma lista com seus elementos 
//dividos por 2

// reutilizando codigos
function mapeiaLista (lista, funcao){
    let novaLista =[];
    for (let i=0; i <lista;i++){
        let novaVariavel = funcao(lista[indice]);
        novaLista.push(novaVariavel)
    }
    return novaLista;
}

//ex1
function exercicio1(lista){
    function soma(elemento){
        return elemento*2
    }
}


//ex2
function exercicio2 (lista){
    return mapeiaLista(lista,function(val){
        return val/2;
    })
}

//ex3 
function exercicio3 (lista){
    return mapeiaLista(lista, (elemento)=>{return elemento-2});
}

//ex4
/*function exercicio4(lista){
    return mapeiaLista(lista, (elemento) => elemento+2);
}*/
function exercicio4(lista){
    console.log(lista.length);
    let novaLista=lista.map(function(elemento){
        return elemento+2
    })
    return novaLista;
}
// abaixo tenho uma função anonima que tem o parametro lista, 
// que e uma arrow function que e um map da lista. 
// que recebe uma função arrow function tambem com parametro valor e 
// função que soma parametro valor +5
let exercicio6 = (lista) => lista.map(valor=>valor+5);//nesta linha temos uma função passada para o map com apenas 1 parametro que e valor neste caso.
console.log(exercicio6(lista));