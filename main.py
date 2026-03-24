import os
import psycopg2
from dotenv import load_dotenv

# 1. Cargamos las variables de entorno del archivo .env 
load_dotenv()

def check_data_quality():
    print("--- Iniciando análisis de calidad de datos ---")
    
    # Lógica de IA/Datos que ya tenías
    data = [10, 20, None, 40]
    nulos = data.count(None)
    print(f"Resultado local: Se encontraron {nulos} valores nulos.")
    
    # 2. Intentamos conectar con Supabase (PostgreSQL) [cite: 11]
    db_url = os.getenv("DB_URL")
    
    if not db_url:
        print("Error: No se encontró la variable DB_URL en el entorno.")
        return

    try:
        # Establecemos la conexión real
        conn = psycopg2.connect(db_url)
        print("✅ Conexión exitosa a la base de datos en la nube (Supabase).")
        
        # Opcional: Podrías insertar el resultado del análisis en una tabla aquí
        # para demostrar trazabilidad y escalabilidad.
        
        conn.close()
    except Exception as e:
        print(f"❌ Error al conectar con la base de datos: {e}")

if __name__ == "__main__":
    check_data_quality()