const date = new Date();

switch(date.getDay()){
    case 0:
        console.log("Hoje é final de semana");
        break;
    case 6:
        console.log("Hoje é final de semana");
        break;
    default:
        console.log("Hoje é dia útil");
}