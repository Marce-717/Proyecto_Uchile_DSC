# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 18:50:56 2025

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

# --------------- DICCIONARIOS ---------------

print("\n\n>>> DICCIONARIOS (dict)")
print("-" * 40)

# Datos de análisis de suelo
analisis_suelo = {
    "ph": 6.5,
    "materia_organica": 3.2,
    "nitrogeno": 45,
    "fosforo": 12,
    "potasio": 180,
    "textura": "franco",
    "profundidad": 30
}

print("Análisis de suelo:")
for parametro, valor in analisis_suelo.items():
    print(f"  {parametro}: {valor}")

# Acceso seguro con get()
conductividad = analisis_suelo.get("conductividad", "No medido")
print(f"\nConductividad eléctrica: {conductividad}")

# Diccionario de parcelas
parcelas = {
    "P001": {"cultivo": "maíz", "area_ha": 12.5, "rendimiento": 8.2},
    "P002": {"cultivo": "trigo", "area_ha": 15.0, "rendimiento": 5.5},
    "P003": {"cultivo": "maíz", "area_ha": 10.0, "rendimiento": 7.8}
}

print("\nInformación de parcelas:")
for codigo, datos in parcelas.items():
    print(f"{codigo}: {datos['cultivo']} - {datos['area_ha']} ha - {datos['rendimiento']} ton/ha")