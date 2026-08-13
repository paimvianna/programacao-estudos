console.log(2>3);
console.log(2<'3');//converte os tipos para comparar
console.log('Carlos'<'Jezer');//leva em conta a ordem alfabetica
console.log('1234'<'24');//compara cada um dos campos individualmente neste caso 1 e maior que 2 sendo este e o segundo campo validador do caso.
console.log("2"==2);//converte e vai dar true
console.log(1==true);//true e 1
console.log(""==0);//false e 0
console.log([]==false);//lista ou array vazio e false
// == ignora o tipo === leva em consideração o tipo
a=""//vazio e zero e zero e false
if (a){
    console.log('entrou no if')

}else{console.log('não entrou no if')}

b=' '//com qualquer coisa e 1 e 1 e true
if (b){
    console.log('entrou no if')
}else{console.log('não entrou no if')}

console.log(2==2 && 3==3);
console.log(4==4 || 2==3);
let lista =[2,3];

let objeto={nome:"jezer"};

if (objeto && objeto.nome){
    console.log(objeto.nome)
}