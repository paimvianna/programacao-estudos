/* map: Converta um array de datas no formato "YYYY-MM-DD" para "DD/MM/YYYY".
    Exemplo: ["2023-10-05", "2024-01-01"] → ["05/10/2023", "01/01/2024"] */

let Exemplo= ["2023-10-05", "2024-01-01"]

function dataOrdenada(array){
    return array.map(data => { 
        const [ano,mes,dia] = data.split("-");
        return dia+"/"+mes+"/"+ano})
}
console.log(dataOrdenada(Exemplo))