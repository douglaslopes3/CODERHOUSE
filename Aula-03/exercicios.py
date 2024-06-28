
#%% 

#Escreva um programa que receba um número inteiro 
# e exiba se ele é par ou ímpar.

numero  = int(input('Digite um valor: '))

if numero % 2 == 0:
    print(f'{numero} é par')
else: 
    print(f'{numero} é impar')

# %%

# screva um programa em Python que solicita ao usuário uma frase e,
#  em seguida, 
# exibe cada palavra e seu número de caracteres.

frase = input('Digite uma frase: ')
palavras = frase.split()
for i in palavras:
   print(f'A palavra {i} tem {len(i)} caracteres')

#%% 
#Crie um programa em Python que solicita ao usuário
#uma senha numérica de 4 dígitos. 
#O programa deve repetir essa solicitação 
#até que o usuário informe a senha correta (1234).

senha = int(input('Digite a senha: '))

while senha!= 1234:
    print('Senha incorreta')
    senha = int(input('Digite a senha correta'))

print('Senha correta')


#%%
#Escreva um programa que dado um valor n calcula o fatorial de n.

numero = int(input('Digite um numero: '))
fatorial = 1
for i in range(1,numero+1):
    fatorial = fatorial * i
print(fatorial)

#%%

#Crie um dicionário com os dados da tabela ao lado, crie um loop
#para exibir os valores. 

dicionario = {
    'Mês': ['Janeiro','Fevereiro','Junho','Julho'],
    'Quantidade': [232,321,589,547]  
}

for i in range(len(dicionario['Mês'])):
    print(f'{dicionario["Mês"][i]}: {dicionario["Quantidade"][i]}')


# %%

dicionario = {
    'Janeiro': 232,
    'Fevereiro': 321,
    'Junho': 589,
    'Julho': 547
}

for mes, quantidade in dicionario.items():
    print(f'{mes}: {quantidade}')
