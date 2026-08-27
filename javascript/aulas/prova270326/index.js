import {input, select} from '@inquirer/prompts';
import CrudAPI from './CrudAPI.js';
let listaGeneros = await CrudAPI.listaGeneros()
//console.log(listaGeneros); controle pra ver se carrega.
let generos = listaGeneros.map(genero => {
    return {name:genero.nome, value: genero.id}
});

async function listaGeneroPornome(){
    
    let genero = await select({
        message:'Opção: ',
        choices: generos
    });
    return genero
}

async function cadastrarLivro(){
    let titulo;
    let paginas;
    let autor;
    let genero;
    while(!titulo && isNaN(titulo)){
        titulo =await input({message: "Titulo: "});
    }

    while(!paginas && !NaN){
        paginas = await input ({message:"Numero de Paginas: "});
    }

    while(!autor && isNaN(autor)){
        autor =await input({message: "Autor: "});
    }

    genero = await listaGeneroPornome();
    let numeroPaginas =Number(paginas);
    let registro = {titulo:titulo, paginas:numeroPaginas, autor:autor, id_genero:genero}
    let cadastrado = await CrudAPI.criar(registro)
    console.log("Cadastrado com sucesso! ID: "+ cadastrado.id)
}

async function listarLivros() {
    let livros = await CrudAPI.lerTodos();
    console.log(livros)
    livros.forEach(livro => {
        console.log('ID - '+livro.id +' - paginas '+livro.titulo+ ' - autor: '+ livro.autor +' - id_genero: '+livro.id_genero ); 
    });
}

async function buscaPorId(){
    let id;
    while(!id && !NaN){
        id = await input ({message:"ID do livro: "});
    }
    let numero = Number(id);
  
    let lerPorId = await CrudAPI.lerPorId(numero);
    console.log('ID: '+lerPorId.id);
    console.log('Titulo: '+lerPorId.titulo);
    console.log('Paginas: '+lerPorId.paginas);
    console.log('Autor: '+lerPorId.autor);
    let nomeGenero;//variavel que guarda o nome genero.
    generos.forEach(genero=>{
        if(genero.value == lerPorId.id_genero){
            nomeGenero = genero.nome
            console.log('Genero: '+genero.name)
        }
    });
}

async function buscaPorNome(){
    let autor;
    let autorMinusculo;
    let livros;
    let nomeAutor;
    let todosResultado=[];
    while (!autor && isNaN(autor)){
        autor=await input({message: "Informe o Nome do Autor: "});
    }
    autorMinusculo=autor.toLocaleLowerCase();
    
    livros = await CrudAPI.lerTodos();
  
    todosResultado = livros.filter(livro =>{
        nomeAutor =livro.autor.toLocaleLowerCase();
        return nomeAutor.startsWith(autorMinusculo);

    });
    //faço um if onde verifico se o array tem algo. confirmando que houve retorno positivo da busca.;
    if (todosResultado.length>0){
        //console.table(todosResultado);
        todosResultado.forEach(livro => {console.log('ID: '+livro.id+' - paginas '+livro.titulo+ ' - autor: '+ livro.autor +' - id_genero: '+livro.id_genero)});
    }else{
        console.log("Nenhum paciente encontrado.");
    }

}

async function buscaPorGenero(){
    let generos;
    let livros = await CrudAPI.lerTodos();
    console.log('Gêneros disponíveis: ')
    listaGeneros.forEach(genero=>
        console.log(genero.id+ ' - '+ genero.nome)
        );
    /*while (true) {
        entrada = await input({ message: "Informe o ID do Gênero (somente números): " });

        // Validação 1: É um número?
        if (entrada.trim() === "" || isNaN(entrada)) {
            console.log("❌ Erro: Digite um valor numérico válido.");
            continue; // Volta para o início do while
        }

        idEscolhido = Number(entrada);

        // Validação 2: Esse ID de gênero existe no banco?
        generoExiste = listaGeneros.some(g => g.id === idEscolhido);

        if (!generoExiste) {
            console.log("❌ Erro: Esse ID de gênero não consta no sistema.");
        } else {
            break; // Valor é número e existe, pode sair do loop
        }
    }*/
    while(true){

        generos = await input ({message:"Informe o ID do Genero: "});
        if (genero.trim()===" ||")
    }        
    let numero = Number(generos);
    let resultados = livros.filter(livro =>{ 
        return livro.id_genero == numero

    })
    //console.log(resultados) controle
    if(resultados.length>0){
    resultados.forEach(livro =>
        console.log('ID - '+livro.id +' - paginas '+livro.titulo+ ' - autor: '+ livro.autor +' - id_genero: '+livro.id_genero ))
    }else{'\nNenhum livro encontrado para este gênero.'}
   /*livros.forEach(livro =>{ ta errado pq na linha nao satisfaz o criterio ele simplesmente imprime genero inexistente.
    if(livro.id_genero==numero){
                    console.log('ID - '+livro.id +' - paginas '+livro.titulo+ ' - autor: '+ livro.autor +' - id_genero: '+livro.id_genero ); 
    }else{console.log('Genero inexistente.')}
                })*/
             
         
    }

async function lerPagina() {
    let numeroPaginas = await input ({message:'Informe o Numero de paginas: '});
    let livros = CrudAPI.lerPorId
    let maiorNumeroPaginas= livros.find(livro=>{
        livro.paginas>numeroPaginas
}

);
  console.log(maiorNumeroPaginas);  
}
let opcao ="";
while (opcao != "sair"){
    opcao = await select({
    message: 'Opção: ',
    choices:[
        {name:'1 - Cadastrar Livro.', value:'cadastrar'},
        {name:'2 - Listar Todos Livros.', value:'listar'},
        {name:'3 - Buscar Livro Por ID.', value:'buscaId'},
        {name:'4 - Buscar Livro Por Autor.', value:'buscaAutor'},
        {name:'5 - Buscar Livro Por Genero.', value:'buscaGenero'},
        {name:'6 - Listar Todos os Livros (com o nome do genero)', value:'listarComNomeGenero'},
        {name:'7 - Ler Numero de Paginas e Listar com Maior que o Indicado.', value:'lerPaginas'},
        {name:'8 - Listar Quantidades Por Genero', value:'quantidadePorGenero'},
        {name:'9 - Sair',  value:'sair'},
    ]
    });
    switch (opcao) {
        case "cadastrar":
            console.log('Cadastra Livro')
            await cadastrarLivro();
        break

        case "listar":
            console.log('Listar Livros')
            await listarLivros();
        break

        case "buscaId":
            console.log('Buscar por id')
            await buscaPorId();
        break
        
        case "buscaAutor":
            console.log('Buscar por Autor')
            await buscaPorNome();
        break

        case "buscaGenero":
            console.log('Buscar por Genero')
            await buscaPorGenero();
        break

        case "listarComNomeGenero":
            console.log('Listar com o nome do genero.')
            await listarTodosComNomeGenero();
        break

        case "lerPaginas":
            console.log('Listar livros com paginas acima do indicado.')
            await lerPaginas();
        break

        case "quantidadePorGenero":
            console.log('Listar quantidades por Genero.')
            await listarRegistrosProblematicos();
        break

        case "sair":
            //await sair();
            opcao = "sair"
        break
    }
}
console.log(opcao);