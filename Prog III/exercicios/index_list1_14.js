/*14. Com esse mesmo array some o valor total do produtos em estoque.

Entrada:

const produtos = [

{ nome: "Notebook", valor: 2500, quantidadeEmEstoque: 10 },

{ nome: "Celular", valor: 1500, quantidadeEmEstoque: 0 },

{ nome: "Monitor", valor: 800, quantidadeEmEstoque: 5 },

{ nome: "Teclado", valor: 100, quantidadeEmEstoque: 0 },

{ nome: "Mouse", valor: 50, quantidadeEmEstoque: 20 }

];

Saída esperada:

[

{ nome: "Notebook", valor: 2500, quantidadeEmEstoque: 10 },

{ nome: "Monitor", valor: 800, quantidadeEmEstoque: 5 },

{ nome: "Mouse", valor: 50, quantidadeEmEstoque: 20 }

]*/
const produtos = [

{ nome: "Notebook", valor: 2500, quantidadeEmEstoque: 10 },

{ nome: "Celular", valor: 1500, quantidadeEmEstoque: 0 },

{ nome: "Monitor", valor: 800, quantidadeEmEstoque: 5 },

{ nome: "Teclado", valor: 100, quantidadeEmEstoque: 0 },

{ nome: "Mouse", valor: 50, quantidadeEmEstoque: 20 }

];
let totalPecasEstoque = produtos.reduce((acumulador, numero) => acumulador + numero.quantidadeEmEstoque,0);//errei de novo nao pus o inicial 0 no reduce, com isso tava dando erro antes.
console.log(totalPecasEstoque);