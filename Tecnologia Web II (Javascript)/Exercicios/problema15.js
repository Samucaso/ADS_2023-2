var custo = 0;
console.log('Qual bebida gostaria?')
var bebida = 'cafe';
console.log(bebida)

switch(bebida){
    case 'cafe':
        custo += 2;
        break;
    case 'cha':
        custo += 1.5;
        break;
    case 'chocolate quente':
        custo += 2.5;
        break;
};

console.log("Gostaria de adicionar leite?");
leite = "sim"
console.log(leite)
    if(leite == 'sim'){
        custo += 0.5
    }
console.log("Gostaria de adicionar açúcar?");
acucar = "sim"
console.log(acucar)
    if(acucar == 'sim'){
        custo += 0.25
    }
console.log("Gostaria de adicionar chantilly?");
chantilly = "nao"
console.log(chantilly)
    if(chantilly == 'sim'){
        custo++
    }

console.log("o custo final é " + custo)