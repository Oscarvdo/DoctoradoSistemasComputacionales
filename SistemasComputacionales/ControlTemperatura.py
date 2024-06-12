import random
import matplotlib.pyplot as plt

class Termostato:
    def __init__(self, set_point, k_p):
        self.set_point = set_point  # Temperatura deseada
        self.k_p = k_p  # Ganancia proporcional
        self.temperatura_actual = random.uniform(set_point - 5, set_point + 5)  # Temperatura inicial aleatoria

    def actualizar_temperatura(self):
        # Simulación de cambio de temperatura ambiental
        perturbacion = random.uniform(-0.5, 0.5)
        self.temperatura_actual += perturbacion
        
        # Calcular error
        error = self.set_point - self.temperatura_actual
        
        # Control proporcional
        ajuste = self.k_p * error
        
        # Actualizar temperatura
        self.temperatura_actual += ajuste
        
    def obtener_temperatura(self):
        return self.temperatura_actual

# Parámetros de la simulación
set_point = 22.0  # Temperatura deseada (°C)
k_p = 0.1  # Ganancia proporcional
num_iteraciones = 100  # Número de iteraciones de la simulación

# Crear instancia del termostato
termostato = Termostato(set_point, k_p)

# Listas para almacenar los resultados de la simulación
temperaturas = []

# Ejecutar la simulación
for _ in range(num_iteraciones):
    termostato.actualizar_temperatura()
    temperaturas.append(termostato.obtener_temperatura())

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(temperaturas, label='Temperatura Actual')
plt.axhline(y=set_point, color='r', linestyle='--', label='Set Point')
plt.xlabel('Iteraciones')
plt.ylabel('Temperatura (°C)')
plt.title('Simulación de Control de Temperatura')
plt.legend()
plt.show()
