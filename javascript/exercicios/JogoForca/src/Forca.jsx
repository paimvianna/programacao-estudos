// Componente filho responsável apenas por exibir a palavra oculta/revelada em botões
export default function Forca(props) {
    // Recebe a palavra secreta (ex: "REACT") e o array com as letras já chutadas pelo jogador
    const palavra = props.palavra;
    const letrasTentadas = props.letrasTentadas;

    // Transforma a string da palavra em um array de caracteres para poder usar o .map()
    // Exemplo: "REACT".split("") -> ["R", "E", "A", "C", "T"]
    const letras = palavra.split("");

    return (
        <div>
            {/* Percorre cada letra da palavra e renderiza um botão para ela */}
            {letras.map((letra, index) => (
                <button key={index}>
                    {/* Se a letra já estiver no array letrasTentadas, exibe a letra; senão, exibe "-" */}
                    {letrasTentadas.includes(letra) ? letra : "-"}
                </button>
            ))}
        </div>
    );
}