/*
1. Componente Alerta

Crie um componente chamado Alerta que receba as seguintes props:

    tipo: uma string que pode receber os valores "erro", "sucesso" ou "aviso".
    texto: uma string contendo a mensagem que deverá ser exibida.

O componente deve verificar o valor da prop tipo e modificar a forma de apresentação da mensagem. Você pode, por exemplo, utilizar uma cor diferente, negrito ou acrescentar uma identificação textual para cada tipo.

O componente pai deve renderizar pelo menos um exemplo de cada tipo de alerta.
Exemplo de chamada

<Alerta tipo="erro" texto="Não foi possível salvar os dados." />
<Alerta tipo="sucesso" texto="Cadastro realizado com sucesso." />
<Alerta tipo="aviso" texto="Existem campos que precisam ser revisados." />

Exemplo de resultado esperado

Erro: Não foi possível salvar os dados.

Sucesso: Cadastro realizado com sucesso.

Aviso: Existem campos que precisam ser revisados.
*/
export default function Alerta(props){
    //aqui estou usando o sistema de teste de tipo para retorno
   /* const corAlerta =()=>{
        if (props.tipo == "sucesso"){
            return"alerta-sucesso";
        }else if(props.tipo == "aviso"){
            return"alerta-falha";
        }else if(props.tipo == "erro"){
            return"alerta-erro";
        }
        return "";
    };
    //retorno do jsx aplicando a classe na tag
    return(
        <p className={corAlerta}> aqui faltou o () se nao uso isso estou referenciando a função.
            {props.texto}
        </p>
    );*/
    return(
        <p className= {`alerta alerta-${props.tipo}`}>
            {props.texto}
        </p>
    );
}