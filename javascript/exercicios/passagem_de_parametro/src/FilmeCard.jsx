/*
10. Componente FilmeCard

Crie um componente chamado FilmeCard que receba:

    titulo: título do filme.
    genero: gênero do filme.
    classificacao: idade mínima recomendada.

Se a classificação for menor que 12, o componente deve exibir Livre para a maioria das idades. 
Caso seja maior ou igual a 12, deve exibir Classificação: X anos.
Exemplo de chamada

<FilmeCard titulo="Aventura no Espaço" genero="Aventura" classificacao={10} />
<FilmeCard titulo="Mistério da Cidade" genero="Suspense" classificacao={16} />

Exemplo de resultado esperado
Aventura no Espaço

Gênero: Aventura

Livre para a maioria das idades
Mistério da Cidade

Gênero: Suspense

Classificação: 16 anos
*/
export default function FilmeCard(props){
    const classificacao = props.classificacao;
    const titulo = props.titulo;
    const genero = props.genero;
    return(classificacao <= 12?
        <>
            <p>{titulo}</p>
            <p>Gênero: {genero}</p>
            <p>Livre para a maioria das idades.</p><br />
        </>:<>
            <p>{titulo}</p>
            <p>Gênero: {genero}</p>
            <p>Classificação: {classificacao}</p>
        </>

    )
}