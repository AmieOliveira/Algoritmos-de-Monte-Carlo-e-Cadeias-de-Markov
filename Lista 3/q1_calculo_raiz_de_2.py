"""
    Autora: Amanda Oliveira (AmieOliveira)

    Lista 3, questao 1
    Implementacao do metodo de Monte Carlo para estimar o valor de sqrt(2)
"""

from random import random   # Utiliza o metodo Mersenne Twister
from math import sqrt
import matplotlib.pyplot as plt


max_exp = 6
estimate = []
n_values = []

r2 = sqrt(2)

for exponent in range(max_exp+1):
    n = 10**exponent     # Numero de amostras geradas (para o calculo da media amostral)

    sum_g = 0

    for idx in range(n):
        # Ponto aleatorio dentro de um quadrado de lado 2
        x = random()*2
        y = random()*2
        # Multiplicando por 2, passamos a ter um dominio [0,2)^2

        g = 1 if (y <= 2 - x**2) else 0
        sum_g += g

    mean_g = sum_g/float(n)

    r_2 = 3*mean_g   # Valor aproximado de sqrt(2)
    #print(n, r_2, r2)

    estimate += [ abs(r_2 - r2)/r2 ]
    n_values += [ n ]

plt.plot(n_values, estimate)
plt.xscale('log')
plt.title(r"Erro relativo do estimador de $\sqrt{2}$")
plt.ylabel(r"$\frac{|\hat{e}_n - \sqrt{2}|}{\sqrt{2}}$")
plt.xlabel("Número de amostras n")

fig = plt.figure()
plt.plot(n_values, estimate)
plt.xscale('log')
plt.yscale('log')
plt.title(r"Erro relativo do estimador de $\sqrt{2}$")
plt.ylabel(r"$\frac{|\hat{e}_n - \sqrt{2}|}{\sqrt{2}}$")
plt.xlabel("Número de amostras n")

plt.show()