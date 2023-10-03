import sys

class Tamagushi:
    def __init__(self, nome=None, fome=5, saude=5, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self._humor = 4

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    # nesse metodo, o usuario escolhe se deseja, e com que alimento deseja alimentar o bichinho
    # de acordo com o alimento selecionado, a barra de fome do bichinho aumenta um certo nivel
    def alterar_fome(self):
        self.fome -= 2
        self.retornar_fome()
        resposta = input('Deseja alimentar seu bichinho? ("sim" ou "nao"): ').lower()
        while True:
            try:
                if resposta == "sim":
                    alimento = int(input(f'''Como deseja alimentar {self.nome}?
(digite 1 para "banana", digite 2 para "frango" e digite 3 para "lasanha"): '''))
                    while True:
                        # criei essa lista pra verificar se o numero fornecido pelo usuario é valido
                        # se estiver dentro da lista, ele roda o codigo seguinte
                        if alimento in [1, 2, 3]:
                            # qtd_fome são os valores a serem adicionados na barra de fome do bichinho
                            # self.fome é aumentado de acordo com o index, e usei o index [alimento - 1],
                            # pois coincidentemente alimento é uma sequencia de 1, 2, 3
                            qtd_fome = [2, 5, 8]
                            self.fome += qtd_fome[alimento - 1]
                            if qtd_fome[alimento-1] == 0:
                                self._humor += 2
                            elif qtd_fome[alimento-1] == 1:
                                self._humor += 3
                            else:
                                self._humor += 5
                            self.retornar_fome()
                            break
                        else:
                            alimento = int(input("Digite uma opção válida (1, 2 ou 3): "))
                    break
                elif resposta == "nao":
                    self.fome -= 3
                    self._humor -= 2
                    self.retornar_fome()
                    self.retornar_humor()
                    break
                else:
                    resposta = input("Digite (sim/nao): ")
            # criei esse try except pra evitar erros de valor, com o usuario digitando uma string ao inves de um int
            except ValueError:
                print("Digite um dos números válidos!")

    # metodo que calcula o nivel de saude do bichinho e pergunta se voce deseja medica-lo ou noo
    def alterar_saude(self):
        self.saude -= 3
        self.retornar_saude()
        if self.saude <= 5:
            while True:
                resposta2 = input('Deseja medicá-lo? ("sim" ou "nao") ').lower()
                if resposta2 == "sim":
                    print("Você medicou o seu bichinho!")
                    self.saude = 10
                    self.retornar_saude()
                    self._humor += 4
                    break
                elif resposta2 == "nao":
                    self.saude -= 3
                    self._humor -= 3
                    self.retornar_saude()
                    self.retornar_humor()
                    break
                else:
                    print("Digite um input válido!")
        else:
            pass

    def aumentar_idade(self):
        self.idade += 1

    def retornar_humor(self):
        if self._humor < 0:
            self._humor = 0
        elif self._humor > 10:
            self._humor = 10
        if 3 < self._humor <= 5:
            print(f"{self.nome} está triste :(")
        elif 0 < self._humor <= 3:
            print(f"{self.nome} está muito triste! :(")
        elif self._humor == 0:
            print(f"{self.nome} estava tão triste que fugiu :(")
            # funcao que fecha a execução do código, funcionando como um "fim do jogo"
            sys.exit()
        elif self._humor == 10:
            print(f"{self.nome} está extremamente feliz e agradecido! Obrigado por cuidar tão bem de mim!")
            sys.exit()
        else:
            print(f"{self.nome} está feliz!")

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        if self.fome > 10:
            self.fome = 10
        elif self.fome < 0:
            self.fome = 0
        print(f"A barra de fome de {self.nome} está em {self.fome}/10")
        if self.fome == 0:
            print(f"{self.nome} estava morrendo de fome e decidiu fugir!")
            sys.exit()
        elif 0 < self.fome < 5:
            print(f"{self.nome} está com fome!")
        elif 5 <= self.fome < 10:
            print(f"{self.nome} está satisfeito")
        else:
            print(f"{self.nome} está empanturrado!")

    def retornar_saude(self):
        if 4 >= self.saude < 5:
            print(f"{self.nome} está doente :(")
            self._humor -= 2
        elif 0 > self.saude < 4:
            print(f"{self.nome} está muito doente! :(")
            self._humor -= 5
        elif self.saude == 5:
            print(f"{self.nome} está ficando doente :|")
        else:
            print(f"{self.nome} está saudável :)")


bicho = Tamagushi()
print("SEJA BEM-VINDO AO BICHINHO VIRTUAL!")

nomeBicho = input("Dê um nome ao seu bichinho: ").strip()
bicho.alterar_nome(nomeBicho)

# while que roda o "jogo" enquanto os sys.exit nao forem executados
while True:
    bicho.aumentar_idade()
    print(f"{bicho.nome} está com {bicho.idade} anos.")
    bicho.alterar_fome()
    input("---pressione Enter para continuar---")
    bicho.alterar_saude()
    input("---pressione Enter para continuar---")
    bicho.retornar_humor()
