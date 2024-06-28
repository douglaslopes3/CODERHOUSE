
#%% 
# criando funçaõ simples 
def soma(elemento1, elemento2):
    return elemento1 + elemento2

numero1 = int(input('Digite um número: '))

numero2 = int(input('Digite outro número: '))

print(soma(numero1,numero2))

# %%
# criando função com parametro fixo

def potencia(x,y=1):
    return x**y

numero1 = int(input('Digite um número: '))

numero2 = int(input('Digite outro número: '))

print(potencia(numero1,numero2))
#%%

#função anonima lambda
# lambda argumentos: função simples

cubo=lambda x:x**3
cubo(3)

# %%

#Função integrada MAP
# map(função pronta, iteravel)

x = map(cubo,[1,2,3,4,5])
print(list(x))
# %%

