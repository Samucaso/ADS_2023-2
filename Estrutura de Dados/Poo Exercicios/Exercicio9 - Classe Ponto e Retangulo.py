class Ponto:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def valores_ponto(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        return self.x, self.y


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        # instanciando os atributos vertice (escolhidos aleatoriamente) à classe ponto.
        self.vertice_inferior_esquerdo = Ponto()
        self.vertice_inferior_direito = Ponto()

    def valor_vertices(self, x1, x2, y1, y2):
        self.vertice_inferior_esquerdo = Ponto(x1, y1)
        self.vertice_inferior_direito = Ponto(x2, y2)

    # formula do centro do retangulo:
    # (coordenadas de um dos vertices(x, y) + coordenadas de um vertice oposto a esse(x, y)) / 2
    def centro_retangulo(self):
        c1 = (self.vertice_inferior_esquerdo.x + self.vertice_inferior_direito.x) / 2
        c2 = (self.vertice_inferior_esquerdo.y + self.vertice_inferior_direito.y) / 2
        return Ponto(c1, c2)


#   valores exemplo
ret = Retangulo(50, 20)
ret.valor_vertices(2, 4, 5, 3)
centro = ret.centro_retangulo()

print(f"As coordenadas do centro do retângulo são ({centro.x},{centro.y})")
