// Componente filho responsável por renderizar o teclado virtual com as letras do alfabeto
export default function Teclado(props) {
    // Recebe a lista de letras já clicadas, o status de fim de jogo e a função de clique do pai
    const letrasTentadas = props.letrasTentadas;
    const finalizado = props.finalizado;
    const onEscolherLetra = props.onEscolherLetra;

    // Cria um array com as 26 letras do alfabeto usando .split("")
    const alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");

    return (
        <div>
            {/* Renderiza um botão para cada letra do alfabeto */}
            {alfabeto.map((letra) => {
                // Verifica se essa letra já foi selecionada anteriormente pelo jogador
                const jaClicada = letrasTentadas.includes(letra);

                return (
                    <button
                        key={letra}                               // Usa a própria letra como chave única
                        onClick={() => onEscolherLetra(letra)}    // Envia a letra clicada para o componente pai
                        disabled={jaClicada || finalizado}        // Desabilita o botão se a letra já foi usada ou se o jogo acabou
                    >
                        {letra}
                    </button>
                );
            })}
        </div>
    );
}