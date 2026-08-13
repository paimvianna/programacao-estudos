const produtos = [

{ nome: "Notebook", valor: 2500, quantidadeEmEstoque: 10 },

{ nome: "Celular", valor: 1500, quantidadeEmEstoque: 0 },

{ nome: "Monitor", valor: 800, quantidadeEmEstoque: 5 },

{ nome: "Teclado", valor: 100, quantidadeEmEstoque: 0 },

{ nome: "Mouse", valor: 50, quantidadeEmEstoque: 20 }

];
function filtroEstoque(estoque, quantidade){
    return estoque.filter(estoque => estoque.quantidadeEmEstoque > quantidade).reduce((acumlador,numero) => acumlador + numero.valor,0); //coloquei o zero pois ai determino que o numero vai começar com este valor de forma a nao confundir o metodo. 
    
}
let resultado = filtroEstoque(produtos,0)
console.log(resultado)