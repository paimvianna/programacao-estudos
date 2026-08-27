import leitor from "readline-sync";

console.log("Calculadora");
let valor1 =Number(leitor.question("Valor 1: "));
let valor2 =Number(leitor.question("Valor 2: "));
let operacao = leitor.question("Operação (+,-,*,/): ")
let executar=function(valor1,valor2)
            {
            return "operação invalida!"
            };
if(operacao=="+")/*aqui eu estou declarando a 
função que vou atribuir a executar*/{
    function soma(a,b){
        return a+b;
    }
    executar=soma;
}else if (operacao == "-")/*neste bloco estou at
ribuindo uma função anonima a executar*/{
    executar = function (v1,v2){
        return v1-v2
    }
}else if (operacao =="/"){
    executar = (a,b) =>{
        return a/b;
    }
}else if(operacao=="*"){
    executar = (a,b) => a*b; //se for somente e somente um comando não
    // ou e inrelevante nao precisa de return escrito ou chaves.
    
}


console.log("Executando a operação" + operacao);
let resultado = executar(valor1,valor2);
console.log("resultado:" + resultado)