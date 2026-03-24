import os
import psycopg2
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

def check_data_quality():
    # Tu lógica original
    data = [10, 20, None, 40]
    nulos = data.count(None)
    
    db_url = os.getenv("DB_URL")
    status_db = "No conectada"
    
    try:
        conn = psycopg2.connect(db_url)
        status_db = "✅ Conexión Exitosa a Supabase"
        conn.close()
    except Exception as e:
        status_db = f"❌ Error: {e}"
    
    return f"Resultado: {nulos} nulos encontrados. Estado DB: {status_db}"

@app.route('/')
def home():
    # Al entrar a la URL, se ejecuta tu análisis
    resultado = check_data_quality()
    return f"<h1>Analizador de Datos IA</h1><p>{resultado}</p>"

if __name__ == "__main__":
    # Render asigna un puerto automáticamente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)