"""
    Autora: Amanda Oliveira (AmieOliveira)

    Lista 3, questao 3
    Implementacao do metodo de Monte Carlo para estimar o numero de dominios WEB dentro da UFRJ
    Padrao de nome: http://www.[].ufrj.br (onde [] e uma sequencia de caracteres (regex))
"""

N_LETRAS = 26
LETRAS = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

from random import random   # Utiliza o metodo Mersenne Twister
import requests
import matplotlib.pyplot as plt

k = 4   # Tamanho maximo da sequencia de caracteres desejada
max_exp = 4


# Obtencao do total de sequencias possiveis
N = 0
pesos = []

for i in range(k+1):
    tmp = N_LETRAS**i
    N += tmp
    pesos += [ tmp ]
print(N) # pesos

# Funcao que gera uma sequencia de maneira uniforme
def sequencia():
    # NOTE: Poderia fazer uma geradora que retornaria em O(1), entretanto considerando
    # que nao vamos usar valores grandes de k, julguei que o ganho de processamento nao justifica
    # (especialmente porque da forma que esta feito na maioria das vezes vai retornar em O(1))

    # Determinacao do tamanho da sequencia
    u = random()
    soma, tamanho = N-pesos[k], k
    while soma > N*u:
        tamanho -= 1
        soma = soma - pesos[tamanho]

    # Conseguindo sequencia
    s = ""
    for i in range(tamanho):
        # Selecao de maneira uniforme do caracter
        u = random()
        cIdx = int(N_LETRAS*u)

        s += LETRAS[cIdx]

    return s

# Funcao que verifica se o site existe
def check(website):
    try:
        r = requests.head(website)
        return 1
        #if request.status_code == requests.codes.ok: # Codigo que diz que o site esta ok: requests.codes.ok = 200
        #    return 1
        #return 0
        # NOTE: Nao preciso conferir o codigo, porque se ha codigo entao um servidor deu essa resposta
        # (Assim posso considerar que existe o dominio)
    except requests.ConnectionError:
        return 0

n_list = []
D_list = []

for exp in range(max_exp+1):
    n = 10**exp
    n_list += [ n ]

    # Implementacao do metodo de Monte Carlo
    soma = 0
    for sampleIdx in range(n):
        site = "http://www.{}.ufrj.br".format(sequencia())
        #print(site)
        existe = check(site)
        soma += existe
        if existe:
            print("Found! {}".format(site))
    mediaAmostral = soma/n
    print(mediaAmostral)

    D = N*mediaAmostral

    D_list += [ D ]

print(n_list, D_list)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(n_list, D_list)
plt.xscale('log')
plt.title("Estimativa do número de domínios da UFRJ")
plt.xlabel("Número de amostras n")
plt.text(.15, .7, r'$k=4$', transform=ax.transAxes)
#plt.show()
plt.savefig("Imagens/q3_dominios_ufrj.pdf")