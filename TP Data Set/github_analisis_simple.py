import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# Evitar errores de caracteres en Windows
sys.stdout.reconfigure(encoding="utf-8")

# 1. Descargar directamente desde Kaggle
path = kagglehub.dataset_download(
    "felkan228/metadata-of-the-top-1000-github-repositories"
)

print("Dataset descargado en:")
print(path)

# 2. Cargar el CSV
archivo = os.path.join(path, "top_1000_os_rules.csv")
df = pd.read_csv(archivo)

# 3. Tomar una muestra de 100 repositorios
df = df.sample(100, random_state=42)

# 4. Exploración
print("\nPrimeros registros:")
print(df.head())

print("\nCantidad de filas y columnas:")
print(df.shape)

print("\nValores nulos:")
print(df.isnull().sum())

print("\nRegistros duplicados:")
print(df.duplicated().sum())

# 5. Analizar los lenguajes
lenguajes = (
    df["language"]
    .fillna("Sin especificar")
    .value_counts()
)

print("\nLenguajes más utilizados:")
print(lenguajes)

# 6. Gráfico
lenguajes.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Lenguajes de programación en 100 repositorios de GitHub")
plt.xlabel("Lenguaje")
plt.ylabel("Cantidad de repositorios")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()