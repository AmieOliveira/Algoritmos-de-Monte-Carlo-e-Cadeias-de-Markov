"""

Autora: AmieOliveira
Experimento:
    Tirando duas bolinhas do saco e tendo verificado que uma delas e branca ('b'), qual a probabilidade de
    as duas serem brancas?

"""

from random import randint
import matplotlib.pyplot as plt


saco = ['b', 'b', 'v', 'a']

nTries = 0
nSuccess = 0
progression = []
progressionLog = []


nTotTries = 1000
expected = 1.0/5


while nTries < nTotTries:
    # Sorteio duas bolinhas
    idx1 = randint(0, len(saco)-1)
    bolinha1 = saco[idx1]
    saco2 = saco[:idx1] + saco[idx1+1:]
    idx2 = randint(0, len(saco2)-1)
    bolinha2 = saco2[idx2]

    if (bolinha1 == 'b') or (bolinha2 == 'b'):
        nTries += 1
        if (bolinha1 == 'b') and (bolinha2 == 'b'):
            nSuccess += 1
        progression += [float(nSuccess)/nTries]
        progressionLog += [ abs(float(nSuccess)/nTries - expected) ]

print("Result: {}".format( float(nSuccess)/nTries) )

plt.plot([0, nTries], [expected, expected], 'k')
plt.plot(progression)
plt.grid(True)

plt.figure()
plt.plot(progressionLog)
plt.yscale('log')
plt.grid(True)

plt.show()