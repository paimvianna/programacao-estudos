/*
15. Componente ResumoFinanceiro

Crie um componente chamado ResumoFinanceiro que receba:

    receitas: valor total das receitas.
    despesas: valor total das despesas.

O componente deve calcular o saldo subtraindo as despesas das receitas:

saldo = receitas - despesas

Após realizar o cálculo:

    Se o saldo for maior que zero, mostrar Saldo positivo: R$ X,XX.
    Se o saldo for igual a zero, mostrar Saldo zerado.
    Se o saldo for menor que zero, mostrar Saldo negativo: R$ X,XX.

O componente pai deve testar as três situações: saldo positivo, saldo zerado e saldo negativo.
Exemplo de chamada

<ResumoFinanceiro receitas={5000} despesas={3200} />
<ResumoFinanceiro receitas={3000} despesas={3000} />
<ResumoFinanceiro receitas={2500} despesas={4000} />

Exemplo de resultado esperado

Saldo positivo: R$ 1.800,00

Saldo zerado

Saldo negativo: R$ -1.500,00

*/
export default function ResumoFinanceiro(props){
    const despesas = props.despesas;
    const receitas = props.receitas;
    const saldo = receitas - despesas;
    /*
    neste formato o sinal negativo fica antes do R$
    const saldoFormatado = saldo.toLocaleString('pt-BR',{style:'currency', currency:'BRL'});
    */
    const saldoFormatado = Math.abs(saldo).toLocaleString('pt-BR',{
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
    return saldo > 0 ?(
        <p>Saldo positivo: R$ {saldoFormatado}</p>
    ):(saldo < 0 ? (<p>Saldo negativo: R$ -{saldoFormatado}</p>):(<p>Saldo zerado.</p>));    
}