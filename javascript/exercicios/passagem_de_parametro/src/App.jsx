import { useState } from 'react'
import Alerta from './Alerta'
import UserCard from './UserCard'
import NotaAluno from './NotaAluno'
import Produto from './Produto'
import Mensagem from './Mensagem'
import StatusUsuario from './StatusUsuario'
import BotaoAcao from './BotaoAcao'
import CaixaTema from './CaixaTema'
import PrecoParcelado from './PrecoParcelado'
import FilmeCard from './FilmeCard'
import TituloDinamico from './TituloDinamico'
import FraseIdioma from './FraseIdioma'
import PlacarJogo from './PlacarJogo'
import ProgressoTarefa from './ProgressoTarefa'
import ResumoFinanceiro from './ResumoFinanceiro'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Alerta tipo = "sucesso" texto = "Cadastro realizado com sucesso."/>      
      <Alerta tipo = "aviso" texto = "Aviso: Existem campos que precisam ser revisados."/>      
      <Alerta tipo = "erro" texto = "Erro: Não foi possível salvar os dados."/> <br />
      <UserCard nome="Ana" idade={25} cidade="Porto Alegre" />
      <UserCard nome="Carlos" idade={31} cidade="Canoas" />
      <NotaAluno nome="Mariana" nota={8.5} />
      <NotaAluno nome="Pedro" nota={5.5} /> <br />
      <Produto nome="Teclado" preco={120} emPromocao={true} />
      <Produto nome="Mouse" preco={80} emPromocao={false} /><br />
      <Mensagem texto="Servidor indisponível." prioridade="alta" />
      <Mensagem texto="Atualização disponível." prioridade="baixa" /><br />
      <StatusUsuario nome="João" status="online" />
      <StatusUsuario nome="Maria" status="offline" />
      <StatusUsuario nome="Lucas" status="ocupado" /><br />
      <BotaoAcao texto="Salvar" desabilitado={false} />
      <BotaoAcao texto="Excluir" desabilitado={true} /><br />
      <CaixaTema tema="claro" conteudo="Conteúdo utilizando o tema " />
      <CaixaTema tema="escuro" conteudo="Conteúdo utilizando o tema " /><br />
      <PrecoParcelado precoTotal={1200} parcelas={10} />
      <PrecoParcelado precoTotal={500} parcelas={4} /><br />
      <FilmeCard titulo="Aventura no Espaço" genero="Aventura" classificacao={10} />
      <FilmeCard titulo="Mistério da Cidade" genero="Suspense" classificacao={16} />
      <TituloDinamico texto="Título Principal" nivel="h1" />
      <TituloDinamico texto="Título Secundário" nivel="h2" />
      <TituloDinamico texto="Título Menor" nivel="h3" />
      <FraseIdioma
          textoPortugues="Bem-vindo ao sistema"
          textoIngles="Welcome to the system"
          idiomaAtual="pt"
        />

        <FraseIdioma
          textoPortugues="Bem-vindo ao sistema"
          textoIngles="Welcome to the system"
          idiomaAtual="en"
        />
        <PlacarJogo
          timeA="Azul"
          timeB="Vermelho"
          pontosA={3}
          pontosB={1}
        />

        <PlacarJogo
          timeA="Verde"
          timeB="Amarelo"
          pontosA={2}
          pontosB={2}
        />
        <ProgressoTarefa nome="Criar interface" porcentagem={40} />
        <ProgressoTarefa nome="Criar banco de dados" porcentagem={100} />
        <ResumoFinanceiro receitas={5000} despesas={3200} />
        <ResumoFinanceiro receitas={3000} despesas={3000} />
        <ResumoFinanceiro receitas={2500} despesas={4000} />
    </>
  )
}

export default App
