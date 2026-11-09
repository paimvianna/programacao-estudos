/*3. Componente NotaAluno

Crie um componente chamado NotaAluno que receba as props nome e nota.

Se a nota for maior ou igual a 7, o componente deve exibir Aprovado. 
Caso contrário, deve exibir Reprovado.

incluindo pelo menos um aluno aprovado e um reprovado.
Exemplo de chamada

<NotaAluno nome="Mariana" nota={8.5} />
<NotaAluno nome="Pedro" nota={5.5} />

Exemplo de resultado esperado

Mariana - Nota: 8.5 - Aprovado

Pedro - Nota: 5.5 - Reprovado */

export default function NotaAluno(props){
     /*
     return(props.nota>=7?
        <div>
            <p>{props.nome} - Nota: {props.nota} - Aprovado</p>
        </div>:<div>
            <p>{props.nome} - Nota: {props.nota} - Reprovado</p>
        </div>
    ); 
    */
   //codigo otimizado
   const status = props.nota >= 7 ? "Aprovado" : "Reprovado";
   return(
    <p>{props.nome} - Nota: {props.nota} - {status}</p>
   )
}