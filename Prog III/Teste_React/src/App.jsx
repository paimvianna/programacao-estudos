import { useState } from 'react';
import listaItens from "./listaItens";
import PesquisaSatisfacao from "./PesquisaSatisfacao/PesquisaSatisfacao";


function App() {

  return (
    <>
    <PesquisaSatisfacao listaItens={listaItens} /> <br />
    teste
    </>
  )
}

export default App
