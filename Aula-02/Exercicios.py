#%%
saldo=950.60
saque=float(input('Digite o valor do saque: '))
saldo=saldo-saque
print( f'ovalor do saldo atual é {saldo:.2f}')
#%%

lista_frutas=[]

for i in range(5):
    fruta = input(f'Digite uma fruta {i+1}: ')
    lista_frutas.append(fruta)
frutas_unicas = set(lista_frutas)
lista_frutas_unicas = list(frutas_unicas)
print(lista_frutas_unicas)

# %%

frase = input('Digite uma frase: ')

vogais = 'aeiouAEIOU'

for vogal in vogais:
    frase = frase.replace(vogal, '*')

print(frase)

# %%
