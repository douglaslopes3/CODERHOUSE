#%%

#date 

from datetime import date
from datetime import datetime as dt

print(date.today())

print(dt.today())

print(dt.now())

print(dt.now().year)

print(dt.now().month)

hoje = dt.today()
print(hoje.strftime('%d/%m/%Y'))
# %%
data_exemplo = dt.strptime('20/06/2024','%d/%m/%Y')
print(data_exemplo)

#%% 

