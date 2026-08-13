/* map: Crie um array de strings HTML com tags <li> para cada elemento de um array.
    Exemplo: ["Pão", "Leite"] → ["<li>Pão</li>", "<li>Leite</li>"] */
    let Exemplo= ["Pão", "Leite"]

    function stringHtml(array){
       //return array.map(palavra => `<li>${palavra}<li>`)
       return array.map(palavra => "<li>"+palavra+"<li>")
       
    }
console.log(stringHtml(Exemplo))