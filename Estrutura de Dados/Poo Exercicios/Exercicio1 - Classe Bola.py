# criação da classe Bola
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

# mudei o valor do atributo cor, utilizando o parametro cor_nova
    def troca_cor(self,  cor_nova):
        self.cor = cor_nova

    def mostra_cor(self):
        return self.cor


# escolhi usar os dados de uma bola de basquete como exemplo
bolaDeBasquete = Bola("Laranja", 75, "Couro Sintetico")

print(f"A cor da bola de basquete é: {bolaDeBasquete.mostra_cor()}")
bolaDeBasquete.troca_cor("Preta")
print(f"A nova cor da bola de basquete é: {bolaDeBasquete.mostra_cor()}")