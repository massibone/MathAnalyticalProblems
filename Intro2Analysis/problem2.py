'''
trovare il limite della somma delle lunghezze delle ordinate della curva y = e^{-x} \cos(\pi x)y=e **−x  cos π x 
Per calcolare il limite della somma delle lunghezze delle ordinate della curva y = e^{-x} \cos(\pi x)y=e 
−x
 cos(πx) quando nn tende a infinito, possiamo considerare che le ordinate della curva sono definite nei punti x = 0, 1, 2, \ldots, nx=0,1,2,…,n. Possiamo approssimare la somma delle lunghezze delle ordinate con una somma di Riemann.

L'incremento \Delta xΔx tra due punti adiacenti sarà 11, poiché abbiamo punti equispaziati.
l limite della somma delle lunghezze delle ordinate della curva y = e^{-x} \cos(\pi x)y=e 
−x
 cos(πx) quando nn tende a infinito è 
e/e−1

'''
import math
import matplotlib.pyplot as plt

def function(x):
    return math.exp(-x) * math.cos(math.pi * x)

def riemann_sum(n):
    sum = 0
    x_values = []
    y_values = []
    delta_x = 1.0 / n
    for i in range(n + 1):
        x = i * delta_x
        sum += math.sqrt(1 + math.exp(-2 * x))
        x_values.append(x)
        y_values.append(function(x))
    return sum, x_values, y_values
