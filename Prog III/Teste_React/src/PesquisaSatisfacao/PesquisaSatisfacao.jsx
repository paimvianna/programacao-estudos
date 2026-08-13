import {useState} from "react";
import ItemAvaliado from "./itemAvaliado";

export default function PesquisaSatisfacao(props){
    const listaItens = props.listaItens;
    const media = ((ruim*0)+(neutro*3)+(bom*5))/listaItens.length
    console.log(listaItens.length)
    
    return(<>
        <h2>Avaliação</h2>
            {listaItens.map((stringItem, index) => {
                const objetoItem = {
                    id: index,
                    pergunta: stringItem,
                    resposta: null
                };
                return (
                    <div key={objetoItem.id} >
                        <ItemAvaliado
                            id={objetoItem.id}
                            pergunta={objetoItem.pergunta}
                            resposta={objetoItem.resposta}
                        />

                    </div>
                ) 
            })}
        </>)
        

}