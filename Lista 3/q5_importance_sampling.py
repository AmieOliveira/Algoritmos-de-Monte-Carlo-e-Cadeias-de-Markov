"""
    Autora: Amanda Oliveira (AmieOliveira)

    Lista 3, questao 5
    Estimando somas com importance sampling
"""

from random import random   # Utiliza o metodo Mersenne Twister
from math import log, sqrt
import matplotlib.pyplot as plt


# Conferindo desempenho da funcao de amostragem
N = 1e6
G_N = 0
s_lin = 0
s_unif = 0
for i in range(1,int(N+1)):
    G_N += i*log(i)
    s_lin += i*log(i)**2
    s_unif += (i*log(i))**2
K = N*(N+1)/2
seg_momento = s_lin*K
seg_mom_unif = s_unif*N
print("O segundo momento para o caso uniforme vale: {:e}, enquanto para a função de amostragem temos {:e}".
      format(seg_mom_unif, seg_momento))

N = 1e6
K = N*(N+1)/2
G_N = 0
for i in range(1,int(N+1)):
    G_N += i*log(i)
print("O valor da soma de {:e} elementos é: {:e}".format(N, G_N))

n_exp_max = 7
n_values = []
erros = []
for exp in range(n_exp_max+1):
    n = 10**exp
    n_values += [n]

    soma = 0
    c = (N * log(N) / K)
    for sampleIdx in range(n):
        # Preciso amostrar com base na funcao de probabilidade P[Y=y] = y/K
        u = random()
        y = ( sqrt(1+8*K*u) - 1 )/2
        soma += K*log(y) #y*log(y)/(y/K)
    Mn = soma/n
    print("{:e}".format(Mn))

    erros += [ abs(Mn - G_N)/G_N ]

plt.plot(n_values, erros)
plt.xscale('log')
plt.title(r"Erro relativo do estimador de $G_N$")
plt.ylabel(r"$\frac{|M_n - G_N|}{G_N}$")
plt.xlabel("Número de amostras n")

fig = plt.figure()
plt.plot(n_values, erros)
plt.xscale('log')
plt.yscale('log')
plt.title(r"Erro relativo do estimador de $G_N$")
plt.ylabel(r"$\frac{|M_n - G_N|}{G_N}$")
plt.xlabel("Número de amostras n")

plt.show()