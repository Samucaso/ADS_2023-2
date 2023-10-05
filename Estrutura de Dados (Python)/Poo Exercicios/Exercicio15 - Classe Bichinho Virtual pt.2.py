import sys


class Tamagushi:
    brincou = False

    def __init__(self, nome=None, fome=5, saude=5, idade=0, tedio=5):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = tedio
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
                            if qtd_fome[alimento-1] == 0:
                                self._humor += 2
                            elif qtd_fome[alimento-1] == 1:
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

    # adicionado o metodo brincar, que permite que voce brinque com o bichinho.
    # caso voce nao brinque com o bichinho, ele fica entediado
    def brincar(self):
        print("Voce brincou com seu bichinho!")
        self._humor += 4
        self.retornar_humor()
        self.brincou = True
        self.retornar_tedio()
        self.retornar_humor()

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
            sys.exit()
        elif self._humor == 10:
            print(f"{self.nome} está extremamente feliz e agradecido! Obrigado por cuidar tão bem de mim!")
            sys.exit()
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
            print(f"{self.nome} estava morrendo de tedio e decidiu fugir!")
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

    # adicionado o metodo action, que organiza todas as ações em um menu
    def action(self):
        while True:
            try:
                acao = int(input("""O que deseja fazer com seu bichinho?
1 - Verificar fome; 2 - Verificar saude; 3 - Verificar humor; 4 - Brincar; 5 - Sair do jogo:\n"""))
                if acao in [1, 2, 3, 4, 5]:
                    if acao == 1:
                        self.alterar_fome()
                    elif acao == 2:
                        self.alterar_saude()
                    elif acao == 3:
                        self.retornar_humor()
                    elif acao == 4:
                        self.brincar()
                    else:
                        sys.exit()
                else:
                    print("Digite um dos numeros validos!")
                self.aumentar_idade()
                print(f"{self.nome} está com {self.idade} anos de idade")
            except ValueError:
                print("Digite um numero inteiro!")


bicho = Tamagushi()
print("SEJA BEM-VINDO AO BICHINHO VIRTUAL!")

nomeBicho = input("Dê um nome ao seu bichinho: ").strip()
bicho.alterar_nome(nomeBicho)

bicho.action()
