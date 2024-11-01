from  datetime import datetime
import pytz
class contacorrente:
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S')
    def __init__(self,nome,cpf,agencia,num_conta):
        self._nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
    def consultar_saldo(self):
        print("seu saldo atual é de R${:,.2f}".format(self.saldo))
        pass
    def depositar_dinheiro(self,valor):
        self.saldo += valor
        self.transacoes.append((valor,self.saldo,contacorrente._data_hora()))
        pass
    def limite_conta(self):
        self.limite = -1000
        return self.limite
    def sacar_dinheiro (self,valor):
        if self.saldo - valor <self.limite_conta():
            print("Voce não tem saldo suficiente POBRE")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((valor,self.saldo,contacorrente._data_hora()))
        pass
    def consultar_historico_transacoes(self):
        print('historico de transações: ')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self,valor,conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor,self.saldo,contacorrente._data_hora()))
        conta_destino.saldo +=valor
        conta_destino.transacoes.append((valor,conta_destino.saldo,contacorrente._data_hora())) 
#programa
conta_lira = contacorrente("Lira","111.222.333-45","Dayd-102",4002)
conta_lira.consultar_saldo()
#depositar um dinheiro na conta:
conta_lira.depositar_dinheiro(int(input("digite seu dinheiro: ")))
conta_lira.consultar_saldo()
#sacando
conta_lira.sacar_dinheiro(int(input("digite a quantidade: ")))
conta_lira.consultar_saldo()
conta_lira.consultar_historico_transacoes()
conta_maelira = contacorrente('Beth','222.333.444-55',55555,656565)
conta_lira.transferir(1000,conta_maelira)
print("Saldo da conta é: ",conta_lira.saldo)
print(conta_lira.cpf)
print(conta_lira.agencia)
print(conta_lira.num_conta)
print(conta_lira.transacoes)
print("*"*20)

print(conta_maelira.cpf)
print(conta_maelira.agencia)
print(conta_maelira.num_conta)
print(conta_maelira.transacoes)

print(conta_maelira )    