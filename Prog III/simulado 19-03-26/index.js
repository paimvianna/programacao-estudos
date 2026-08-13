import {input, select} from '@inquirer/prompts';
import  CruAPI from './CrudAPI.js';
let listaEspecialidades = await CruAPI.listaEspecialidades();
let especialidades = listaEspecialidades.map(especialidade => {
    return{name:especialidade.nome, value:especialidade.id}
});
/*let especialidadesNome = especialidades.filter(especialidade =>{
    especialidade.value == paciente.id_especialidade;
    return especialidade.nome
});*/

async function listaEspecialidade(){
    /*let especialidades =await CruAPI.listaEspecialidades();
    especialidades.forEach(especialidade =>{
        console.log(especialidade.nome+" - "+especialidade.id)
    })
    especialidades.map(especialidade => {
    return{name:especialidade.nome, value:especialidade.id}
   });*/
   let especialidade = await select({
        message: 'Opção: ',
        choices: especialidades
   });
   return especialidade
}

async function cadastrarPessoa(){
    let nome;
    let numeroIdade;
    let especialidade;
    while(!nome && isNaN(nome)){
        nome =await input({message: "Nome: "});
    }

    while(!numeroIdade && !NaN){
        numeroIdade = await input ({message:"Idade: "});
    }

    /*while(!especialidade){
        especialidade = await input({message:"Especialidade: "});
    }*/
    especialidade = await listaEspecialidade();
    let idade =Number(numeroIdade);
    let pessoa = {paciente:nome, idade:idade, id_especialidade:especialidade}
    let cadastrado = await CruAPI.criar(pessoa)
    console.log("Cadastrado com sucesso! ID: "+ cadastrado.id)
}

async function listarTodos(){
    let todos = await CruAPI.lerTodos();
    todos.forEach(pessoa => {
        console.log("ID: "+pessoa.id, typeof pessoa.id + " - Nome: " + pessoa.paciente + " - Idade: "+ pessoa.idade+" - Id_especialidade: "+pessoa.id_especialidade)        
    });
}

async function buscaPorId(){
    let id;
    while(!id && !NaN){
        id = await input ({message:"Id: "});
    }
    let num = Number(id);
    //console.log(num);
    let lerPorId = await CruAPI.lerPorId(num);
    console.log('ID: '+lerPorId.id);
    console.log('Nome: '+lerPorId.paciente);
    console.log('Idade: '+lerPorId.idade);

    console.log('Especialidade: '+lerPorId.id_especialidade);
}

async function buscaPorNome(){
    let nome;
    let nomeMinusculo;
    let todos;
    let nomepaciente;
    let todosResultado=[];
    while (!nome && isNaN(nome)){
        nome=await input({message: "Informe o Nome para a busca: "});
    }
    nomeMinusculo=nome.toLocaleLowerCase();
    
    todos = await CruAPI.lerTodos();
    /*
    todosResultado= todos.filter(function(paciente){
        return paciente.paciente.toLocaleLowerCase()===nomeMinusculo
    });*/
    todosResultado = todos.filter(paciente =>{
        nomepaciente =paciente.paciente.toLocaleLowerCase();
        return nomepaciente.startsWith(nomeMinusculo);

    });
    console.log(todosResultado);
    if (todosResultado.length>0){
        console.table(todosResultado);
        todosResultado.forEach(pessoa => {console.log('ID: '+pessoa.id+' - Nome: '+pessoa.paciente+' - Idade: '+pessoa.idade+' - id_especialidade: '+pessoa.id_especialidade)});
    }else{
        console.log("Nenhum paciente encontrado.");
    }
    //console.log(todosResultado)
}

