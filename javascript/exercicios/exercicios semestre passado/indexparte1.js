console.log(1);

function teste(val1,val2){
    console.log(val1);
    console.log(val2);
    return true;
}

teste(1,2);
teste("a","b");
teste("b","a");
//novo

let h= function(val1){
    console.log("aqui function "+val1);
};
h("exemplo")

let r=(val1) =>{
    console.log("aqui arrow "+val1);
};

r("exempo");

let soma = (a,b) => {
    return a + b;
}

//soma(a,b);

let y = soma(2,4);
console.log(y);
console.log(soma(2,4));
