#%%
from exercicios import Retangulo

retangulo = Retangulo(10,20)
retangulo.area()
retangulo.perimetro()
# %%

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor

conta = Conta( 'Doug',20)

conta.depositar(10)
print(f'O saldo após deposito é {conta.saldo}')

conta.sacar(10)
print(f'O saldo após o saque é {conta.saldo}')
# %%
