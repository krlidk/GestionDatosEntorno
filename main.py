import os

def check_data_quality():
    print("--- Iniciando análisis de calidad de datos ---")
    # Aquí simularíamos la lógica de IA o Datos
    data = [10, 20, None, 40]
    nulos = data.count(None)
    print(f"Resultado: Se encontraron {nulos} valores nulos.")

if __name__ == "__main__":
    check_data_quality()