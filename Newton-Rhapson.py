def f(x):
    return x**4-10*x**3+3*x**2+x+23

def Df(x):
    return 4*x**3-30*x**2+6*x+1

x0 = 1
i = 1
error = 10
while error > 1e-7:
    x1 = x0 - f(x0) / Df(x0)
    error = abs(x1 - x0)
    x0 = x1
    print("Iteracion", i, ", raiz aproximada: ", x0)
    i = i + 1