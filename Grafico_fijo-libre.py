import Graphing
import numpy as np
import sympy as sp

sp.init_printing()

N = 10      # cantidad de masas a simular

L = 10       # largo L
T_0 = 4      # tension promedio de la cuerda en reposo
rho = 0.1    # densidad lineal de la cuerda

modoMaximoRepresentado = 100

h = L/(N+1)
c = np.sqrt(T_0/rho)
c_rara = np.sqrt(T_0/(rho*(h**2)))

def construccion_matriz(i, j):
    if (i == 1 and j == 0):
        return -c_rara
    if j == N:
        if i == N-2:
            return -c_rara
        elif i == N-1:
            return 2*c_rara
        else:
            return 0
    elif i == 0 or j == 0 or i == N or j == N:
        return 0
    elif i == j:
        return 2*c_rara
    elif i+1 == j:
        return -c_rara
    elif i-1 == j:
        return -c_rara
    else:
        return 0

M = sp.Matrix(N+1, N+1, construccion_matriz)
# Psi = A*cos(wt) con vector A=autovec del modo (cada componente de A es amplitud de una masa) y w=sqrt(autoval)

sp.pprint(M)

eigenvals = [] # los autovalores son las frecuencias cuadradas
eigenvects = []
for eigenval in M.eigenvals():
    eigenvals.append(eigenval)
for eigenvect in M.eigenvects():
    eigenvects.append(eigenvect[2][0])

modo_normal = 3
assert(False)
def calc_psi(A, w, t):
    return A#A*np.cos(w*t)

X = np.array(range(N+1))
Y = np.array(eigenvects)

g = Graphing.Graphing2D(X, Y[1], Y[2], Y[3], Y[4], Y[5], Y[6], Y[7], Y[8], Y[9])
for i in range(1, 10):
    g.add_scatter(0, i)
    g.add_plot(0, i)
    g.set_title('modo {0}'.format(i))
    g.show()