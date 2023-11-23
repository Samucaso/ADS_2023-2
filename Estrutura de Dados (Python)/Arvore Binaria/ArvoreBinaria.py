class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return f"{self.esquerda and self.esquerda.chave} <- {self.chave} ->" \
               f" {self.direita and self.direita.chave}"


def em_ordem(raiz):
    if not raiz:
        return
    em_ordem(raiz.esquerda)
<<<<<<< HEAD
    print(raiz.chave),
=======

    print(raiz.chave)

>>>>>>> 4ac017f0ae18b5a99948842d4751c952d3fafccc
    em_ordem(raiz.direita)


raiz = NodoArvore(40)
raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)
raiz.direita.esquerda = NodoArvore(50)
raiz.direita.direita = NodoArvore(70)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)

print("Árvore: ", raiz)
em_ordem(raiz)

