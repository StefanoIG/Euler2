import numpy as np
import matplotlib.pyplot as plt

# Definición de la ecuación diferencial
def f(t, y):
    return t - y

# Condiciones iniciales
t0 = 0.0
y0 = 1.0

# Intervalo de tiempo
t_final = 2.0

# Tamaños de paso
h1 = 0.5
h2 = 0.25

# Número de pasos
num_pasos1 = int((t_final - t0) / h1)
num_pasos2 = int((t_final - t0) / h2)

# Arreglos para almacenar resultados
t1 = np.zeros(num_pasos1 + 1)
y1 = np.zeros(num_pasos1 + 1)
t2 = np.zeros(num_pasos2 + 1)
y2 = np.zeros(num_pasos2 + 1)

# Inicializar condiciones iniciales
t1[0] = t0
y1[0] = y0
t2[0] = t0
y2[0] = y0

# Método de Euler con h = 0.5
for i in range(num_pasos1):
    t1[i + 1] = t1[i] + h1
    y1[i + 1] = y1[i] + h1 * f(t1[i], y1[i])

# Método de Euler con h = 0.25
for i in range(num_pasos2):
    t2[i + 1] = t2[i] + h2
    y2[i + 1] = y2[i] + h2 * f(t2[i], y2[i])

    for i in range(num_pasos1 + 1):
        print(f"T(h=0.5) = {t1[i]:.1f} , Y(h=0.5) = {y1[i]:.2f} ")

for i in range(num_pasos2 + 1):
    print(f"T(h=0.25) = {t2[i]:.1f} , Y(h=0.25) = {y2[i]:.2f} ")


# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(t1, y1, label=f'Método de Euler (h = {h1})')
plt.plot(t2, y2, label=f'Método de Euler (h = {h2})')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Solución de la Ecuación Diferencial')
plt.show()







