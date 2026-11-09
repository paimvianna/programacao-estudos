/*
8. Componente CaixaTema

Crie um componente chamado CaixaTema que receba:

    tema: pode receber "claro" ou "escuro".
    conteudo: texto apresentado dentro da caixa.

O componente deve alterar sua aparência conforme o tema recebido. 
No tema claro, pode utilizar fundo claro e texto escuro. 
No tema escuro, pode utilizar fundo escuro e texto claro.
Exemplo de chamada

<CaixaTema tema="claro" conteudo="Conteúdo utilizando o tema claro." />
<CaixaTema tema="escuro" conteudo="Conteúdo utilizando o tema escuro." />

Exemplo de resultado esperado

Conteúdo utilizando o tema claro.

Conteúdo utilizando o tema escuro.
*/
export default function CaixaTema(props){
    const tema = props.tema;
    const conteudo = props.conteudo
    const temaFormatado = tema.charAt(0).toUpperCase() + tema.slice(1)
    return(
        <p className={`caixa caixa-${tema}`}>{conteudo}{temaFormatado}.</p>
    );
}