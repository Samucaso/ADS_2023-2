const pessoas = [
    {nome: 'Samuel', sobrenome: 'Fernandes'},
    {nome: 'Diogo', sobrenome: 'Boechat'},
    {nome: 'Erick', sobrenome: 'Calazaes'},
    {nome: 'Raphael', sobrenome: 'Antunes'}
]

var novasPessoas = pessoas.map((valor, indice) => {
    let item = {};
    item.nomeCompleto = valor.nome + ' ' + valor.sobrenome;
    item.id = indice
    return item
})

console.log(novasPessoas)