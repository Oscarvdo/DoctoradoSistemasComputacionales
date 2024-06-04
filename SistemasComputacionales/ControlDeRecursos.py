import psutil
import time
import matplotlib.pyplot as plt

# Configuración inicial de límites de recursos
cpu_threshold = 80  # Porcentaje máximo de uso de CPU
memory_threshold = 80  # Porcentaje máximo de uso de memoria

# Función para monitorear y ajustar los recursos
def monitor_and_adjust():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    print(f"Uso de CPU: {cpu_usage}%")
    print(f"Uso de Memoria: {memory_usage}%")

    if cpu_usage > cpu_threshold:
        print("Advertencia: Uso de CPU alto. Ajustando tareas...")
        # Implementar lógica para reducir carga de CPU, por ejemplo, reduciendo prioridades de procesos
    if memory_usage > memory_threshold:
        print("Advertencia: Uso de Memoria alto. Liberando memoria...")
        # Implementar lógica para liberar memoria, por ejemplo, cerrando aplicaciones no críticas

    return cpu_usage, memory_usage

# Monitorear y ajustar en un bucle continuo
cpu_usages = []
memory_usages = []
for _ in range(10):
    cpu, memory = monitor_and_adjust()
    cpu_usages.append(cpu)
    memory_usages.append(memory)
    time.sleep(5)  # Intervalo de tiempo entre chequeos

# Visualizar los resultados
plt.figure(figsize=(10, 5))
plt.plot(cpu_usages, label='Uso de CPU (%)')
plt.plot(memory_usages, label='Uso de Memoria (%)')
plt.axhline(y=cpu_threshold, color='r', linestyle='--', label='Umbral CPU')
plt.axhline(y=memory_threshold, color='b', linestyle='--', label='Umbral Memoria')
plt.xlabel('Tiempo (intervalos de 5 segundos)')
plt.ylabel('Porcentaje de Uso')
plt.title('Monitoreo y Ajuste de Recursos')
plt.legend()
plt.show()
