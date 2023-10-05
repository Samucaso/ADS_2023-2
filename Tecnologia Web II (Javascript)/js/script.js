var custo = 0;
const bebida = prompt('Qual bebida gostaria? (café, chá ou chocolate quente?)').toLowerCase();

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
    default :
    alert("Essa opção não temos");
};

const leite = prompt("Gostaria de adicionar leite?");
if(leite == 'sim'){
    custo += 0.5;
}
const acucar = prompt("Gostaria de adicionar açúcar?");
if(acucar == 'sim'){
    custo += 0.25;
}
const chantilly = prompt("Gostaria de adicionar chantilly?");
if(chantilly == 'sim'){
    custo++;
}

alert(`O preço final é ${custo}`);