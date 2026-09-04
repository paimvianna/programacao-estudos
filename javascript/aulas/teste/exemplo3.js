import CrudAPI from "./CrudAPI.js";

async function criaLista(){
let novoContato = {nome:'jezer', email:"jezer@exemplo.com"};
let promessaCriar = CrudAPI.criar(novoContato);
console.log('continua assincrono');
let contatoBanco = await promessaCriar;
console.log('Agora só vai chegar aqui depois de sincronizar');
console.log('contato criado. id: '+contatoBanco.id);
let clientes = await CrudAPI.lerTodos();

clientes.forEach(cliente => console.log(cliente.nome));
return "OK";
};
console.log("chamei o cria lista");
let retorno = criaLista();
console.log(retorno);
retorno.then(function(resultado){
    console.log(resultado);
});