export default function Tabela(props){
    console.log(props);

    return<>
    <table border={1}>
        <thead>
            <tr>
                <td>ID</td>
                <td>Nome</td>
                <td>E-mail</td>
            </tr>
        </thead>
        <tbody>
        {props.contatos.map((contato)=><tr>
            <td>{contato.id}</td>
            <td>{contato.nome}</td>
            <td>{contato.email}</td>
            </tr>)}
    </tbody>
    </table>
    
    </>
}