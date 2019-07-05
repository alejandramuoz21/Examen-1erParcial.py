import numpy as np
def f(x):
    return x - np.sin(x)
a = 0
b = 4
error = 10
i = 0
while error > 1e-8:
    c = (a + b) / 2
    fa = f(a)
    fc = f(c)
    if fc == 0:
        raiz = c
        break
    elif fa * fc < 0:
        b = c
    else:
        a = c
    raiz = c
    i += 1
    error = abs(fc)
    print("Iteracion", i, ".Raiz aproximada: ", raiz)