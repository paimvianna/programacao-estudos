export default function ListaQuestoes(props){
    console.log(props)
    return<>
        <table border={1}>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>PERGUNTA</th>
                    <th>RESPOSTA</th>
                    <th>Justificativa</th>
                    <th>OPÇÕES</th>
                </tr>
            </thead>
            <tbody>
                {props.listaPerguntas.map((pergunta) => <tr>
                    <td>{pergunta.id}</td>
                    <td>{pergunta.pergunta}</td>
                    <td>{pergunta.resposta?"sim":"não"}</td>
                    <td>{pergunta.justificativa}</td>
                    <td><span>✏️</span><span>🪦</span></td>
                </tr>)}
            </tbody>
        </table>
    </>
}