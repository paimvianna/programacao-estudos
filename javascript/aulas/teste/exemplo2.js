import CrudAPI from "./CrudAPI.js";
let novoContato = {nome:'jezer', email:'jezer@exemplo.com'};
let promessa = CrudAPI.criar(novoContato);
console.log('Criando no registro...')
promessa.then(function(contatoBanco){
    console.log('Novo registro criado. Id '+contatoBanco.id);
    let promessaLista = CrudAPI.lerTodos()
    promessaLista.then(function(contatos){
        console.log('Lista Contatos:')
        contatos.forEach(contato => {
            console.log(console.id + " " + contato.nome);
            
        });
    //caso for preciso fazer nova inserção se coloca o digo de solicitação aqui dentro, 
    });

});
