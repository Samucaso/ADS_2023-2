class TV:
    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume

    # metodo feito pra que um canal seja selecionado,
    # simulando uma tv que possui canais do 1 ao 100.
    def alterar_canal(self, novo_canal):
        if novo_canal > 100 or novo_canal < 1:
            print("Esse canal não existe, selecione um canal entre 1 e 100")
        else:
            self.canal = novo_canal

    def aumentar_volume(self):
        if self.volume == 100:
            print("O volume já está no máximo")
        else:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume == 0:
            print("O volume já está no mínimo")
        else:
            self.volume -= 1


tv = TV()
print(f"Você está no canal: {tv.canal}")
print(f"O volume da TV está em: {tv.volume}")

# while true para que o codigo nao pare caso haja uma digitação errada do usuario,
# no caso, ele printa uma mensagem de input invalido e reinicia o bloco
while True:
    resposta = input("Você quer mudar o canal? (sim/nao): ").lower()

    if resposta == "sim":
        muda_canal = int(input("Para qual canal deseja mudar?"))
        tv.alterar_canal(muda_canal)
        print(f"Você está no canal: {tv.canal}")
        break
    elif resposta == "nao":
        break
    else:
        print("Input inválido")

while True:
    resposta = input("Deseja aumentar ou diminuir o volume? (+/-)").lower()
    if resposta == "+":
        tv.aumentar_volume()
        print(f"O volume da TV está em: {tv.volume}")
        break
    elif resposta == "-":
        tv.diminuir_volume()
        print(f"O volume da TV está em: {tv.volume}")
        break
    else:
        print("Input inválido")
