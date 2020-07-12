"""
    Autora: Amanda Oliveira (AmieOliveira)

    Lista 4, questao 4
    Tempo de mistura de passeios aleatórios
"""

import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

epsilon = 1e-4

n_values = np.array([10, 50, 100, 300, 700, 1000])
n_arvore = np.array([15, 63, 127, 255, 511, 1023])
n_grid = np.array([9, 49, 100, 289, 729, 1024])

n_size = len(n_values)

tau_an = np.zeros(n_size)
tau_av = np.zeros(n_size)
tau_gr = np.zeros(n_size)

# NOTE: Seria mais eficiente se criasse todos os grafos e rodasse o tempo uma vez so?

for nIdx in range(n_size):

    #n_max = max([n_values[nIdx], n_arvore[nIdx]])
    n = n_values[nIdx]
    nA = n_arvore[nIdx]
    nG = n_grid[nIdx]

    # Distribuicao estacionaria
    pi_estac = { "anel": np.ones(n)/n,
                 "arvore": np.zeros(nA),
                 "grid": np.zeros(nG)
                }

    leafs = (nA + 1)/2
    K_a = 2 + 3*(nA - leafs - 1) + leafs
    pi_estac["arvore"][0] = 2/K_a

    sqG = int(sqrt(nG))
    K_g = 8 + 12*(sqG - 2) + 4*(nG - 4*sqG + 4)
    pi_estac["grid"][0] = 2/K_g


    # Matriz de transicao
    P = {"anel": np.zeros((n, n)),
         "arvore": np.zeros((nA, nA)),
         "grid": np.zeros((nG, nG))
         }

    for i in range(max([n, nA, nG])):
        v = i+1

        # Distribuicao estacionaria
        # Arvore
        if 1 < v <= nA:
            if v < int(leafs): # Tronco
                pi_estac["arvore"][i] = 3/K_a
            else:  # Folha
                pi_estac["arvore"][i] = 1/K_a

        # Grid
        if 1 < v <= nG:
            if v in [sqG, nG-sqG+1, nG]: # Quina
                pi_estac["grid"][i] = 2/K_g
            elif 1 < v < sqG:
                pi_estac["grid"][i] = 3/K_g
            elif nG-sqG+1 < v < nG:
                pi_estac["grid"][i] = 3/K_g
            elif v % sqG == 1:
                pi_estac["grid"][i] = 3/K_g
            elif v % sqG == 0:
                pi_estac["grid"][i] = 3/K_g
            else: # Interior
                pi_estac["grid"][i] = 4/K_g


        # Matriz de transicao
        # Anel
        if v <= n:
            P["anel"][i][i] = 0.5

            if i != n-1:
                P["anel"][i][i+1] = 0.25
            else:
                P["anel"][i][0] = 0.25

            P["anel"][i][i-1] = 0.25

        # Arvore
        if v <= nA:
            P["arvore"][i][i] = 0.5

            if v == 1: # raiz
                P["arvore"][i][i+1] = 0.25
                P["arvore"][i][i+2] = 0.25

            elif v < int(leafs): # Tronco
                P["arvore"][i][int((i-1)/2)] = 1/6
                P["arvore"][i][2*i + 1] = 1/6
                P["arvore"][i][2*i + 2] = 1/6

            else: # Folha
                P["arvore"][i][ int((i-1)/2) ] = 0.5

        # Grid
        if v <= nG:
            P["grid"][i][i] = 0.5

            # Quinas
            if v == 1:
                P["grid"][i][i + 1] = 0.25
                P["grid"][i][i + sqG] = 0.25
            elif v == sqG:
                P["grid"][i][i - 1] = 0.25
                P["grid"][i][i + sqG] = 0.25
            elif v == nG-sqG+1:
                P["grid"][i][i - sqG] = 0.25
                P["grid"][i][i + 1] = 0.25
            elif v == nG:
                P["grid"][i][i - 1] = 0.25
                P["grid"][i][i - sqG] = 0.25

            # Laterais
            elif 1 < v < sqG:
                P["grid"][i][i-1] = 1/6
                P["grid"][i][i+1] = 1/6
                P["grid"][i][i+sqG] = 1/6
            elif nG-sqG+1 < v < nG:
                P["grid"][i][i-1] = 1/6
                P["grid"][i][i+1] = 1/6
                P["grid"][i][i-sqG] = 1/6
            elif v % sqG == 1:
                P["grid"][i][i-sqG] = 1/6
                P["grid"][i][i+sqG] = 1/6
                P["grid"][i][i+1] = 1/6
            elif v % sqG == 0:
                P["grid"][i][i-sqG] = 1/6
                P["grid"][i][i+sqG] = 1/6
                P["grid"][i][i-1] = 1/6

            # Interior
            else:
                P["grid"][i][i+1] = 0.125
                P["grid"][i][i-1] = 0.125
                P["grid"][i][i+sqG] = 0.125
                P["grid"][i][i-sqG] = 0.125

    #print(pi_estac["anel"])
    #print(pi_estac["arvore"])
    #print(pi_estac["grid"])

    #print(P["anel"])
    #print(P["arvore"])
    #print(P["grid"])

    # Distribuicao de probabilidade inicial
    pi_t = { "anel": np.zeros(n),
             "arvore": np.zeros(nA),
             "grid": np.zeros(nG)
            }
    pi_t["anel"][0] = 1
    pi_t["arvore"][0] = 1
    pi_t["grid"][0] = 1

    #print(pi_t)



    finished = { "anel": False,
                 "arvore": False,
                 "grid": False
                }

    # Iterando no tempo
    t = 0
    while not (finished["anel"] and finished["arvore"] and finished["grid"]):
        t += 1

        # Anel
        if not finished["anel"]:
            pi_t["anel"] = np.matmul(pi_t["anel"], P["anel"])

            distance = 0
            for idx in range(n):
                distance += abs(pi_t["anel"][idx] - pi_estac["anel"][idx])
            distance = distance/2

            if distance <= epsilon:
                tau_an[nIdx] = t
                finished["anel"] = True
                print("Terminado anel. n={}, t={}".format(n,t))

        # Arvore
        if not finished["arvore"]:
            pi_t["arvore"] = np.matmul(pi_t["arvore"], P["arvore"])

            distance = 0
            for idx in range(nA):
                distance += abs(pi_t["arvore"][idx] - pi_estac["arvore"][idx])
            distance = distance/2

            if distance <= epsilon:
                tau_av[nIdx] = t
                finished["arvore"] = True
                print("Terminada arvore. n={}, t={}".format(nA, t))

        # Grid
        if not finished["grid"]:
            pi_t["grid"] = np.matmul(pi_t["grid"], P["grid"])

            distance = 0
            for idx in range(nG):
                distance += abs(pi_t["grid"][idx] - pi_estac["grid"][idx])
            distance = distance/2

            if distance <= epsilon:
                tau_gr[nIdx] = t
                finished["grid"] = True
                print("Terminada grid. n={}, t={}".format(nG, t))



plt.plot(n_values, tau_an)
plt.plot(n_arvore, tau_av)
plt.plot(n_grid, tau_gr)
plt.xlabel(r"Número de vértices $n$")
plt.ylabel(r"Tempo de mistura $\tau_n$ ($\epsilon = 10^{-4}$)")
plt.legend(["Grafo em Anel", "Árvore Binária Cheia", "Grafo em Reticulado 2D"])

plt.figure()
plt.plot(n_values, tau_an)
plt.plot(n_arvore, tau_av)
plt.plot(n_grid, tau_gr)
plt.xlabel(r"Número de vértices $n$")
plt.ylabel(r"Tempo de mistura $\tau_n$ ($\epsilon = 10^{-4}$)")
plt.legend(["Grafo em Anel", "Árvore Binária Cheia", "Grafo em Reticulado 2D"])
#plt.xscale('log')
plt.yscale('log')

plt.grid(True)
plt.show()