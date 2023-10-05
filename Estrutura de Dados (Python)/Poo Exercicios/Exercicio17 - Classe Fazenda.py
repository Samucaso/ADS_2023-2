import sys
import random


class Fazenda:
    brincou = False

    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)
        self.tedio = random.randint(0, 10)
        self.saude = 5
        self.idade = 0
        self._humor = 4

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

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
                        if alimento in [1, 2, 3]:
                            qtd_fome = [2, 5, 8]
                            self.fome += qtd_fome[alimento - 1]
                            if qtd_fome[alimento - 1] == 0:
                                self._humor += 2
                            elif qtd_fome[alimento - 1] == 1:
                                self._humor += 3
                            else:
                                self._humor += 5
                            self.retornar_fome()
                            self.retornar_humor()
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
            except ValueError:
                print("Digite um dos números válidos!")

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
                    self.retornar_humor()
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

    def brincar(self):
        print("Voce brincou com seu bichinho!")
        self._humor += 4
        self.retornar_humor()
        self.brincou = True
        self.retornar_tedio()
        self.retornar_humor()

    def aumentar_idade(self):
        self.idade += 1

    def str(self):
        print(f"---ATRIBUTOS---")
        print(f"Nome: {self.nome}")
        print(f"Fome: {self.fome}")
        print(f"Saude: {self.saude}")
        print(f"Idade: {self.idade}")
        print(f"Tedio: {self.tedio}")
        print(f"Humor: {self._humor}")

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
            print(f"{self.nome} esta extremamente triste :(")
        elif self._humor == 10:
            print(f"{self.nome} está extremamente feliz e agradecido! Obrigado por cuidar tão bem de mim!")
        else:
            print(f"{self.nome} está feliz!")

    def retornar_tedio(self):
        if not self.brincou:
            self.tedio -= 4
        else:
            self.tedio = 10

        if self.tedio < 0:
            self.tedio = 0

        if self.tedio < 5:
            print(f"{self.nome} esta entediado pois voce nao brinca com ele!")
        elif self.tedio == 0:
            print(f"{self.nome} esta morrendo de tedio!!")
            sys.exit()
        else:
            print(f"{self.nome} esta extasiado!")

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        if self.fome > 10:
            self.fome = 10
        elif self.fome < 0:
            self.fome = 0
        print(f"A barra de fome de {self.nome} está em {self.fome}/10")
        if self.fome == 0:
            print(f"{self.nome} esta morrendo de fome!!")
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

    # metodo alterado para funcionar com todos os bichinhos
    def action(self):
        while True:
            try:
                acao = int(input("""O que deseja fazer com seus bichinhos?
1 - Verificar fome; 2 - Verificar saude; 3 - Verificar humor; 4 - Brincar; 5 - Sair do jogo:\n"""))
                if acao == 1:
                    # para cada bichinho na lista fazenda, ele executa o metodo
                    for bicho in fazenda:
                        bicho.alterar_fome()
                    print("Você alimentou todos os bichinhos!")
                elif acao == 2:
                    for bicho in fazenda:
                        bicho.alterar_saude()
                    print("Você brincou com todos os bichinhos!")
                elif acao == 3:
                    for bicho in fazenda:
                        bicho.retornar_humor()
                elif acao == 4:
                    for bicho in fazenda:
                        bicho.brincar()
                elif acao == 5:
                    print("Saindo da fazenda, adeus!")
                    sys.exit()
                else:
                    print("Escolha uma opção válida!")
            except ValueError:
                print("Digite um numero inteiro!")


# lista feita para organizar os bichinhos em um lugar só
fazenda = []

num_bichinhos = int(input("Quantos bichinhos você deseja na sua fazenda? "))

# loop que adiciona os bichinhos à lista e os instancia ao mesmo tempo
for i in range(num_bichinhos):
    nome_bichinho = input(f"Digite o nome do bichinho {i + 1}: ")
    fazenda.append(Fazenda(nome_bichinho))

for bichinho in fazenda:
    bichinho.action()