async function buscaPorEspecialidade(){
    console.log("Informe a Especialidade para a busca: ");
    let idEspecialidade = await listaEspecialidade();
    console.log(idEspecialidade);
    let todos = await CruAPI.lerTodos();
    let todosResultados = todos.filter(paciente =>{
    return  paciente.id_especialidade == idEspecialidade;
    //let todosResultados = []
    /*todosResultados = todos.filter(paciente =>{
    return  paciente.id_especialidade == idEspecialidade.value;*/

    });
    //console.log(todosResultados);
    if (todosResultados.length>0){
        console.log(todosResultados)
        console.table(todosResultados);
        todosResultados.forEach(pessoa =>{console.log('ID: '+pessoa.id+' - Nome: '+pessoa.paciente+' - Idade: '+pessoa.idade+' - id_especialidade: '+pessoa.id_especialidade)});

    }else{
        console.log("Nenhuma consulta encontrada.");
    }
    //console.log(todosResultado)
}

async function listarTodosComNomeEspecialidade(){
    let todos = await CruAPI.lerTodos();
    todos.forEach(paciente => {
        // Para cada pessoa, buscamos no array 'especialidades' 
        // aquele que tem o ID igual ao id_especialidade do paciente
        let especialidadeEncontrada = especialidades.find(especialidade => {
            console.log(especialidade.value);
            console.log(paciente.id_especialidade);
            especialidade.value == paciente.id_especialidade
        });
        console.log(especialidadeEncontrada)
        let nomeDaEspecialidade = especialidadeEncontrada ? especialidadeEncontrada.name: "Especialidade não encontrada";
        //outra forma de imprimir
        //console.log('ID: ${paciente.id} - Nome: ${paciente.paciente} - Idade: ${paciente.idade} - Especialidade: ${nomeDaEspecialidade}');
         console.log('ID: '+paciente.id+ '- Nome: '+paciente.paciente+' - Idade: '+paciente.idade+ '- Especialidade: '+nomeDaEspecialidade);
    });
}

async function quebraNome(nome){
    let quebra = nome.split(" ");
    if(quebra.length <=1){
        return nome;
    }
    let sobrenome = quebra[quebra.nome.length -1];
    let nomePrimeiro = quebra[0];
    return sobrenome +", "+nomePrimeiro;
}

async function listarTodosSobrenome(){
    let todos = await CruAPI.lerTodos();
    todos.forEach(pessoa => console.log(quebraNome(pessoa.nome)))
}

let opcao ="";
while (opcao != "sair"){
    opcao = await select({
    message: 'Opção: ',
    choices:[
        {name:'Criar Nova Consulta.', value:'cadastrar'},
        {name:'Listar Todas as Consultas.', value:'listar'},
        {name:'Buscar Consulta Por ID.', value:'buscaId'},
        {name:'Buscar Por Nome do Paciente', value:'buscaNome'},
        {name:'Buscar Consulta Por Especialidade', value:'buscaEspecialidade'},
        {name:'Listar Todas as Consultas (com o nome da especialidade)', value:'listarComNomeEspecialidade'},
        {name:'Menores de Idade', value:'buscarMenoresDe18'},
        {name:'Registros com Problemas(Pediatria/Geriatria)', value:'registroProblematicos'},
        {name:'Especialidades', value:'especialistas'},
        {name:'Sair',  value:'sair'},
    ]
    });
    switch (opcao) {
        case "cadastrar":
            //console.log('criar consulta')
            await cadastrarPessoa();
        break

        case "listar":
            //console.log('listar')
            await listarTodos();
        break

        case "buscaId":
            console.log('buscar por id')
            await buscaPorId();
        break
        
        case "buscaNome":
            console.log('buscar por Nome')
            await buscaPorNome();
        break

        case "buscaEspecialidade":
            console.log('buscar por Especialidade')
            await buscaPorEspecialidade();
        break

        case "listarComNomeEspecialidade":
            console.log('buscar por lista com o nome da especialidade')
            await listarTodosComNomeEspecialidade();
        break

        case "buscarMenoreDe18":
            console.log('busca menores de 18')
            await buscarMenoresDe18();
        break

        case "registroProblematicos":
            console.log('busca registros com problemas')
            await listarRegistrosProblematicos();

        /*case "sobrenome":
            await listarTodosSobrenome();
        break*/

        case "especialistas":
            //console.log('especialistas')
            await listaEspecialidade();
        break

        case "sair":
            //await sair();
            opcao = "sair"
        break
    }
}
console.log(opcao);