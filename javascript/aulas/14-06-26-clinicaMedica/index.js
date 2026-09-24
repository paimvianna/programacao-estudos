//import {input, select} from '@inquirer/prompts';
import * as realine from 'node:readline/promises';
import {stdin as input, stdout as output} from 'node:process';
import CrudAPI from './CrudAPI.js';

const leitor = realine.createInterface({input,output});

async function validaNome() {
    let habilitaNome = true;
    while(habilitaNome){
        let nome = await leitor.question('\nInforme o nome do paciente: ')
        if (!nome.trim() || !Number.isNaN(Number(nome))){
            console.log('\nNome deve ser alfabetico, não pode ser vazio ou somente numeros!\n')
        }else{
            habilitaNome = false;
            //console.log(nome);
            return nome;
        }
    }
}

async function validaID() {
    let habilitaID = true;
    while(habilitaID){
        let entrada = await leitor.question('\nInforme o ID: ')
        let id = Number(entrada.trim())
        if (entrada.trim()==='' || !Number.isInteger(id) || id <= 0){
            console.log('\nO ID informado deve ser um numero inteiro e positivo. \n')
        }else{
            habilitaID = false;
            //console.log(id)
            return id;
        }
    }
}

async function validaIdade() {
    let habilitaIdade = true;
    while(habilitaIdade){
        let entrada = await leitor.question('\nInforme o Idade: ');
        let idade = Number(entrada.trim());
        if (entrada.trim()==='' || !Number.isInteger(idade) || Number(idade) <= 0){
            console.log('\nA idade nao pode ser fracionada e deve ser positiva!\n');
        }else{
            habilitaIdade = false;
            //console.log(idade)
            return idade;
        }
    }
}

async function listaEspecialidade() {
    let especialdades = await CrudAPI.listaEspecialidades();
    //console.log(especialdades);
    return especialdades;
}

async function validaEspecialidade() {
    let especialistas = await listaEspecialidade();

    especialistas.map(especialidade => 
        console.log('\nNome da especialidade:'+especialidade.nome+' - Codigo:'+especialidade.id)
    );
    
    let habilitaEspecialidade = true;
    while (habilitaEspecialidade){
        let entrada = await leitor.question('\nInforme o codigo da especialidade desejada: ')
        let especialidade = Number(entrada.trim())
        if (entrada.trim()==='' || !Number.isInteger(especialidade) || especialidade <= 0){
            console.log('\nO codigo do especialista tem que ser um inteiro positivo!\n')
        }else{
            habilitaEspecialidade = false;
            return especialidade;
            }
            
            
        }
        
    }

async function criarConsulta() {
    let nome = await validaNome();
    let idade = await validaIdade();
    console.log('---Lista de Especialidades---')
    let especialidade = await validaEspecialidade();
    let lista = await listaEspecialidade();
    let existe = lista.find( especialistas => especialistas.id === especialidade)
    //console.log(existe)
    if (!existe){
        console.log('Especialidade não encontrada!')
    }else{
        let registro = {paciente:nome, idade:idade, id_especialidade:existe.id};
        
        //console.log(registro)
        let novoCadastro = await CrudAPI.criar(registro);
        console.log('\nCadastro realizado com sucesso, nova ID: '+novoCadastro.id+'\n');
    }
}

async function listarTodasConsultas() {
        let consultas = await CrudAPI.lerTodos()
        //console.log(consultas) ponto de controle para ver o que estou recebendo e se estou recebendo
        consultas.forEach(consulta => 
            console.log(consulta.id+' - '+consulta.paciente+' - idade:'+consulta.idade+' - id_especialidade: '+consulta.id_especialidade));
    }

async function buscaPorId() {
    console.log('---Busca por ID.---')
    let id = await validaID();
    let consultaId = await CrudAPI.lerPorId(id);
    if (!consultaId){
        console.log('Consulta não encontrada!')
        return;
    }
    //console.log(consultaId); imprime o retorno da promessa da busca por ID
    let especialistas = await listaEspecialidade();
    //console.log(especialistas) todos especialista e seus id.
    let nomeEspecialista = especialistas.find(especialista => 
        especialista.id === consultaId.id_especialidade);
    
    let especialistaEncontrado = nomeEspecialista ? nomeEspecialista.nome : 'Não insformado';
    console.log('\nID: '+consultaId.id+' - Nome: '+consultaId.paciente+' - Idade: '+'- Especialidade: '+nomeEspecialista.nome+'\n');
}

async function buscaPorNome() {
    let lista = await CrudAPI.lerTodos()
    let nome = await validaNome();
    let nomeMinusculo = nome.toLocaleLowerCase();
    //a variavel esta como lista minuscula. mas na verdade não altera o nome do objeto.
    let listaMinuscula = lista.filter(nome => {
        let nomePaciente = nome.paciente.toLocaleLowerCase();
        return nomePaciente.startsWith(nomeMinusculo);
    })
    if (listaMinuscula.length===0){
        console.log('Nenhum nome encontrado.');
    }else{
        listaMinuscula.forEach(consulta => 
            console.log('ID: '+consulta.id+' - Nome: '+consulta.paciente+' - Idade: '+consulta.idade+' - Id_Especialidade: '+consulta.id_especialidade));
    }
}

