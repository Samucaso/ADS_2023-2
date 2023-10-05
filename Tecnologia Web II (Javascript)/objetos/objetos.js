//primeira forma de criar um objeto

const pessoa = {
    nome: "Luiz",
    sobrenome: "Otávio"
}

console.log(pessoa['nome'])

//segunda forma de criar um objeto

const pessoa1 = new Object()
pessoa1.nome = 'Luiz'
pessoa1.sobrenome = "Otavio"
pessoa1.falarNome = function(){
    console.log(this.nome)
}

pessoa1.falarNome()

//Terceira forma de criar um objeto

function criarPessoa(nome, sobrenome){
    return {nome, sobrenome}
}

const p1 = criarPessoa("Luiz", "Otavio");

console.log(p1)

////////////////////////////////////////

function novaPessoa(nome, sobrenome, i){
    return {
        nome, 
        sobrenome,
        idade: i,
        get nomeCompleto(){
            return this.nome + " " + this.sobrenome
        }
    }
}

const novap1 = criarPessoa('Lucas', "Silva")
console.log(novap1.nomeCompleto)