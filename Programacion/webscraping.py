from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import re
import string

# Paso 1: Obtener el contenido HTML desde la URL
try:
    ImparcialFile = urllib.request.urlopen('https://www.elimparcial.com/')
    ImparcialHtml = ImparcialFile.read()
    ImparcialFile.close()
except urllib.error.HTTPError as e:
    print("Error HTTP:", e.code, e.reason)
    raise

# Paso 2: Analizar el HTML utilizando BeautifulSoup
soup = BeautifulSoup(ImparcialHtml, 'html.parser')
ImparcialAll = soup.find_all('a')

# Paso 3: Filtrar los enlaces que contienen 'locurioso'
fuente = []
enlace = []

for link in ImparcialAll:
    href = link.get('href')
    if href and 'locurioso' in href:
        print(href)
        fuente.append('el imparcial')
        enlace.append(href)

# Crear un DataFrame usando los datos recolectados
df = pd.DataFrame({'fuente': fuente, 'enlace': enlace})

# Paso 4: Función para preprocesar el texto
def preprocess(texto):
    texto = texto.lower()  # Convertir a minúsculas
    texto = texto.strip()  # Eliminar espacios en blanco al inicio y final
    texto = re.compile('<.*?>').sub('', texto)  # Eliminar etiquetas HTML
    texto = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', texto)  # Eliminar puntuación
    texto = re.sub(r'\d', ' ', texto)  # Eliminar números
    texto = re.sub('\s+', ' ', texto)  # Reemplazar múltiples espacios con uno solo
    return texto

# Paso 5: Función para extraer texto de un enlace dado
def extraer_texto(enlace):
    nota = 'https://www.elimparcial.com' + enlace
    print(nota)
    texto = ''
    try:
        ImparcialFile = urllib.request.urlopen(nota)
        ImparcialHtml = ImparcialFile.read()
        ImparcialFile.close()
        soup = BeautifulSoup(ImparcialHtml, 'html.parser')
        ImparcialAll = soup.find_all('p')
        for etiqueta in ImparcialAll:
            texto += str(etiqueta)
    except Exception as e:
        print(f"Error al extraer texto: {e}")
    return texto

# Paso 6: Extraer y preprocesar el texto para cada enlace
noticias = []
for index, row in df.iterrows():
    enlace = row['enlace']
    try:
        texto = extraer_texto(enlace)
        texto = preprocess(texto)
        noticias.append(texto)
    except Exception as e:
        print(f"Error en el enlace {enlace}: {e}")
        noticias.append(None)

df['noticias'] = noticias

# Paso 7: Limpiar el DataFrame
df = df.dropna()  # Eliminar filas con valores nulos
df = df.drop_duplicates()  # Eliminar filas duplicadas

# Paso 8: Guardar el DataFrame final en un archivo CSV
df.to_csv('tendencias_elimparcial.csv', index=False)

# Paso 9: Imprimir el DataFrame para verificar
print(df.head())
