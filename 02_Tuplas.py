# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 18:47:47 2025

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

# --------------- TUPLAS ---------------

print("\n\n>>> TUPLAS (tuple)")
print("-" * 40)

# Coordenadas GPS de un punto (inmutable)
coordenada_campo = (-33.4569, -70.6483, 550)  # lat, lon, elevación
print(f"Coordenadas del campo: {coordenada_campo}")
print(f"Latitud: {coordenada_campo[0]}")
print(f"Longitud: {coordenada_campo[1]}")
print(f"Elevación: {coordenada_campo[2]} msnm")

# Múltiples puntos de muestreo
puntos_muestreo = [
    (-33.45, -70.65, 545),
    (-33.46, -70.64, 548),
    (-33.44, -70.66, 552)
]
print(f"\nTotal de puntos: {len(puntos_muestreo)}")