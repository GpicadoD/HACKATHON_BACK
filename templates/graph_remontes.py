import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel
def cargar_datos(ruta):
    xls = pd.ExcelFile(ruta)
    df = pd.read_excel(xls, sheet_name="Consulta")
    return df

# Generar gráfico de barras agrupado por remontes y categorías de edad
def graficar_remontes_por_edad(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x="Remonte", hue="CategoríaEdad", palette="viridis")
    plt.xlabel("Remonte")
    plt.ylabel("Cantidad")
    plt.title("Distribución de Grupos de Edad por Remonte")
    plt.xticks(rotation=45)
    plt.legend(title="Categoría de Edad")
    plt.show()

# Ruta del archivo Excel
file_path = r"C:\Users\Xinwei\Documents\Proyecto The Wave\data\SetDatosEnviar_2.xlsx"  # Ajustar la ruta según sea necesario

df = cargar_datos(file_path)
graficar_remontes_por_edad(df)
