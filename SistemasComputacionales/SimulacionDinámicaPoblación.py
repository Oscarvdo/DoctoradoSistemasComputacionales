import matplotlib.pyplot as plt

# Parámetros iniciales
initial_population = 100
carrying_capacity = 1000  # Capacidad de carga del entorno
growth_rate = 0.1  # Tasa de crecimiento
time_steps = 100

# Lista para almacenar el tamaño de la población en cada paso de tiempo
population = [initial_population]

# Función para simular la dinámica de la población con control de retroalimentación
def simulate_population(population, growth_rate, carrying_capacity, time_steps):
    for t in range(1, time_steps):
        current_population = population[-1]
        growth = growth_rate * current_population * (1 - current_population / carrying_capacity)
        new_population = current_population + growth
        population.append(new_population)

simulate_population(population, growth_rate, carrying_capacity, time_steps)

# Visualizar los resultados
plt.figure(figsize=(10, 6))
plt.plot(population, label='Tamaño de la población')
plt.axhline(y=carrying_capacity, color='r', linestyle='--', label='Capacidad de carga')
plt.xlabel('Tiempo')
plt.ylabel('Tamaño de la población')
plt.title('Simulación de Dinámica de Población con Retroalimentación')
plt.legend()
plt.show()
