/*13. Filtrar Produtos em Estoque

Dado um array de objetos que representam produtos (cada produto tem um nome, valor e quantidadeEmEstoque), crie uma função que filtre apenas os produtos que têm quantidade em estoque maior que 0.

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

] */
const produtos = [

{ nome: "Notebook", valor: 2500, quantidadeEmEstoque: 10 },

{ nome: "Celular", valor: 1500, quantidadeEmEstoque: 0 },

{ nome: "Monitor", valor: 800, quantidadeEmEstoque: 5 },

{ nome: "Teclado", valor: 100, quantidadeEmEstoque: 0 },

{ nome: "Mouse", valor: 50, quantidadeEmEstoque: 20 }

];

let estoqueDiferenteDeZero = produtos.filter(produto => produto.quantidadeEmEstoque>0);
console.log(estoqueDiferenteDeZero)
