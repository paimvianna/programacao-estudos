/*
3.Componentes de Estado no JogoMemoria:

    Gerenciar a lógica do jogo da memória, controlar o estado das cartas, processar as interações do usuário e exibir o layout completo do jogo.
    O componente inicializa dois conjuntos de cartas idênticas (A e B) e as embaralha separadamente.
    Use o estado para gerenciar as seguintes informações:
        As cartas atualmente selecionadas (uma de cada conjunto).
        A quantidade de tentativas restantes (começando em 5).
        Um indicador de erro que sinaliza se o jogador errou a tentativa de combinação.
 */
import { useState } from "react";
import Carta from "./Carta";

const baralho = [
    {id:1, nome:"1", selecionada:false, achada:false},
    {id:2, nome:"2", selecionada:false, achada:false},
    {id:3, nome:"3", selecionada:false, achada:false},
    {id:4, nome:"4", selecionada:false, achada:false},
    {id:5, nome:"5", selecionada:false, achada:false}
]
export default function JogoMemoria(){
    const [baralhoA, setBaralhoA] = useState (()=>Embaralhar(baralho));
    const [baralhoB, setBaralhoB] = useState (()=>Embaralhar(baralho));
    const [selecionadaA, setSelecionadaA] = useState(null)
    const [selecionadaB, setSelecionadaB] = useState(null)
    const [tentativa, setTentativa] = useState(5)
    const [erro, setErro] = useState(false)

    function Embaralhar(baralhoOriginal){
        return baralhoOriginal
            .map(carta => ({...carta}))//metodo de copia usando map// outro metodo baralhoB = [...baralho];
            .sort(()=>Math.random()-0.5);//posso usar o .sort() com a função dentro ()=>math.random() - 0.5 para embaralhar
    }
    function SelecionarCarta(carta,conjunto){
        if (erro || tentativa === 0){
                return;
        }
        console.log(carta.selecionada);
        console.log(conjunto, carta.nome)
        console.log(baralhoA);
        console.log(baralhoB);
        
        let novaA = selecionadaA;
        let novaB = selecionadaB;
        if(conjunto ==="A" && selecionadaA === null){
            setSelecionadaA(carta)
            novaA = carta
        }
        if(conjunto ==="B" && selecionadaB === null){
            setSelecionadaB(carta)
            novaB = carta
        }
        if (novaA!=null && novaB!=null && novaA.id === novaB.id){
            setBaralhoA(baralhoA.map((carta)=> novaA.id === carta.id ? ({...carta, achada : true, selecionada: false}):(carta)))
            setBaralhoB(baralhoB.map((carta)=> novaB.id === carta.id ? ({...carta, achada : true, selecionada: false}):(carta)))
            setSelecionadaA(null)
            setSelecionadaB(null)
        }else if(novaA != null && novaB != null){
            setTentativa(tentativa - 1)
            setErro(true)            
        }
    }
    function TentarNovamente(){
        setSelecionadaA(null);
        setSelecionadaB(null);
        setErro(false);
    }
    
    const venceu = baralhoA.every((carta) => carta.achada);

    return(<>
        {baralhoA.map((carta) => <Carta onSelecionar={()=>SelecionarCarta(carta,"A")} 
            key={carta.id} nome={carta.nome} 
            selecionada = {selecionadaA !== null && (selecionadaA.id ===carta.id)} 
            achada = {carta.achada}/>)} <br />
        {baralhoB.map((carta) => <Carta onSelecionar={()=>SelecionarCarta(carta,"B")}
            key={carta.id} nome={carta.nome}
            selecionada = {selecionadaB !== null && (selecionadaB.id ===carta.id)} 
            achada = {carta.achada}/>)} <br />
        {erro && tentativa > 0 && (
            <div>
                <p>Você errou! Tentativas restantes: {tentativa}</p>
                <button onClick={TentarNovamente}>Tentar Novamente</button>
            </div>
        )}
        {venceu && <p>Você Venceu!</p>}
        {tentativa === 0 && !venceu && <p>Você perdeu.</p>}
        </>)
}