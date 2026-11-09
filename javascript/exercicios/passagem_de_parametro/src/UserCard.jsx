/*
2. Componente UserCard

Crie um componente chamado UserCard para representar um cartão contendo informações de um usuário.

O componente deve receber as seguintes props:

    nome: nome do usuário.
    idade: idade do usuário.
    cidade: cidade onde o usuário mora.

O componente deve exibir cada informação em uma linha separada. No componente pai, 
renderize manualmente vários componentes UserCard, utilizando informações diferentes em cada um.
Exemplo de chamada

<UserCard nome="Ana" idade={25} cidade="Porto Alegre" />
<UserCard nome="Carlos" idade={31} cidade="Canoas" />

Exemplo de resultado esperado
Ana

Idade: 25 anos

Cidade: Porto Alegre
Carlos

Idade: 31 anos

Cidade: Canoas
*/
export default function UserCard(props){
    return(<div>
        <p>{props.nome}</p>
        <p>Idade: {props.idade} anos</p>
        <p>Cidade: {props.cidade}</p><br />
        </div>
    );
}