# Ejemplo de optimización para tu servicio de Supabase
import asyncio
from concurrent.futures import ThreadPoolExecutor
import httpx
from typing import List

# Pool de threads para operaciones de I/O
thread_pool = ThreadPoolExecutor(max_workers=4)


async def subir_imagen_async(nombre_archivo: str, contenido: bytes) -> str:
    """Versión asíncrona de subir imagen"""
    loop = asyncio.get_event_loop()

    # Ejecutar en thread pool para no bloquear
    return await loop.run_in_executor(
        thread_pool,
        subir_imagen_sync,
        nombre_archivo,
        contenido
    )


def subir_imagen_sync(nombre_archivo: str, contenido: bytes) -> str:
    """Tu función original de subir imagen (versión sincrónica)"""
    # Aquí va tu código actual de subir_imagen
    # Ejemplo:
    # supabase.storage.from_("imagenes").upload(nombre_archivo, contenido)
    # return url
    pass


async def subir_multiples_imagenes(archivos: List[dict]) -> List[str]:
    """Sube múltiples imágenes en paralelo"""
    tasks = []

    for archivo in archivos:
        task = subir_imagen_async(archivo['nombre'], archivo['contenido'])
        tasks.append(task)

    # Ejecutar todas las subidas en paralelo
    urls = await asyncio.gather(*tasks)
    return urls


# Alternativa usando httpx para requests asíncronos
async def subir_con_httpx(nombre_archivo: str, contenido: bytes) -> str:
    """Versión con httpx para requests completamente asíncrono"""
    async with httpx.AsyncClient(timeout=30.0) as client:
        # Tu lógica de subida usando httpx
        # response = await client.post(url, files={"file": contenido})
        # return response.json()["url"]
        pass