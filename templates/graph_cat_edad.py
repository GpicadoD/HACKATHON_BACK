import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel
def cargar_datos(ruta):
    xls = pd.ExcelFile(ruta)
    df = pd.read_excel(xls, sheet_name="Consulta")
    return df

# Generar gráfico de barras de la distribución de categorías de edad
def graficar_categorias_edad(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, y="CategoríaEdad", order=df["CategoríaEdad"].value_counts().index, palette="viridis")
    plt.xlabel("Cantidad")
    plt.ylabel("Categoría de Edad")
    plt.title("Distribución de Categorías de Edad")
    plt.show()

# Ruta del archivo Excel
file_path = r"C:\Users\Xinwei\Documents\Proyecto The Wave\data\SetDatosEnviar_2.xlsx"  # Ajustar la ruta según sea necesario

df = cargar_datos(file_path)
graficar_categorias_edad(df)
