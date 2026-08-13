//7. Somar Todos os Elementos de um Array usarei o metodo reduce
 let numeros = [1,2,3,4,5,];
 function soma (parametro){
    return parametro.reduce((acumulador,numero) => acumulador + numero);
 }
 console.log(soma(numeros));