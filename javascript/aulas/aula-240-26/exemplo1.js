/*tres criterios para: nome, parametro, e bloco codigo;
 sendo que a mesma pode ser anonima sem nome como uma expressão */
function a(){
    console.log("teste a");
}

let b = a;
console.log(a);
console.log(b);

function executa3Vezes(algo){
    algo();
    algo();
    algo();
}
executa3Vezes(b)
/*na função 3 vezes e obrigatorio que 
seja uma função pq a mesma e evocada/executada/chamada 
podemos passar funções como parametros */

/*tudo que retorna um valor e uma expressao no caso constante */

let c = 2+2
console.log(typeof(c));

c="casa"
console.log(typeof(c));

c=function(){console.log("azul"); return "aa"};//aqui estou passado para "c" a função.
console.log(typeof(c));

let d = c(); //estou passando o resultado da 
//execução da função que no caso e o retorno da função anonima.

//arrow function

c =() => {console.log("casa"); return "ss" }

