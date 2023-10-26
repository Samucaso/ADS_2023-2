const numeros = [1, 25, 5, 3, 32, 56, 12]
const numerosDobrados = numeros.map(function(valor, indice){
    return indice
})

console.log(numerosDobrados);

const pessoas = [
    {nome: 'Luiz', idade : 23},
    {nome: 'Samuel', idade : 18},
    {nome: 'Gabi', idade : 17},
    {nome: 'João', idade: 54},
    {nome: 'Lucas', idade: 43},
    {nome: 'Julia', idade: 98}
]

const nomes = pessoas.map(function(valor){
    return valor.nome
})

const pessoasComId = pessoas.map(function(valor, indice){
    valor.id = indice;
    return valor
})

const nomes_v2 = pessoas.map(valor => valor.nome);

const novoObjeto = pessoas.map(function(valor, indice){
    const newObj = {...valor};
    newObj.id = indice
    return newObj
})

console.log(pessoasComId)