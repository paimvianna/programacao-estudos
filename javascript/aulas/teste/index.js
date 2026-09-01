import CrudAPI from "./CrudAPI.js";
let promessa = CrudAPI.lerTodos();//aqui e uma promessa da API
promessa.then(function(retornoDaPromessa)/*o then vai ser o que faremos com o retorno da solicitação*/{
    console.log('retorno da promessa.')
    console.log(retornoDaPromessa)// aqui e o retorno da promeça e atribuido ao parametro para ser impresso.
    retornoDaPromessa.forEach(contato =>console.log(contato.nome));
    console.log(retornoDaPromessa);

});
console.log("contatos");
console.log(promessa);
console.log("Código Executado")
