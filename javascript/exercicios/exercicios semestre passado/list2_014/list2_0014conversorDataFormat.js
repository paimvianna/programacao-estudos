/* 14map: Converta um array de datas no formato "YYYY-MM-DD" para "DD/MM/YYYY".
    Exemplo: ["2023-10-05", "2024-01-01"] → ["05/10/2023", "01/01/2024"]*/

    let datas = ["2023-10-05", "2024-01-01", "2001-09-11", "1985-11-24", "1983-11-26", "2011-06-14", "2016-09-12"]
    let dataExplodida = datas.split("-").map(ano, mes, dia)=>({ano:ano, mes})
    console.log(dataExplodida)

    /*function conversorDatasFormat(parametro){

        parametro.map(data =>)
    }*/