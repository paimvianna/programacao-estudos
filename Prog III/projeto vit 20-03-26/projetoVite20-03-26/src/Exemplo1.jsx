export default function Exemplo1(props){
    console.log(props.cor);
    console.log(props.fonte)
    console.log(props.texto)
    return<>
    <div>
    Essa é um componente exemplo.
    <input disabled={true} type="number" />
    <input type="password" />
    esse é o valor do parametro texto: {props.texto}
    </div>
    </>
}