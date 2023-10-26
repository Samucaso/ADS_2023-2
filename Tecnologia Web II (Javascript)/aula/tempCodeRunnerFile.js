var lista = ["geladeira", "fogao", "coifa"];

function primeiraLetraMaiuscula(valor){
    return valor.charAt(0).toUpperCase() + valor.slice(1)
}

var listaEmMaiusculo = lista.map(primeiraLetraMaiuscula)

console.log(listaEmMaiusculo)