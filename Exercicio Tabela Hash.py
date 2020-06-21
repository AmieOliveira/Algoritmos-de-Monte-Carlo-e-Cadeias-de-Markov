"""

Autora: AmieOliveira
Experimento:
    Seja k o tamanho de uma tabela hash 'perfeita' [[ P( f(d1)=i ) = 1/k para todo i pertencente a [1, k] ]], e
    n o numero de elementos de dados a serem armazenados, trace um grafico da probabilidade de colisao (eixo y)
    em funcao de n (eixo x) para diferentes valores de k. Faca k = {10^4, 10^6, 10^8, 10^10}

"""

from math import exp
import matplotlib.pyplot as plt

k = [ 1e4, 1e6, 1e8, 1e10 ]

# pc = {}
for kValue in k:
    print("{}...".format(kValue))
    n = [ i for i in range( 1001 ) ]
    # pc[kValue] = [ (1.0-exp(-nValue*(nValue-1)/(2*kValue))) for nValue in n]
    pcK = [ (1.0-exp(-nValue*(nValue-1)/(2*kValue))) for nValue in n ]
    plt.plot(n, pcK)
    # plt.show()

print("Done! Printing")
plt.show()