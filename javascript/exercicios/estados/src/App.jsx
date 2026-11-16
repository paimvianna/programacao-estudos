import { useState } from 'react'
import Mostra_Esconder from './Mostra_Esconder'
import AlterarTema from './AlteraTema'
import ControleVolume from './AumentarDiminuirVolume'
import ProximaCor from './SemaforoProximaCor'
import BloqueioBotao from './CliqueUmaVez'
import LampadaPotenciometro from './LampadaPotenciometro'
import Desconto from './Loja'
import PlayerSimples from './PlayerSimples'
import ModoAlerta from './AlternarModoAviso'
import SistemaAlerta from './TelaSucessoErroAviso'
function App() {
  //const[count, setCount] = useState(0)
  return(
    <>
    <h1>Teste</h1>
    
    <Mostra_Esconder/> <br />
    <AlterarTema texto = "O tema vai variar junto com o botão. "/> <br />
    <ControleVolume/><br />
    <ProximaCor/> <br />
    <BloqueioBotao/><br />
    <LampadaPotenciometro/><br />
    <Desconto nome = "Teclado" preco = {100} desconto = {10}/> <br />
    <PlayerSimples musica = "Bet Balanço"/> <br />
    <ModoAlerta texto = "Texto para teste da mudança."/><br/>
    <SistemaAlerta 
      textoerro = "Erro: Ocorreu um erro no sistema." 
      textosucesso = "Sucesso: A operação foi bem sucedida."
      textoaviso = "Aviso: Existe pendencias na operação."/> <br />   
    </> 
  )
}

export default App
