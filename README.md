# Documentación Técnica: Preparación del Entorno para Soluciones de IA
**Asignatura:** ITY1101 - Gestión de Datos para IA 
**Resultado de Aprendizaje:** RA1 (IL 1.3) 

## 1. Propósito de la Actividad
El objetivo principal es configurar un entorno técnico completo en la nube que integre herramientas reales para el desarrollo de soluciones basadas en datos e inteligencia artificial. El enfoque busca garantizar una base sólida con trazabilidad y escalabilidad.

## 2. Stack Tecnológico Seleccionado
Para esta solución se implementaron las siguientes herramientas esenciales]:

| Herramienta | Función |
| :--- | :--- |
| **GitHub** | Sistema de control de versiones y repositorio central. |
| **VS Code / Codespaces** | Editor de código y entorno de desarrollo en la nube. |
| **Docker** | Contenerización para asegurar la portabilidad del entorno. |
| **GitHub Actions** | Automatización de pipelines de Integración Continua (CI/CD). |
| **Supabase (PostgreSQL)** | Base de datos en la nube para persistencia de datos. |
| **Render** | Plataforma de despliegue para la ejecución del servicio web. |

## 3. Pasos de Implementación
Se siguieron las fases sugeridas para la configuración del entorno:

1.  **Estructura Base:** Creación del repositorio y configuración de archivos de control (`.gitignore`, `.env.example`).
2.  **Contenerización:** Redacción del `Dockerfile` para estandarizar la ejecución del "Analizador de Calidad de Datos".
3.  **Automatización:** Configuración de un pipeline en GitHub Actions (`ci.yml`) que valida el código en cada actualización.
4.  **Integración de Datos:** Conexión mediante el Connection Pooler de Supabase para asegurar compatibilidad de red y escalabilidad.
5.  **Despliegue:** Publicación de un micro-servicio Flask en Render para mantener la disponibilidad del servicio.

## 4. Decisiones Técnicas y Trazabilidad
* **Uso de Flask:** Se decidió implementar un servidor web para evitar que el proceso finalizara prematuramente en Render y permitir el monitoreo en tiempo real del análisis.
* **Variables de Entorno:** Se implementó `python-dotenv` para separar las credenciales sensibles del código fuente, siguiendo estándares de seguridad.
* **Dockerización:** Se utilizó para garantizar que el modelo de IA o análisis de datos corra idénticamente en desarrollo y producción.

## 5. Resultados del Despliegue 
* **URL de Producción:** https://gestiondatosentorno.onrender.com
* **Estado de la Base de Datos:** Conectada vía Supabase.

## 6. Investigación de Alternativas 
Como parte del trabajo autónomo, se identificaron herramientas alternativas que podrían cumplir funciones similares:
* **Despliegue:** Railway o Vercel.
* **Base de Datos:** MongoDB Atlas o PlanetScale.
* **CI/CD:** GitLab CI o CircleCI.
