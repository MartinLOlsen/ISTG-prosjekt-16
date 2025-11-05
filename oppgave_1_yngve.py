import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('C:/Users/yngve/.vscode/Python/Maskin/3. Semester/Statistikk/Prosjekt/data.csv', header=0)
#print(df)
#print(df.shape)

# Del 1
X = df['omkrets'].mean() # gjennomsnitt av målinger
std = df['omkrets'].std(ddof=1) # standardavvik for målinger
print(f'Gjennomsnitt: {X:.2f}')
print(f'Standardavvik: {std:.2f}')

# Del 2
n = df['omkrets'].count() # antall målinger
SE = std / np.sqrt(n) # standardfeil
print(f'Standardfeil: {SE:.2f}')

# 95% Konfidensintervall
t = stats.t.ppf(0.975, n - 1) # t-verdi for 95% konfidensintervall
margin = t * SE 
nedre = X - margin # nedre grense i konfidensintervallet
ovre = X + margin # øvre grense i konfidensintervallet
print(f'95% konfidensintervall: ({nedre:.2f}, {ovre:.2f})')

# Del 3
A = X**2 / (4 * np.pi) # målefunksjon for areal av tverrsnitt
SE_A = (X / (2 * np.pi)) * SE # standardfeil for areal
#print(f'Areal: {A:.2f}')
#print(f'Standardavvik for areal: {SE_A:.2f}')

k = 2
print(f'Areal: {A:.2f} ± {k*SE_A:.2f}') # areal og usikkerhet med dekningsfaktor k=2

x = df['omkrets'].values # x1, x2, ..., xn
a = x**2 / (4 * np.pi) # a1, a2, ..., an
a_snitt = np.mean(a) # gjennomsnitt av areal
std_a = np.std(a, ddof=1) # standardavvik for areal
SE_a = std_a / np.sqrt(n) # standardfeil for areal
usikkerhet = k * SE_a # usikkerhet for areal med dekningsfaktor k=2
print(f'Areal (beregnet fra hver måling): {a_snitt:.2f} ± {usikkerhet:.2f}')