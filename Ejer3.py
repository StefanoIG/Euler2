import numpy as np

# Definimos la ecuación dy/dt = -k*sqrt(y)
def derivative(y, k):
    return -k * np.sqrt(y)

# Parámetros iniciales
y0 = 3.0  # Nivel inicial del agua en metros
k = 0.06  # Constante k
dt = 0.5  # Paso de tiempo en minutos
t = 0.0  # Tiempo inicial

# Lista para almacenar los valores de y en cada paso
y_values = [y0]

# Lista para almacenar los valores de t en cada paso
t_values = [t]

# Número total de pasos
num_steps = int(3.0 / dt)  # Tiempo total de 3 minutos

# Aplicamos el método de Euler
for _ in range(num_steps):
    y_new = y_values[-1] + dt * derivative(y_values[-1], k)
    t += dt
    y_values.append(y_new)
    t_values.append(t)

# Imprimimos los resultados
for i, (ti, yi) in enumerate(zip(t_values, y_values)):
    print(f"Tiempo: {ti} minutos, Nivel de agua: {yi:.2f} metros")

# Tiempo total requerido para vaciar el tanque
total_time = t_values[-1]
print(f"Tiempo total requerido para vaciar el tanque: {total_time:.2f} minutos")
