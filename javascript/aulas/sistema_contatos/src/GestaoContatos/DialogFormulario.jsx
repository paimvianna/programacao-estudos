export default function DialogFormulario(props){
    function enviar(formData){
        let nome = formData.get("nome");
        let email = formData.get("email");
        console.log(`form foi enviado:${nome} - ${email}`);
        let novoContato = {
            nome : nome,
            email: email
        };
        props.onEnviar(novoContato)
    }

    return <dialog open>
        <form action = {enviar}>
            <label>Nome: <input name = "nome" required/></label>
            <br />
            <br />
            <label>E-mail: <input name = "email" type="email" required/></label>
            <br />
            <br />
            <button type="submit">Cadastrar</button>
            <button type="button" onClick={props.onFechar}>Cancelar</button>
        </form>
    </dialog>
}
/*
<button type="button" onClick={props.onFechar}>Cancelar</button>
*/