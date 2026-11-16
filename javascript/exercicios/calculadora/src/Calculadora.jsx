/*
Crie uma calculadora em React usando botões e eventos de onClick, 
com as 4 operações básicas, um botão "=" para resolver a equação
 e um botão "C" para limpar os valores, conforme a imagem abaixo.

Imagem da calculador

Dica:

Para resolver operações matemáticas, pode-se utilizar o comando eval* 
do JavaScript:

https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/eval

* O comando eval deve ser usado com muito cuidado, pois pode gerar falhas de segurança na aplicação.

*/
import { useState } from "react";

export default function Calculadora(props){
    const[visor, setVisor] = useState("")

    function DadosVisor(parametro){
        setVisor(visor + parametro)
    }
    function ResultadoConta(){
        setVisor(eval(visor))
    }
    function LimparVisor(parametro){
        setVisor("")
    }
    return(<div>
                <table style={{tableLayout:"fixed",borderCollapse:"collapse",
                                fontFamily:"Arial, sans-serif",
                                width:"200px",
                                height:"50px",
                                overflow:"auto",
                                border:"2px solid"}}>
                    <thead>
                        <tr style={{border: "1px solid #cccccc",
                                    padding: "8px", textAlign:"right"}}>
                            <th colSpan ={4} style={{fontWeight:"bold"}}>
                                <input style={{textAlign:"right", width: "100%", boxSizing: "border-box" }}
                                        type="text" value={visor} readOnly/>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <button onClick={()=>DadosVisor(7)}>7</button>
                            </td>
                            <td>
                                <button onClick={()=>DadosVisor(8)}>8</button>
                            </td>
                            <td>
                                <button onClick={()=>DadosVisor(9)}>9</button>
                            </td>
                            <td>
                                <button onClick={()=>DadosVisor("/")}>/</button>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <button onClick={()=>DadosVisor(4)}>4</button>
                            </td>
                            <td>
                                <button onClick={()=>DadosVisor(5)}>5</button>
                            </td>
                            <td>
                                <button onClick={()=>DadosVisor(6)}>6</button>
                            </td>
                            <td>
                                <button onClick={()=>DadosVisor("*")}>X</button>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <button onClick={()=>DadosVisor(1)}>1</button>
                            </td>
                            <td>
                                <button onClick={()=>DadosVisor(2)}>2</button>
                            </td>
                            <td>
                                <button onClick={()=>DadosVisor(3)}>3</button>
                            </td>
                            <td>
                                <button onClick={()=>DadosVisor("-")}>-</button>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <button onClick={LimparVisor}>C</button>
                            </td>
                            <td>
                                <button onClick={()=>DadosVisor(0)}>0</button>
                            </td>
                            <td>
                                <button onClick={ResultadoConta}>=</button>
                            </td>
                            <td>
                                <button onClick={()=>DadosVisor("+")}>+</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
    </div>
        
    )
}