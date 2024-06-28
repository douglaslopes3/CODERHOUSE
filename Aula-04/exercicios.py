#%%

eh_multiplo_10 = lambda x: x % 10 == 0
print(eh_multiplo_10(int(input('Digite um numero'))))
#%%


#Exercicio 4 
nome_completo = 'Douglas Lopes de Souza'
primeiro_nome = nome_completo.split(' ')[0]
print(primeiro_nome)

#%%

def primeiro_nome(nome_completo):
    nome_1 = nome_completo.split(' ')[0]
    return nome_1

print(primeiro_nome('Douglas Lopes de Souza'))
# %%

#Exercicio 6


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun',]

def dia_semana(data_br):
    from datetime import datetime as dt    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun',]
    data = dt.strptime(data_br, '%d/%m/%Y')
    return days[data.weekday()]

print(dia_semana('20/06/2024'))
# %%
