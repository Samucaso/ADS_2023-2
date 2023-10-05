//Terceira forma de criar um objeto
function criarPessoa(nome, sobrenome){
    return {nome, sobrenome}
}

const p1 = criarPessoa("Luiz", "Otavio");

console.log(p1)