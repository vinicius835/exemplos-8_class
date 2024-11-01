

class tv():
    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
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
tv_sala = tv()
tv_quarto = tv()
tv_sala.mudar_canal()
print(tv_sala.canal)
print(tv_quarto.canal)
# tv.mudar_canal()
# tv.ligar_desligar()
