function chamar3vezes(a,valor1,valor2,valor3)/*aqui estou passando 4 parametros*/{
    a(valor1),//invoco 'a' como função passando o valor do parametro valor1
    a(valor2),//invoco 'a' como função passando o valor do parametro valor2
    a(valor3);//invoco 'a' como função passando o valor do parametro valor3    
};

let soma = function(numero)/*estou usando aqui uma função anonima para fazer um print de uma soma*/{
    console.log(numero + 1)
}

chamar3vezes(soma,1,2,3);

