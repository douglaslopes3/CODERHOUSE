#%%
if 3 > 2: 
    print('o primeirovalor é maior que o segundo')
# %%

temperatura = 29
if temperatura > 30: 
    print('Eu vou pra praia!')
# %%
temperatura = 29
if temperatura > 30:
    print('Eu vou pra praia!')
else: 
    print('Eu não vou pra praia!')

# %%

temperatura = 29

if temperatura > 30:
    print('Eu vou pra praia!')
elif temperatura > 20:
    print('Eu vou pro parque')
else:     
    print('Eu não vou fazer nada!')
# %%

salario = True
temperatura = 21
if temperatura > 30:
    print('Eu vou pra praia!')
elif temperatura > 20:
    print('Eu vou pro parque')
else:     
    if salario ==True:
        print('Vou ao cinema')
    else:
        print('Eu não vou fazer nada!')
# %%

score = 0.8
if score >= 0.85: 
    print('Aprovado')
elif (score>= 0.7):
    print('Solicitar documentos')
else: 
    print('Reprovado')


# %%

# for é usado quando eu sei quantas repetições eu necessito 

for i in range(10):
    print(i)

#%%
soma=0 
for i in range(10):
    soma=soma+i
print(soma)
# %%
alunos = ['Joao', 'Pedro', 'Lucas', 'Claudio']
nota = []
for i in alunos: 
    nota.append(int(input('Qual a nota do aludo{}? '.format(i))))
print(nota)

#%%
# while = enquanto 
# eu crio uma condição de parada, e ele vai rodar infinitamente a´te chegar nessa condição 

while i in range(10):
    print(i)
# %%

numero = 1 
while numero !=0: 
    numero=int(input('Digite um numero: '))
    print('a divisao de {} é {} e o resto é {}. '.format(numero, numero/2, numero%2))
# %%
