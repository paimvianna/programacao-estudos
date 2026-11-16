// Importa o hook useState para gerenciar os estados do jogo
import { useState } from "react";
// Importa os dois componentes filhos que compõem a interface
import Forca from "./Forca";
import Teclado from "./Teclado";

// Componente principal que gerencia o estado e as regras de vitória/derrota do jogo
export default function JogoDaForca(props) {
    // Garante que a palavra recebida via props esteja em letras maiúsculas para bater com o teclado
    const palavra = props.palavra.toUpperCase();

    // Estado 'letrasTentadas': armazena todas as letras que o jogador já chutou (começa vazio)
    const [letrasTentadas, setLetrasTentadas] = useState([]);
    // Estado 'erros': contabiliza a quantidade de tentativas erradas realizadas (começa em 0)
    const [erros, setErros] = useState(0);
    // Estado 'finalizado': controla se o jogo já terminou por vitória ou derrota (começa em false)
    const [finalizado, setFinalizado] = useState(false);

    // Função disparada toda vez que o usuário clica em uma letra no componente Teclado
    function handleEscolherLetra(letra) {
        // Bloqueia qualquer jogada caso o jogo já tenha sido finalizado ou a letra já tenha sido tentada
        if (finalizado || letrasTentadas.includes(letra)) {
            return;
        }

        // Cria um novo array imutável adicionando a nova letra às letras já tentadas
        const novasTentativas = [...letrasTentadas, letra];
        setLetrasTentadas(novasTentativas);

        // Verifica se a palavra secreta NÃO contém a letra escolhida (erro)
        if (!palavra.includes(letra)) {
            // Incrementa o contador de erros em +1
            const novosErros = erros + 1;
            setErros(novosErros);

            // Regra do enunciado: "Caso o jogador cometa mais de três erros" (> 3, ou seja, 4 erros), finaliza o jogo
            if (novosErros > 3) {
                setFinalizado(true);
            }
        } else {
            // Se acertou a letra, verifica com .every() se TODAS as letras da palavra já foram descobertas
            const acertouTodas = palavra
                .split("")
                .every((l) => novasTentativas.includes(l));

            // Se todas as letras foram descobertas, marca o jogo como finalizado (vitória)
            if (acertouTodas) {
                setFinalizado(true);
            }
        }
    }

    // Variáveis auxiliares calculadas a cada renderização para definir qual mensagem final exibir
    const perdeu = erros > 3;
    const ganhou =
        !perdeu &&
        palavra.split("").every((letra) => letrasTentadas.includes(letra));

    return (
        <div>
            <h1>Jogo da Forca</h1>

            {/* Exibe a quantidade de tentativas erradas realizadas até o momento */}
            <p>Tentativas erradas: {erros}</p>

            {/* Renderiza a palavra secreta com "-" nas letras ocultas */}
            <Forca palavra={palavra} letrasTentadas={letrasTentadas} />

            <br />

            {/* Renderiza o teclado virtual de A a Z */}
            <Teclado
                letrasTentadas={letrasTentadas}
                finalizado={finalizado}
                onEscolherLetra={handleEscolherLetra}
            />

            {/* Mensagens condicionais exibidas apenas quando o jogo é finalizado */}
            {perdeu && <p>Você perdeu!</p>}
            {ganhou && <p>Parabéns! Você ganhou!</p>}
        </div>
    );
}