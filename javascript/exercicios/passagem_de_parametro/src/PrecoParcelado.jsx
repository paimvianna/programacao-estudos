/*
9. Componente PrecoParcelado

Crie um componente chamado PrecoParcelado que receba:

    precoTotal: valor total da compra.
    parcelas: quantidade de parcelas.

O componente deve calcular o valor de cada parcela dividindo precoTotal 
por parcelas.

O resultado deve ser apresentado no formato R$ X,XX em Nx de R$ Y,YY.
Exemplo de chamada

<PrecoParcelado precoTotal={1200} parcelas={10} />
<PrecoParcelado precoTotal={500} parcelas={4} />

Exemplo de resultado esperado

R$ 1.200,00 em 10x de R$ 120,00

R$ 500,00 em 4x de R$ 125,00
*/
export default function PrecoParcela(props){
    //nao posso aplicar o .toLocaleString em uma constante antes de fazer um calculo.
    const precoTotal = props.precoTotal
    const precoFormatado = precoTotal.toLocaleString('pt-BR',{style:'currency', currency:'BRL'});
    const parcelas = props.parcelas
    const valorParcela = precoTotal / parcelas;
    const parcelaFormatada = valorParcela.toLocaleString('pt-BR',{style:'currency', currency:'BRL'});
    return(
        /*<p>R$ {precoTotal.toFixed(2).replace('.',',')} em {parcelas}x de R$ {valorParcela.toFixed(2).replace('.',',')}</p>*/
        <p> {precoFormatado} em {parcelas}x de  {parcelaFormatada}</p>
        )
}