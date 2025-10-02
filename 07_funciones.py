# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 19:10:20 2025

@author: marce
"""
"""
Autor: Marcelo Toro Miranda

"""
"""
FUNDAMENTOS DE PROGRAMACIÓN EN PYTHON
Data Science en Sistemas Naturales
Facultad de Ciencias Agronómicas - Universidad de Chile

Ejemplos prácticos para agricultura de precisión y sistemas agropecuarios

"""


# =============================================================================
# 4. FUNCIONES
# =============================================================================

print("\n\n" + "=" * 60)
print("4. FUNCIONES")
print("=" * 60)

# --------------- FUNCIONES BÁSICAS ---------------

print("\n>>> FUNCIONES BÁSICAS")
print("-" * 40)

def calcular_area_terreno(largo, ancho):
    """Calcula el área de un terreno rectangular"""
    return largo * ancho

# Usar la función
largo_m = 250
ancho_m = 180
area = calcular_area_terreno(largo_m, ancho_m)
area_ha = area / 10000

print(f"Terreno de {largo_m}m x {ancho_m}m")
print(f"Área: {area} m² = {area_ha} ha")


# --------------- FUNCIÓN CON MÚLTIPLES PARÁMETROS ---------------


print("\n\n>>> FUNCIÓN CON PARÁMETROS POR DEFECTO")
print("-" * 40)

def calcular_dosis_fertilizante(area_ha, dosis_kg_ha=150, eficiencia=0.85):
    """
    Calcula cantidad de fertilizante necesaria
    
    Parámetros:
        area_ha: Área en hectáreas
        dosis_kg_ha: Dosis por hectárea (default 150 kg/ha)
        eficiencia: Eficiencia de aplicación (default 0.85)
    """
    cantidad_teorica = area_ha * dosis_kg_ha
    cantidad_real = cantidad_teorica / eficiencia
    return cantidad_real

# Usar con valores por defecto
print(f"10 ha con valores por defecto: {calcular_dosis_fertilizante(10):.1f} kg")

# Usar con valores personalizados
print(f"10 ha, 200 kg/ha: {calcular_dosis_fertilizante(10, 200):.1f} kg")
print(f"10 ha, 200 kg/ha, 90% efic: {calcular_dosis_fertilizante(10, 200, 0.90):.1f} kg")


# --------------- FUNCIÓN CON RETORNO MÚLTIPLE ---------------


print("\n\n>>> FUNCIÓN CON RETORNO MÚLTIPLE")
print("-" * 40)

def analizar_rendimientos(rendimientos):
    """Analiza una lista de rendimientos y retorna estadísticas"""
    promedio = sum(rendimientos) / len(rendimientos)
    maximo = max(rendimientos)
    minimo = min(rendimientos)
    rango = maximo - minimo
    
    return promedio, maximo, minimo, rango

# Usar la función
datos = [4.5, 5.2, 3.8, 6.1, 4.9]
prom, max_r, min_r, rango = analizar_rendimientos(datos)

print("Análisis de rendimientos:")
print(f"  Promedio: {prom:.2f} ton/ha")
print(f"  Máximo: {max_r} ton/ha")
print(f"  Mínimo: {min_r} ton/ha")
print(f"  Rango: {rango} ton/ha")


# --------------- FUNCIÓN PARA ÍNDICES DE VEGETACIÓN ---------------


print("\n\n>>> FUNCIÓN PARA AGRICULTURA DE PRECISIÓN")
print("-" * 40)

def calcular_ndvi(nir, red):
    """
    Calcula el Índice de Vegetación de Diferencia Normalizada (NDVI)
    
    Parámetros:
        nir: Reflectancia en infrarrojo cercano
        red: Reflectancia en rojo
        
    Retorna:
        NDVI: Valor entre -1 y 1
    """
    if (nir + red) == 0:
        return 0
    
    ndvi = (nir - red) / (nir + red)
    return ndvi

def clasificar_ndvi(ndvi):
    """Clasifica el valor NDVI"""
    if ndvi < 0.2:
        return "Suelo desnudo o agua"
    elif ndvi < 0.4:
        return "Vegetación escasa"
    elif ndvi < 0.6:
        return "Vegetación moderada"
    else:
        return "Vegetación densa y saludable"

# Simular lecturas de diferentes zonas
zonas = [
    {"nombre": "Zona A", "nir": 0.45, "red": 0.15},
    {"nombre": "Zona B", "nir": 0.52, "red": 0.12},
    {"nombre": "Zona C", "nir": 0.38, "red": 0.18},
]

print("Análisis NDVI por zona:")
for zona in zonas:
    ndvi = calcular_ndvi(zona["nir"], zona["red"])
    clasificacion = clasificar_ndvi(ndvi)
    print(f"  {zona['nombre']}: NDVI = {ndvi:.3f} - {clasificacion}")


# --------------- FUNCIÓN COMPLEJA ---------------


print("\n\n>>> FUNCIÓN DE RECOMENDACIÓN DE FERTILIZACIÓN")
print("-" * 40)

def recomendar_fertilizacion(cultivo, ph, nitrogeno_ppm, fosforo_ppm, potasio_ppm):
    """
    Recomienda dosis de fertilización según análisis de suelo
    
    Retorna un diccionario con recomendaciones
    """
    recomendacion = {
        "cultivo": cultivo,
        "ajuste_ph": "No requerido",
        "nitrogeno_kg_ha": 0,
        "fosforo_kg_ha": 0,
        "potasio_kg_ha": 0,
        "observaciones": []
    }
    
    # Ajuste de pH
    if ph < 5.5:
        recomendacion["ajuste_ph"] = f"Aplicar cal: {(6.0 - ph) * 1000:.0f} kg/ha"
        recomendacion["observaciones"].append("pH bajo - priorizar encalado")
    elif ph > 7.5:
        recomendacion["ajuste_ph"] = "Aplicar azufre elemental"
        recomendacion["observaciones"].append("pH alto - puede limitar disponibilidad")
    
    # Recomendación de N según cultivo
    if cultivo == "maíz":
        if nitrogeno_ppm < 20:
            recomendacion["nitrogeno_kg_ha"] = 200
        elif nitrogeno_ppm < 40:
            recomendacion["nitrogeno_kg_ha"] = 150
        else:
            recomendacion["nitrogeno_kg_ha"] = 100
    elif cultivo == "trigo":
        if nitrogeno_ppm < 20:
            recomendacion["nitrogeno_kg_ha"] = 150
        elif nitrogeno_ppm < 40:
            recomendacion["nitrogeno_kg_ha"] = 100
        else:
            recomendacion["nitrogeno_kg_ha"] = 80
    
    # Recomendación de P
    if fosforo_ppm < 10:
        recomendacion["fosforo_kg_ha"] = 80
        recomendacion["observaciones"].append("Nivel de P crítico")
    elif fosforo_ppm < 20:
        recomendacion["fosforo_kg_ha"] = 50
    else:
        recomendacion["fosforo_kg_ha"] = 30
    
    # Recomendación de K
    if potasio_ppm < 100:
        recomendacion["potasio_kg_ha"] = 100
        recomendacion["observaciones"].append("Nivel de K bajo")
    elif potasio_ppm < 200:
        recomendacion["potasio_kg_ha"] = 60
    else:
        recomendacion["potasio_kg_ha"] = 40
    
    return recomendacion

# Probar la función
resultado = recomendar_fertilizacion(
    cultivo="maíz",
    ph=5.2,
    nitrogeno_ppm=18,
    fosforo_ppm=8,
    potasio_ppm=95
)

print(f"Recomendación para {resultado['cultivo']}:")
print(f"  Ajuste de pH: {resultado['ajuste_ph']}")
print(f"  Nitrógeno: {resultado['nitrogeno_kg_ha']} kg/ha")
print(f"  Fósforo: {resultado['fosforo_kg_ha']} kg/ha")
print(f"  Potasio: {resultado['potasio_kg_ha']} kg/ha")

if resultado['observaciones']:
    print("  Observaciones:")
    for obs in resultado['observaciones']:
        print(f"    - {obs}")
