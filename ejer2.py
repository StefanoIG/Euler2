import numpy as np
import matplotlib.pyplot as plt

# Definición de la ecuación diferencial
def f(x, y):
    return (1 + 4 * x) * np.sqrt(y)

# Condiciones iniciales
x0 = 0.0
y0 = 1.0
h = 0.25

# Intervalo de tiempo
x_final = 1.0

# Número de pasos
num_pasos = int((x_final - x0) / h)

# Arreglos para almacenar resultados
x = np.zeros(num_pasos + 1)
y = np.zeros(num_pasos + 1)

# Inicializar condiciones iniciales
x[0] = x0
y[0] = y0

# Método de Euler
for i in range(num_pasos):
    x[i + 1] = x[i] + h
    y[i + 1] = y[i] + h * f(x[i], y[i])

    for i in range(num_pasos + 1):
        print(f"X(h=0.25) = {x[i]:.1f} , Y(h=0.25) = {y[i]:.2f} ")

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Método de Euler (h = 0.25)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Solución de la Ecuación Diferencial')
plt.show()
