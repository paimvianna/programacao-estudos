// Importa o hook useState para gerenciar os estados do componente
import { useState } from "react";
// Importa o componente filho responsável por renderizar cada linha de avaliação
import ItemAvaliado from "./ItemAvaliado";
// Importa apenas os ícones ativados para exibir o resultado final conforme a média
import ruimAtivado from './assets/ruimAtivado.png';
import neutroAtivado from './assets/neutroAtivado.png';
import bomAtivado from './assets/bomAtivado.png';

// Componente principal que concentra toda a lógica e os estados da pesquisa
export default function PesquisaSatisfacao(props) {
    // Recebe via props a lista de strings com os nomes dos itens a serem avaliados
    const itens = props.itens;

    // Estado 'avaliacoes': cria um array do mesmo tamanho de 'itens', iniciado todo com null
    const [avaliacoes, setAvaliacoes] = useState(() => itens.map(() => null));
    // Estado 'finalizado': controla se o app está na tela de votação (false) ou de resultado (true)
    const [finalizado, setFinalizado] = useState(false);

    // Atualiza a nota de um item específico sem alterar os demais (imutabilidade)
    function handleAvaliar(indice, nota) {
        // Impede qualquer alteração nas notas caso a pesquisa já tenha sido finalizada
        if (finalizado) {
            return;
        }
        // Percorre o array atual e substitui apenas o valor da posição 'indice' pela nova 'nota'
        setAvaliacoes(
            avaliacoes.map((valorAtual, i) => (i === indice ? nota : valorAtual))
        );
    }

    // Valida se todos os itens foram respondidos antes de encerrar a pesquisa
    function handleFinalizar() {
        // .every() verifica se absolutamente todas as posições são diferentes de null (0 é válido)
        const todosPreenchidos = avaliacoes.every((nota) => nota !== null);
        // Se algum item ainda estiver sem resposta, exibe o alerta obrigatório e interrompe
        if (!todosPreenchidos) {
            alert("Preencha todos os itens");
            return;
        }
        // Caso tudo esteja preenchido, muda o estado para exibir a tela final
        setFinalizado(true);
    }

    // Restaura o estado inicial do aplicativo para realizar uma nova pesquisa
    function handleNovaPesquisa() {
        setAvaliacoes(itens.map(() => null)); // Limpa todas as notas voltando para null
        setFinalizado(false);                 // Retorna para a tela de avaliação
    }

    // Soma todas as notas do array usando .reduce() (trata null como 0 por segurança)
    const soma = avaliacoes.reduce((total, nota) => total + (nota || 0), 0);
    // Calcula a média aritmética dividindo a soma pela quantidade total de itens
    const media = itens.length > 0 ? soma / itens.length : 0;

    // Define o ícone e o texto alternativo padrão para média < 2.0 (Ruim)
    let iconeResultado = ruimAtivado;
    let textoResultado = "Ruim";

    // Atualiza o ícone caso a média atinja os intervalos de Bom (>= 4.0) ou Neutro (>= 2.0 e < 4.0)
    if (media >= 4.0) {
        iconeResultado = bomAtivado;
        textoResultado = "Bom";
    } else if (media >= 2.0) {
        iconeResultado = neutroAtivado;
        textoResultado = "Neutro";
    }

    return (
        <div>
            {/* Renderização condicional: exibe a tela de avaliação enquanto 'finalizado' for false */}
            {!finalizado ? (
                <div>
                    <h1>Pesquisa de Satisfação</h1>
                    {/* Mapeia cada string da lista 'itens' para um componente ItemAvaliado */}
                    {itens.map((item, index) => (
                        <ItemAvaliado
                            key={index}                                        // Chave única exigida pelo React em listas
                            nome={item}                                        // Passa o nome do item atual
                            valor={avaliacoes[index]}                          // Passa a nota atual armazenada para este índice
                            onAvaliar={(nota) => handleAvaliar(index, nota)}   // Passa a função que vincula o índice à nota clicada
                        />
                    ))}
                    {/* Botão que dispara a validação e finalização da pesquisa */}
                    <button onClick={handleFinalizar}>Finalizar</button>
                </div>
            ) : (
                /* Tela exibida quando 'finalizado' passa a ser true */
                <div>
                    <h1>Obrigado por Responder!</h1>
                    {/* .toFixed(2) formata a média obrigatoriamente com duas casas decimais */}
                    <p>Média: {media.toFixed(2)}</p>
                    {/* Exibe a imagem ativada correspondente à faixa da média calculada */}
                    <img src={iconeResultado} alt={textoResultado} />
                    <br />
                    {/* Botão que limpa as respostas e reinicia o fluxo */}
                    <button onClick={handleNovaPesquisa}>Nova Pesquisa</button>
                </div>
            )}
        </div>
    );
}