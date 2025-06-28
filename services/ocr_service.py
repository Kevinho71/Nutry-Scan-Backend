import os
import re
import json
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
from io import BytesIO

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("⚠️ No se encontró la variable GEMINI_API_KEY en el archivo .env")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')


def extract_json(texto):
    # Extrae JSON de bloque Markdown ```json ... ```
    match = re.search(r"```json(.*?)```", texto, re.DOTALL)
    contenido = match.group(1).strip() if match else texto.strip()

    try:
        return json.loads(contenido)
    except Exception as e:
        print("❌ Error al parsear JSON:", e)
        return {"error": "JSON inválido o no encontrado"}


async def analizar_ingredientes_por_imagen(files_data):
    """
    Analiza ingredientes desde datos de archivos ya leídos
    files_data: Lista de diccionarios con 'contenido', 'filename', 'content_type'
    """
    try:
        images = []

        # Procesar cada archivo desde el contenido ya leído
        for file_data in files_data[:2]:  # Solo se permiten hasta 2 imágenes
            image_bytes = file_data['contenido']
            image = Image.open(BytesIO(image_bytes))
            images.append(image)

        prompt = """
        Eres un nutricionista profesional. A partir de la o las imagenes del producto, extrae la siguiente información:

        1. Ingredientes listados en el orden original, con una breve descripción nutricional para cada uno.
        2. Nutrientes de la tabla nutricional por cada 100g, con su valor e interpretación profesional.
        3. Aditivos y su nivel de toxicidad, toma como referencia a la EFSA para la informacion
        4. Puntos positivos del producto.
        5. Advertencias relevantes (por ejemplo, alto en calorías, bajo en fibra, contiene alérgenos, etc.).

        Devuélvelo en el siguiente formato JSON (no escribas nada más fuera de este bloque):

        ```json
        {
          "ingredientes": [
            { "nombre": "Almidón de yuca", "descripcion": "Fuente de carbohidratos simples." }
          ],
          "tabla_nutricional": [
            { "nombre": "Carbohidratos", "valor": "69.1 g", "interpretacion": "Muy alto contenido de carbohidratos." }
          ],
          "Aditivos":[
            { "codigo": "(SIN 338)", "nombre": "Acido fosforico", "Toxicidad": "medio.", "Interpretacion": "Puede causar reacciones alérgicas en personas sensibles a los sulfitos." }
          ],
          "puntos_positivos": [
            "Buena fuente de calcio."
          ],
          "advertencias": [
            "Muy alto en calorías."
          ]
        }"""

        # Enviar todas las imágenes cargadas en una sola solicitud
        content = [prompt] + images
        response = model.generate_content(content)

        texto = response.text or ""
        print("📄 Ingredientes:\n", texto)
        return extract_json(texto)

    except Exception as e:
        print("🚨 Error analizando ingredientes:", e)
        return {"error": "Error al procesar imagen"}