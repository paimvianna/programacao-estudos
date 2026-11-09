/*6. Componente StatusUsuario

Crie um componente chamado StatusUsuario que receba:

    nome: nome do usuário.
    status: pode receber "online", "offline" ou "ocupado".

O componente deve mostrar o nome do usuário e seu status atual. 
Os diferentes estados devem ser apresentados de forma distinta, 
podendo ser utilizadas cores, negrito ou outras propriedades de estilo.
Exemplo de chamada

<StatusUsuario nome="João" status="online" />
<StatusUsuario nome="Maria" status="offline" />
<StatusUsuario nome="Lucas" status="ocupado" />

Exemplo de resultado esperado

João - Online

Maria - Offline

Lucas - Ocupado
 */
export default function(props){
    const status = props.status;
    const nome = props.nome;

    /*metodo mais verboragico fiz sozinho.
    return(
        status == "online"?
        <p className={`status-${status}`}>{nome} - Online</p> : 
            status == "offline"?
            <p className={`status-${status}`}>{nome} - Offline</p> :
                <p className={`status-${status}`}>{nome} - Ocupado</p>
    )
    */
    //metodo onde no uso ternario e faço uma concatenação de status apos a quebra ou corte dele
    // Função simples para colocar a primeira letra em maiúscula (ex: "online" -> "Online")
    const statusFormatado = status.charAt(0).toUpperCase()+status.slice(1);
    /*acima eu pego status e seleciono a primeira letra com chartAt(0) que aplico um UpperCase que
    deixa maiuscula concateno com '+' com o resto de estatus a partir do indice 1*/
    return(
        <p>
            {nome} - <span className={`status-${status}`}>{statusFormatado}</span>
        </p>
    );
}