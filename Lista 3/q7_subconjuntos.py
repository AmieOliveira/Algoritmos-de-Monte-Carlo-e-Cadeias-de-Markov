"""
    Autora: Amanda Oliveira (AmieOliveira)

    Lista 3, questao 7
    Geracao de subconjuntos
"""

from random import random   # Utiliza o metodo Mersenne Twister
import numpy as np
from time import time
import matplotlib.pyplot as plt

r = 1000
n_values = [1e4, 1e6, 1e8]
k_values = [1e1, 1e2, 1e3, 1e4]

tempos = {}
for n in n_values:
    n = int(n)
    tempos[n] = []
    elementos_base = np.array(list(range(1, n + 1)))

    for k in k_values:
        k = int(k)
        elementos = elementos_base.copy()

        start_time = time()
        for repeat in range(r):
            #elementos = elementos_base.copy()
            # Estou considerando que, devido a aleatoriedade, nao reiniciar o vetor nao gera
            # dependencia entre as amostras
            for ite in range(k):
                u = random()
                i = int((n-ite)*u)
                tmp = elementos[i]
                elementos[i] = elementos[(n-1) - ite]
                elementos[(n-1) - ite] = tmp

            # NOTE: A amostra corresponde aos primeiros k elementos do vetor
            # amostra = elementos[:k]
            # print(amostra)
            # Observe que no caso de subconjuntos nao ordenados a comparacao de duas
            # amostras necessitaria da ordenacao das mesmas


        total_time = time() - start_time # Em segundos
        tempos[n] += [total_time/r] # Tempo medio
        print(n, k, total_time/r)

fig = plt.figure()
plt.title(r"Tempo médio de execução")
plt.ylabel("Tempo (s)")
plt.xlabel("Tamanho do subconjunto k")
texts = []
for n in n_values:
    n = int(n)
    plt.plot(k_values, tempos[n])
    texts += [r"$n={}$".format(n)]
plt.xscale('log')
#plt.yscale('log')
plt.legend(texts)
plt.savefig("Imagens/q7_subconjuntos_tempoMedio.pdf")
plt.show()