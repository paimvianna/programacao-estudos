/*
12. Componente FraseIdioma

Crie um componente chamado FraseIdioma que receba:

    textoPortugues: frase em português.
    textoIngles: frase em inglês.
    idiomaAtual: pode receber "pt" ou "en".

Quando idiomaAtual for "pt", deve ser exibido textoPortugues. 
Quando for "en", deve ser exibido textoIngles.
Exemplo de chamada

<FraseIdioma
  textoPortugues="Bem-vindo ao sistema"
  textoIngles="Welcome to the system"
  idiomaAtual="pt"
/>

<FraseIdioma
  textoPortugues="Bem-vindo ao sistema"
  textoIngles="Welcome to the system"
  idiomaAtual="en"
/>

Exemplo de resultado esperado

Bem-vindo ao sistema

Welcome to the system
*/
export default function(props){
    const idiomaAtual = props.idiomaAtual;
    const textoPortugues = props.textoPortugues
    const textoIngles = props.textoIngles
    return(idiomaAtual == "pt"? <p>{textoPortugues}</p>:
            idiomaAtual == "en"? <p>{textoIngles}</p>: 
                <p>Idioma não encontrado.</p>)
}