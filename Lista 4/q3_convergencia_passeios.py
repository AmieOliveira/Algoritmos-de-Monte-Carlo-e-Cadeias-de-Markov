"""
    Autora: Amanda Oliveira (AmieOliveira)

    Lista 4, questao 3
    Convergência de passeios aleatórios

    Obs.: Este codigo foi estruturado de forma a torna-lo mais organizado e facilitar a
        compreensao, e portanto foram desconsideradas diversas otimizacoes que poderiam
        tornar sua execucao mais eficiente e reduzir a complexidade
"""

import numpy as np
import matplotlib.pyplot as plt


T = 1000

d_pi_t = { "anel": np.zeros(T+1),
           "arvore": np.zeros(T+1),
           "grid": np.zeros(T+1)
          }


# Anel
n = 100 # Numero de vertices

pi_estac = np.ones(n)/n

pi_t = np.zeros(n)
pi_t[0] = 1         #  O passeio comeca com o andarilho no primeiro vertice

P = np.zeros((n,n))
for i in range(n):
    P[i][i] = 0.5

    if i != n-1:
        P[i][i+1] = 0.25
    else:
        P[i][0] = 0.25

    P[i][i-1] = 0.25

#print(pi_estac, "\n", P)
#print(pi_t)

for t in range(0, T+1):
    if t != 0:
        # Dou um passo:
        pi_t = np.matmul(pi_t, P)
        #print(pi_t)

    distance = 0
    for idx in range(n):
        distance += abs(pi_t[idx] - pi_estac[idx])
    distance = distance/2

    d_pi_t["anel"][t] = distance


#print(d_pi_t["anel"])

# -------------------------------
# Arvore
n = 127 # Numero de vertices

pi_estac = np.array([ 2.0/252 ] + [ 3.0/252 ]*62 + [ 1.0/252 ]*64)

pi_t = np.zeros(n)
pi_t[0] = 1         #  O passeio comeca com o andarilho no primeiro vertice

P = np.zeros((n,n))
for i in range(n):
    P[i][i] = 0.5

    if i == 0: # Raiz
        P[i][i+1] = 0.25
        P[i][i+2] = 0.25

    elif 0 < i < 63: # Tronco
        P[i][ int((i-1)/2) ] = 1/6
        P[i][2*i + 1] = 1/6
        P[i][2*i + 2] = 1/6

    else: # Folhas (i >= 63)
        P[i][ int((i-1)/2) ] = 0.5


for t in range(0, T+1):
    if t != 0:
        # Dou um passo:
        pi_t = np.matmul(pi_t, P)
        #print(pi_t)

    distance = 0
    for idx in range(n):
        distance += abs(pi_t[idx] - pi_estac[idx])
    distance = distance/2

    d_pi_t["arvore"][t] = distance


# -------------------------------
# Grid
pi_estac = np.zeros(100) # n = 100

for idx in range(1, 101):
    if idx in [1, 10, 91, 100]:
        pi_estac[idx-1] = 2.0/360

    elif 2 <= idx <= 9:
        pi_estac[idx-1] = 3.0/360

    elif 92 <= idx <= 99:
        pi_estac[idx-1] = 3.0/360

    elif idx % 10 == 0:
        pi_estac[idx-1] = 3.0/360

    elif idx % 10 == 1:
        pi_estac[idx-1] = 3.0/360

    else:
        pi_estac[idx-1] = 4.0/360


pi_t = np.zeros(100)
pi_t[0] = 1         #  O passeio comeca com o andarilho no primeiro vertice

P = np.zeros((100,100))
for i in range(100):
    n_i = i+1

    P[i][i] = 0.5

    # Quinas
    if n_i == 1:
        P[i][i+1] = 0.25
        P[i][i+10] = 0.25
    elif n_i == 10:
        P[i][i-1] = 0.25
        P[i][i+10] = 0.25
    elif n_i == 91:
        P[i][i-10] = 0.25
        P[i][i+1] = 0.25
    elif n_i == 100:
        P[i][i-1] = 0.25
        P[i][i-10] = 0.25

    # Laterais
    elif 2 <= n_i <= 9:
        P[i][i-1] = 1/6
        P[i][i+1] = 1/6
        P[i][i+10] = 1/6
    elif 92 <= n_i <= 99:
        P[i][i-1] = 1/6
        P[i][i+1] = 1/6
        P[i][i-10] = 1/6
    elif n_i % 10 == 1: # Nao vai incluir 1 e 91, ja foram contemplados
        P[i][i-10] = 1/6
        P[i][i+10] = 1/6
        P[i][i+1] = 1/6
    elif n_i % 10 == 0: # Nao vai incluir 10 e 100, ja foram contemplados
        P[i][i-10] = 1/6
        P[i][i+10] = 1/6
        P[i][i-1] = 1/6

    # Meio
    else:
        P[i][i+1] = 0.125
        P[i][i-1] = 0.125
        P[i][i+10] = 0.125
        P[i][i-10] = 0.125

for t in range(0, T+1):
    if t != 0:
        # Dou um passo:
        pi_t = np.matmul(pi_t, P)
        # print(pi_t)

    distance = 0
    for idx in range(100):
        distance += abs(pi_t[idx] - pi_estac[idx])
    distance = distance/2

    d_pi_t["grid"][t] = distance




# -------------------------------
# Grafico dos resultados
plt.plot(d_pi_t["anel"])
plt.plot(d_pi_t["arvore"])
plt.plot(d_pi_t["grid"])
plt.xlabel(r"Tempo $t$")
plt.ylabel(r"$d_{TV}(\pi, \pi_t) = \dfrac{1}{2}\sum_k|\pi_k - \pi_k(t)|$")
plt.legend(["Grafo em Anel", "Árvore Binária Cheia", "Grafo em Reticulado 2D"])

plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()