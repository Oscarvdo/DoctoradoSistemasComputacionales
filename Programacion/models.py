import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, roc_curve
from sklearn.preprocessing import LabelEncoder  # Importar LabelEncoder
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Función para calcular la curva Precision-Recall manualmente
def precision_recall_curve_manual(y_true, y_score):
    thresholds = np.linspace(0, 1, 100)
    precision_values = []
    recall_values = []

    for threshold in thresholds:
        y_pred = (y_score >= threshold).astype(int)
        true_positives = np.sum((y_true == 1) & (y_pred == 1))
        false_positives = np.sum((y_true == 0) & (y_pred == 1))
        false_negatives = np.sum((y_true == 1) & (y_pred == 0))

        precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
        recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0

        precision_values.append(precision)
        recall_values.append(recall)

    return np.array(precision_values), np.array(recall_values)

# Cargar el DataFrame desde el archivo CSV generado anteriormente
df = pd.read_csv('tendencias_elimparcial.csv')

# Eliminar filas con valores NaN en la columna 'noticias'
df = df.dropna(subset=['noticias'])

# Convertir textos de noticias en vectores numéricos
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['noticias'])

# Codificar la variable de destino y
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['categoria'])  # Codificar y

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir una lista de modelos a probar
modelos = {
    'Regresión Logística': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC()
}

# Entrenar y evaluar cada modelo
resultados = {'Modelo': [], 'Precisión': []}
mejor_modelo = None
mejor_precision = 0

for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    predicciones = modelo.predict(X_test)
    precision = accuracy_score(y_test, predicciones)
    resultados['Modelo'].append(nombre)
    resultados['Precisión'].append(precision)
    print(f"{nombre}: {precision}")
    if precision > mejor_precision:
        mejor_precision = precision
        mejor_modelo = nombre

print(f"El mejor modelo es: {mejor_modelo} con una precisión de {mejor_precision}")

# Mostrar los resultados como un DataFrame
resultados_df = pd.DataFrame(resultados)
print("\nTabla de Comparación:")
print(resultados_df)

# Gráfico de barras de la precisión de los modelos
plt.figure(figsize=(8, 6))
sns.barplot(x='Modelo', y='Precisión', data=resultados_df, palette='viridis')
plt.title('Precisión de Modelos de Aprendizaje Automático')
plt.ylim(0, 1)

output_dir = 'graficas'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

barplot_path = os.path.join(output_dir, 'barplot.png')
plt.savefig(barplot_path)
plt.close()

# Curva ROC para el mejor modelo (Regresión Logística)
mejor_modelo = modelos['Regresión Logística']
fpr, tpr, thresholds = roc_curve(y_test, mejor_modelo.predict_proba(X_test)[:, 1])

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label='ROC Curve')
plt.plot([0, 1], [0, 1], color='red', linestyle='--', label='Random Guessing')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Curva ROC para Regresión Logística')
plt.legend()

roc_curve_path = os.path.join(output_dir, 'roc_curve.png')
plt.savefig(roc_curve_path)
plt.close()

# Curva Precision-Recall para el mejor modelo (Regresión Logística)
precision, recall = precision_recall_curve_manual(y_test, mejor_modelo.predict_proba(X_test)[:, 1])

plt.figure(figsize=(8, 6))
plt.plot(recall, precision, color='green', label='Precision-Recall Curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Curva Precision-Recall para Regresión Logística')
plt.legend()
plt.grid(True)

precision_recall_curve_path = os.path.join(output_dir, 'precision_recall_curve.png')
plt.savefig(precision_recall_curve_path)
plt.close()

print("Gráficas guardadas en el directorio 'graficas'.")
