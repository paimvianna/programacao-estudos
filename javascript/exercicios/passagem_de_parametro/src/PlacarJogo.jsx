/*
13. Componente PlacarJogo

Crie um componente chamado PlacarJogo que receba:

    timeA: nome do primeiro time.
    timeB: nome do segundo time.
    pontosA: pontuação do primeiro time.
    pontosB: pontuação do segundo time.

O componente deve comparar os pontos e informar qual time está vencendo. Caso os valores sejam iguais, deve informar que o jogo está empatado.
Exemplo de chamada

<PlacarJogo
  timeA="Azul"
  timeB="Vermelho"
  pontosA={3}
  pontosB={1}
/>

<PlacarJogo
  timeA="Verde"
  timeB="Amarelo"
  pontosA={2}
  pontosB={2}
/>

Exemplo de resultado esperado

Azul: 3

Vermelho: 1

Azul está vencendo.

Verde: 2

Amarelo: 2

Empate.
*/
export default function PlacarJogo(props){
    const timeA = props.timeA;
    const timeB = props.timeB;
    const pontosA = props.pontosA
    const pontosB = props.pontosB
    /* este esta com excesso de linha pq não e preciso mudar a ordem de time A e B
    abixo vai um codigo mais limpo
    return (pontosA>pontosB?<div>
                <p>{timeA}: {pontosA}</p>
                <p>{timeB}: {pontosB}</p>
                <p>{timeA} está vencendo.</p>
                </div>:
                    pontosB > pontosA?<div>
                    <p>{timeB}: {pontosB}</p>
                    <p>{timeA}: {pontosA}</p>
                    <p>{timeB} está vencendo.</p>
                    </div>:
                        <div>
                        <p>{timeB}: {pontosB}</p>
                        <p>{timeA}: {pontosA}</p>
                        <p>Empate.</p>
                        </div>

    )*/
   return(
        <div>
            <p>{timeA}: {pontosA}</p>
            <p>{timeB}: {pontosB}</p>
            {pontosA > pontosB ? (
                <p>{timeA} está vencendo.</p>
            ): pontosB > pontosA?(
                <p>{timeB} está vencendo.</p>
            ):(
                <p>Empate.</p>
            )}
        </div>
    
   ) 
}