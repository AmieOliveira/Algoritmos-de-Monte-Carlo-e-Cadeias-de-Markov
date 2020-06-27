"""
    Autora: Amanda Oliveira (AmieOliveira)

    Lista 3, questao 6
    Integracao de Monte Carlo
"""

from random import random   # Utiliza o metodo Mersenne Twister
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)


a_values = [0]
b_values = [1, 2, 4]
alpha_values = [1, 2, 4]
color = [['brown','indianred','lightcoral'],
         ['darkorange','orange','gold'],
         ['darkslategrey','teal','cadetblue']]

n_max = 6

fig, ax = plt.subplots(3, 3, sharey='row', sharex='col', figsize=(10,6))

fig.suptitle(r"Erro relativo do estimador de $g(\alpha, a, b)$")
fig.text(0.04, 0.5, r"$\frac{|\hat{g}_n - g(\alpha, a, b)|}{g(\alpha, a, b)}$", va='center', rotation='vertical')
fig.text(0.5, 0.04, "Número de amostras n", ha='center')

a_idx = 0
for alpha in alpha_values:
    def f(x):
        return x**alpha
    b_idx = 0
    for a in a_values:
        for b in b_values:
            n_values = []
            g_error = []
            g = ( b**(alpha+1) - a**(alpha+1) )/(alpha+1)

            for exp in range(n_max+1):
                n = 10**exp
                n_values += [n]

                soma = 0
                for i in range(n):
                    x = a + random()*(b-a)
                    y = random()*f(b)

                    if y <= f(x):
                        soma += 1
                Mn = soma/float(n)

                g_til = Mn*f(b)*(b-a)
                #print(g_til)

                g_error += [ abs(g_til - g)/g ]

            ax[a_idx][b_idx].semilogx(n_values, g_error, color=color[a_idx][b_idx])

            info = r"\begin{eqnarray*}" + \
                   r"&\alpha& = {} \\ " \
                   r"&a& = {} \\ " \
                   r"&b& = {}".format(alpha,a,b) + \
                   r"\end{eqnarray*}"
            ax[a_idx][b_idx].text(.7,.5, info, transform=ax[a_idx][b_idx].transAxes)
            ax[a_idx][b_idx].grid(which="both")

            b_idx += 1
    a_idx += 1

plt.savefig("Imagens/q6_integracaoMC")
plt.show()