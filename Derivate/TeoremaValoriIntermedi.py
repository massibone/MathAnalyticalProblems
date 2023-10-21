
'''
se una funzione è continua in un intervallo chiuso e limitato di ℝ, allora la funzione assume ogni valore tra il valore minimo e il valore massimo della funzione in quell'intervallo. 
'''
import numpy as np
import matplotlib.pyplot as plt

# Definizione di una funzione continua su un intervallo
def funzione(x):
    return x**3 - 3*x**2 + 2

# Intervallo chiuso e limitato
intervallo_inizio = -1
intervallo_fine = 3