async function buscaPorEspecialidade() {
    console.log('---Lista de Especialidades---')
    let especialidade = await validaEspecialidade();
    let lista = await listaEspecialidade();
    let existe = lista.find( especialistas => especialistas.id === especialidade)
    //console.log(existe)
    if (!existe){
        console.log('Especialidade não encontrada!')
    }else{
        let lerTodos = await CrudAPI.lerTodos();
        lerTodos.forEach(consulta => {
            if(consulta.id_especialidade == especialidade){
                console.log('\nID:'+consulta.id+' - Nome: '+consulta.paciente+' - Idade: ' + consulta.idade+' - Id_escialidade: '+consulta.id_especialidade)
            }
        })
        }
        };

async function listarTodasConsultasEspecialista() {
        let consultas = await CrudAPI.lerTodos()
        //console.log(consultas) ponto de controle para ver o que estou recebendo e se estou recebendo
        let especialistas = await listaEspecialidade()
        consultas.forEach(consulta => {
            especialistas.forEach(especialista => {
                //console.log(consulta.id_especialidade, especialista.id)
                if (consulta.id_especialidade == especialista.id){
                    console.log(consulta.id+' - '+consulta.paciente+' - idade:'+consulta.idade+' - id_especialidade: '+especialista.nome)
                }
            })
            
        
        });
    }

async function menoresDe18() {
    let lista =  await CrudAPI.lerTodos();
    lista.filter(paciente => paciente.idade < 18)
    .forEach(consulta =>
        //tem que usar o acento agudo em caixa alta em outras palavras a crase
        //{console.log(`ID: ${consulta.id} - Nome: ${consulta.paciente} - Idade: ${consulta.idade} - Especialidade: ${consulta.id_especialidade}`)});
        {console.log(`Nome: ${consulta.paciente} (${consulta.idade})`)});

    }

async function registroInconsistencia() {
        let lista = await CrudAPI.lerTodos();
        let pediatria = lista.filter(paciente => 
            paciente.id_especialidade == 101 && paciente.idade >= 18);
        let geriatria = lista.filter(paciente =>
            paciente.id_especialidade == 105 && paciente.idade < 60);
        //pediatria.forEach(paciente => console.log(`ID: ${paciente.id} - Nome: ${paciente.paciente} - Idade: ${paciente.idade} - Especialidade: ${paciente.id_especialidade}`))
        //geriatria.forEach(paciente => console.log(`ID: ${paciente.id} - Nome: ${paciente.paciente} - Idade: ${paciente.idade} - Especialidade: ${paciente.id_especialidade}`))
        let inconsistentes = lista.filter(paciente => 
            paciente.id_especialidade == 101 && paciente.idade >=18 || 
            paciente.id_especialidade == 105 && paciente.idade <=60);
            inconsistentes.forEach(paciente => console.log(`ID: ${paciente.id} - Nome: ${paciente.paciente} - Idade: ${paciente.idade} - Especialidade: ${paciente.id_especialidade}`))
        }

let opcao = '';
while(opcao !== '10'){
        console.log('\n1 - Criar nova consulta.');
        console.log('2 - Listar todas as consultas.');
        console.log('3 - Buscar consulta por ID.');
        console.log('4 - Buscar consulta por Nome.'); 
        console.log('5 - Buscar consulta por Especialidade');
        console.log('6 - Lista todas as consultas (com o nome da especialidade).');
        console.log('7 - Menores de 18 anos.');
        console.log('8 - Registros com problemas(Pediatria/Geriatria).');
        //console.log('9 - Especialidade');
        console.log('9 - Sair');
    
        opcao = await leitor.question('Informe a opção que deseja: ') 

    switch (opcao){
        case '1':
            //console.log('criando nova consulta.')
            await criarConsulta();
        break;
        case '2':
            //console.log('listando todas consultas.');
           await listarTodasConsultas();
        break;
        case '3':
            //console.log('busca consulta por ID.')
            await buscaPorId();
        break;
        case '4':
            //console.log('buscar consulta por nome.')
            await buscaPorNome();
        break;
        case '5':
            await buscaPorEspecialidade();
        break;
        case '6':
            //console.log('lista usando o nome da especialidade em vez do codigo.')
            await listarTodasConsultasEspecialista();
        break;
        case '7':
            console.log('lista menores de 18 anos.')
            await menoresDe18();
        break;
        case '8':
            /*console.log('lista registros que violam as regras:')
            console.log('Pediatra(id 101) - atende apenas menores de 18.')
            console.log('Geriatria(id 105) - atende apenas com 60 ou mais.')
            console.log('Exibir no formato do item 2.')*/
            await registroInconsistencia();
        break;
        case '9':
            console.log('lista as especialidade com codigo ao lado')
            //await
        break;
        case '9':
            console.log('Encerrando o programa...');
           // await
        break;
        default:
            console.log('Opção inválida. Tente novamente');
        break;
}
}
leitor.close()