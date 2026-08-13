let obj = [
    {nome:'Maria', casado: true},
    {nome:'João', casado: false},
    {nome:'Bruna', casado: true},
    {nome:'Andre', casado: true}
];

let casados = []
let nao_casados = []
for (let index = 0; index < obj.length; index++) {
    let pessoa = obj[index];
    if (pessoa.casado == true){
        casados.push(pessoa);
        //console.log(casados);
    }else if(pessoa.casado == false){
        nao_casados.push(pessoa);
        //console.log(nao_casados);
    }
}
console.log(casados);
console.log(nao_casados);