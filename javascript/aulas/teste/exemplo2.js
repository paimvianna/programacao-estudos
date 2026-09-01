import CrudAPI from "./CrudAPI.js";
let novoContato = {nome:'jezer', email:'jezer@exemplo.com'};
let promessa = CrudAPI.criar(novoContato);
console.log('Criando no registro...')
promessa.then(function(contatoBanco){
    console.log('Novo registro criado. Id '+contatoBanco.id);

});
/*Primeira ideia  */