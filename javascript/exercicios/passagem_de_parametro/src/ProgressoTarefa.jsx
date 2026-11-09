/*
14. Componente ProgressoTarefa

Crie um componente chamado ProgressoTarefa que receba:

    nome: nome da tarefa.
    porcentagem: número entre 0 e 100.

Se a porcentagem for igual a 100, o componente deve mostrar Concluída.
 Para valores menores que 100, deve mostrar Em andamento: X%.
Exemplo de chamada

<ProgressoTarefa nome="Criar interface" porcentagem={40} />
<ProgressoTarefa nome="Criar banco de dados" porcentagem={100} />

Exemplo de resultado esperado

Criar interface - Em andamento: 40%

Criar banco de dados - Concluída
*/

export default function ProgressoTarefa(props){
    const nome = props.nome;
    const porcentagem = props.porcentagem;
    const tarefa = porcentagem == 100 ? (
        <p>{nome} - Concluída</p>
    ):(
        <p>{nome} - Em andamento: {porcentagem}%</p>
    )
    return tarefa
}