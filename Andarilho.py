"""

Autora: AmieOliveira
Experimento: Andarilho Aleatorio

"""

from random import randint
from numpy.random import binomial
import matplotlib.pyplot as plt


# Descricao da moeda:
p = 0.5

# Tamanho do espaco:
n_max = 8

# Estado do andarilho:
x_0 = 7 # randint(1, n_max)
print( "Walker Initial Position: {}".format(x_0) )


# Simulation
repeat = 4000
totTime = 500

counts = []

for turn in range(repeat):
    x = x_0

    for t in range(totTime):
        if x == 1:
            x = 2
        elif x == n_max:
            x = n_max - 1
        else:
            forward = binomial(1, p)
            if forward:
                x = x+1
            else:
                x = x-1

        if turn == 0:
            counts += [[0] * n_max]

        counts[t][x-1] += 1

#print(counts)

spots = list(range(1,n_max+1))

#probabilityOdds = [counts[totTime-1][i]/float(repeat) for i in range(n_max)]
#probabilityEvens = [counts[totTime-2][i]/float(repeat) for i in range(n_max)]
probability = []
for i in range(n_max):
    probability += [ 0.5*( counts[totTime-1][i] + counts[totTime-2][i] )/float(repeat) ]
print(probability)

axisHeight = 0.01 + max(probability)
plt.plot([1,1],[0,axisHeight], 'k')
plt.plot([1,n_max],[0,0], 'k')
plt.plot(spots,probability, "--", linewidth=.5, color='grey')
plt.plot(spots,probability, "*")
plt.text(n_max-1, 0.01, "X0 = {}".format(x_0))
plt.show()
