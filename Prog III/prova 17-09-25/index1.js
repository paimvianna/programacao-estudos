import { input, select} from "@inquirer/prompts";
import CrudAPI from "./CrudAPI.js";
// nao entendi pq nao esta chamando
async function listaEspecialidade() {
    let listaEspecialista = await CrudAPI.listaEspecialidades();
    let especialidade = listaEspecialista.map((especialista)=> {
        return {name:especialista.nome, value: especialista.id}})//vou mudar de string para normal.
    let especialistaID = await select({
    message: 'Opção: ',
    choices: especialidade
});
return especialistaID
}

//criar consulta nao esta funcionando.
async function criarConsulta(){
    let nome;
    let idade;
    let escolhaEspecialidade;
    //tenho que melhorar a validação de nome
    while(!nome){
        nome = await input({message:"Nome do paciente: "});

    }
    //tenho que melhorar a validação de idade
    while(!idade){
        idade = await input({message:"Idade do paciente: "});
    }
    escolhaEspecialidade = await listaEspecialidade();
    let registro = {paciente:nome,idade:idade,id_especialidade:escolhaEspecialidade}
    let novoRegistro = await CrudAPI.criar(registro);
    console.log("Cadastro realizado com sucesso, ID: " + novoRegistro.id)
}

//tenho que fazer uma conversao em busca por id_especialista para o nome.
async function buscarPorId() {
    let id;
     id = await input({message:"ID para exibir: "});
     let numeroId = Number(id);

    if(numeroId != "" && numeroId != NaN){
       let resultadoBuscaId = await CrudAPI.lerPorId(numeroId);
       console.log("ID: "+resultadoBuscaId.id)
       console.log("Nome: "+resultadoBuscaId.paciente)
       console.log("Idade: "+resultadoBuscaId.idade)
       console.log("Especialidade: "+resultadoBuscaId.id_especialidade)
    }else{
        console.log("Consulta não encontrada!")
    }
}
async function buscarNomePaciente() {
    let nome = await input({message:"Paciente: "});
    let listaPaciente = await CrudAPI.lerTodos();
    listaPaciente.forEach((paciente) => {
        if(paciente.paciente == nome){
    console.log(paciente.id+" - "+paciente.paciente+" - Idade: "+paciente.idade+" - Id-especialista "+paciente.id_especialidade);   
    }     
    });
    
}


async function listarTodasConsultas() {
    let todasConsultas = await CrudAPI.lerTodos();
    todasConsultas.forEach((paciente) => {
    console.log(paciente.id+"-"+paciente.paciente+"-"+paciente.idade+"-"+paciente.id_especialidade+"-"+typeof paciente.id_especialidade) ;        
    });
}

async function buscarMenores() {
    let listaPaciente = await CrudAPI.lerTodos();
    listaPaciente.forEach((paciente) => {
        if(paciente.idade < 18){
    console.log(paciente.id+" - "+paciente.paciente+" - Idade: "+paciente.idade+" - Id-especialista "+paciente.id_especialidade);   
    }     
    });
    
}


async function listarTodasConsultasNomeEspecialidade() {
    let todasConsultas = await CrudAPI.lerTodos();
    todasConsultas.forEach(paciente => {
    console.log(paciente.id+"-"+paciente.paciente+"-"+paciente.idade+"-"+paciente.id_especialidade);        
    });
}

async function buscarEspecialista() {
    let especialidade = await listaEspecialidade();
    let especialista = await 
    let todasConsultas = await CrudAPI.lerTodos()
    let consultaEspecialidade = todasConsultas.filter(paciente => paciente.id_especialidade == especialidade)
    console.log(especialidade)
    console.log(consultaEspecialidade)
    consultaEspecialidade.forEach((paciente) => console.log(paciente.id+"-"+paciente.paciente+"-"+paciente.idade+"-"+paciente.id_especialidade))
}
let opcao = "";
while (opcao != "sair"){
    opcao = await select({
    message: 'Opção: ',
    choices:[
        {name:'Criar nova consulta', value:'criar nova consulta'},
        {name:'Listar todas as Consultas', value:'Listar todas as Consultas'},
        {name:'Buscar consulta por ID', value:'Buscar consulta por ID'},
        {name:'Buscar consulta por Nome do Paciente', value:'Buscar consulta por Nome do Paciente'},
        {name:'Buscar por Especialidade', value:'Buscar por Especialidade'},
        {name:'Menores de Idade', value:'Menores de Idade'},
        {name:'Listar todas as Consultas (com nome da especialidade)', value:'Listar todas as Consultas (com nome da especialidade)'},
        {name:'Registros com Problemas(PEdiatria/Geriatria', value:'Registros com Problemas(PEdiatria/Geriatria'},
        {name:'sair', value:'sair'},
    ]});
    switch(opcao){
         case "criar nova consulta": // so vi agora as 22:24 que estava em maiuscula Criar.
            await criarConsulta();
        break
        case "Listar todas as Consultas":
            await listarTodasConsultas();
        break
        case "Buscar consulta por ID":
            await buscarPorId();
        break
        case "Buscar consulta por Nome do Paciente":
            await buscarNomePaciente();
        break
        case "Buscar por Especialidade":
            await buscarEspecialista();
        break
        case "Listar todas as Consultas (com nome da especialidade)":
            await listarTodasConsultasNomeEspecialidade();
        break
        case "Menores de Idade":
            await buscarMenores();
        break
        case "Registros com Problemas(PEdiatria/Geriatria)":
            await buscarRgistrosProblema();
        break
    }
}
console.log(opcao)
