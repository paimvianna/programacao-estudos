// Importa as imagens dos ícones (versões ativada e desativada) da pasta assets
import ruimAtivado from './assets/ruimAtivado.png';
import ruimDesativado from './assets/ruimDesativado.png';
import neutroAtivado from './assets/neutroAtivado.png';
import neutroDesativado from './assets/neutroDesativado.png';
import bomAtivado from './assets/bomAtivado.png';
import bomDesativado from './assets/bomDesativado.png';

// Componente filho sem estado próprio (stateless): apenas exibe dados e avisa cliques ao pai
export default function ItemAvaliado(props) {
    // Extrai as propriedades recebidas do componente pai (PesquisaSatisfacao)
    const nome = props.nome;           // Texto com o nome do critério avaliado (ex: "Atendimento")
    const valor = props.valor;         // Nota atual selecionada para este item (null, 0, 3 ou 5)
    const onAvaliar = props.onAvaliar; // Função callback que envia a nota clicada para o pai

    return (
        <div>
            {/* Exibe o nome do item que está sendo avaliado */}
            <p>{nome}</p>

            {/* Botão "Ruim" (valor 0): ao clicar, chama onAvaliar passando 0 */}
            <button onClick={() => onAvaliar(0)}>
                {/* Ternário: se valor for estritamente 0, mostra o ícone ativado; senão, o desativado */}
                <img src={valor === 0 ? ruimAtivado : ruimDesativado} alt="Ruim" />
            </button>

            {/* Botão "Neutro" (valor 3): ao clicar, chama onAvaliar passando 3 */}
            <button onClick={() => onAvaliar(3)}>
                {/* Ternário: se valor for estritamente 3, mostra o ícone ativado; senão, o desativado */}
                <img src={valor === 3 ? neutroAtivado : neutroDesativado} alt="Neutro" />
            </button>

            {/* Botão "Bom" (valor 5): ao clicar, chama onAvaliar passando 5 */}
            <button onClick={() => onAvaliar(5)}>
                {/* Ternário: se valor for estritamente 5, mostra o ícone ativado; senão, o desativado */}
                <img src={valor === 5 ? bomAtivado : bomDesativado} alt="Bom" />
            </button>
        </div>
    );
}