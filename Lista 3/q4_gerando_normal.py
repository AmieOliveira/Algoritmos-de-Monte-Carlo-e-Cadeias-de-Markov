"""
    Autora: Amanda Oliveira (AmieOliveira)

    Lista 3, questao 4
    Geracao de amostras normais atraves de amostragem por rejeicao
"""

from random import random   # Utiliza o metodo Mersenne Twister
from math import exp, sqrt, pi, log
import matplotlib.pyplot as plt

x_range = [i/10 for i in range(-400,400)]
normal = []
exponencial = []

lam = 1

for x in x_range:
    normal += [ exp(-x**2/2)/sqrt(2*pi) ]
    exponencial += [ lam*exp(-lam*abs(x)) ]
    if normal[-1] > exponencial[-1]:
        print("Atravessou!", normal[-1], exponencial[-1])

#normal = normal[1:][::-1] + normal
#exponencial = exponencial[1:][::-1] + exponencial
fig_envelope = plt.figure()
plt.plot(x_range, normal)
plt.plot(x_range, exponencial)
plt.legend(["Distribuição Normal", "Distribuição Exponencial"])

n = 10000       # Numero de amostras a serem geradas

envelope = []
amostras = []

n_sample = 0
while n_sample < n:
    # Gerando i a partir da distribuicao exponencial
    u_base = random()
    i = -log(1 - u_base)/lam
    u_coin = random()
    if u_coin > 1/2:
        i = -i
    envelope += [i]

    # Gerar uniforme continua entre 0 e P[X=i] (exponencial)
    u = random()*lam*exp(-lam*abs(i))

    # Comparacao com P[Z=i] (normal)
    if u < exp(-i**2/2)/sqrt(2*pi):
        amostras += [i]
        n_sample += 1


fig_amostras_envelope = plt.figure()
plt.hist(envelope, bins=50, density=True)

print(len(amostras), len(envelope))

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(1,1,1)
plt.title("Geração de amostras de distribuição normal")
plt.hist(amostras, bins=25, density=True)
plt.plot(x_range, normal, '--')
plt.legend(["Função Densidade de Probabilidade", "Distribuição Empírica"])
xmin, xmax, ymin, ymax = ax.axis()
ax.axis([-10, 10, ymin, ymax])
plt.savefig("Imagens/q4_pdf_empirica.pdf")
plt.show()