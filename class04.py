

class tv():
    def __init__(self,cor,tamanho):
        self.cor = cor
        self.ligada = False
        self.tamanho = tamanho
        self.canal = 'Netflix'
        self.volume = 10    
    cor = 'preta'
    tamanho = 55
    canal = 10
    volume = 50

    def mudar_canal(self):
        self.canal = "Disney+"
    def mudar_volume(self):
        pass
    def ligar_desligar(self):
        pass
#programa
tv_sala = tv(cor='preta',tamanho=55)
tv_quarto = tv(cor='branca',tamanho=29)
tv_sala.mudar_canal()
print(tv_sala.canal)
print(tv_quarto.canal)
print("cor da TV da sala: ",tv_sala.cor)
print("tamanho da TV do quarto: ",tv_quarto.tamanho)
# tv.mudar_canal()
# tv.ligar_desligar()
