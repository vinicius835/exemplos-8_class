
class tv:
    cor = "preto"
    def __init__(self,tamanho,cor):
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self,novo_canal):
        self.canal = novo_canal
#programa
tv_sala = tv(cor='preto',tamanho=55)
tv_quarto = tv('branca',29)
print(tv_sala.cor)
print(tv_sala.tamanho)
print(tv_quarto.tamanho)
