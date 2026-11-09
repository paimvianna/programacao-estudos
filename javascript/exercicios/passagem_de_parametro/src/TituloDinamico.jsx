/*
11. Componente TituloDinamico

Crie um componente chamado TituloDinamico que receba:

    texto: conteúdo do título.
    nivel: pode receber "h1", "h2" ou "h3".

O componente deve verificar o valor de nivel e renderizar o texto utilizando a tag HTML correspondente.
Exemplo de chamada

<TituloDinamico texto="Título Principal" nivel="h1" />
<TituloDinamico texto="Título Secundário" nivel="h2" />
<TituloDinamico texto="Título Menor" nivel="h3" />

Exemplo de resultado esperado
Título Principal
Título Secundário
Título Menor
*/
export default function TituloDinamico(props){
    const texto = props.texto;
    const Nivel = props.nivel;
    //quando for passar uma props a uma variavel dinamica tem que começa com letra maiuscula como em Nivel
    //tratando como um tag html ou importação de componente tem que ser maiuscula
    return(<>
            <Nivel>{texto}</Nivel><br />
        </>
    )
}