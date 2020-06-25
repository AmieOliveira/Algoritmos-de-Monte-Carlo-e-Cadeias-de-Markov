"""
    Autora: Amanda Oliveira (AmieOliveira)

    Lista 3, questao 2
    Geracao de amostras atraves do metodo da transformada inversa
"""

from random import random   # Utiliza o metodo Mersenne Twister
from math import log
import matplotlib.pyplot as plt

n = 10000       # Numero de amostras a serem geradas
n_bins = 50     # Numero de bins nos histogramas
lam = 1
alp = 10
x_0 = 1

exponencial = []
pareto = []

for sample in range(n):
    u = random()
    exponencial += [ -log(1 - u)/lam ]
    pareto += [ x_0/((1 - u)**(1.0/alp)) ]


#fig, axs = plt.subplots(,nrows=2, ncols=1)
fig, axs = plt.subplots(2, 1,figsize=(5,7)) #, sharex=True)
fig.suptitle("Função densidade de probabilidade empírica", y=.93)

axs[0].hist(exponencial, density=True, bins=n_bins)
axs[0].set_xlabel("Distribuição Exponencial")
axs[0].text(.6, .7, r'$\lambda=1$', va='center', transform=axs[0].transAxes)


axs[1].hist(pareto, density=True, bins=n_bins, color='gray')
axs[1].set_xlabel("Distribuição de Pareto")
axs[1].text(.6, .7, r'$\alpha=10$', va='top', transform=axs[1].transAxes)
axs[1].text(.6, .7, r'$x_0=1$', va='bottom', transform=axs[1].transAxes)

plt.savefig("Imagens/q2_pdfs.pdf")
plt.show()