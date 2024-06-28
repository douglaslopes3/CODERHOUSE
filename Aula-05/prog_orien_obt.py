
#%%
class Cachorro: 
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def latir(self):
        print('Au Au')

cachorro1 = Cachorro('Rex', 3, 'Vira-lata')

cachorro1.latir()
# %%

#pessoa

class Pessoa: 
    def __init__(self, nome, idade, sexo, renda):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.renda = renda


eu = Pessoa('Douglas', 30,'M',10000)
print(eu.idade)
# %%

# equação do primeiro grau 

class equacao1grau: 
    def __init__(self, a, b):
        self.inclinacao = a 
        self.intercepto = b
        self.x = -b/a 

    def raiz(self):
        print(f'A raiz da equação ({self.inclinacao})*x+({self.intercepto}) é {self.x}')

equacao = equacao1grau(2,3)
equacao.raiz()
# %%
