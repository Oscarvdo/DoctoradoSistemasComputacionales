from cryptography.fernet import Fernet

# Generar una clave de cifrado
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as clave_file:
        clave_file.write(clave)

# Cargar la clave de cifrado
def cargar_clave():
    return open("clave.key", "rb").read()

# Encriptar datos
def encriptar_datos(datos):
    clave = cargar_clave()
    f = Fernet(clave)
    datos_encriptados = f.encrypt(datos.encode())
    return datos_encriptados

# Desencriptar datos
def desencriptar_datos(datos_encriptados):
    clave = cargar_clave()
    f = Fernet(clave)
    datos_desencriptados = f.decrypt(datos_encriptados).decode()
    return datos_desencriptados

# Generar y guardar una clave de cifrado (esto se hace una vez)
generar_clave()

# Datos sensibles (por ejemplo, un registro de paciente)
datos_sensibles = "Nombre: Juan Perez, Diagnóstico: Hipertensión, Medicamentos: Amlodipino"

# Encriptar los datos
datos_encriptados = encriptar_datos(datos_sensibles)
print(f"Datos encriptados: {datos_encriptados}")

# Desencriptar los datos
datos_desencriptados = desencriptar_datos(datos_encriptados)
print(f"Datos desencriptados: {datos_desencriptados}")

