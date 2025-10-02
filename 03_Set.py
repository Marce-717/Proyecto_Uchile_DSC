# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 18:48:53 2025

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

# --------------- SETS ---------------

print("\n\n>>> SETS (set)")
print("-" * 40)

# Especies encontradas en diferentes parcelas
parcela_a = {"trigo", "maleza_1", "maleza_2", "avena"}
parcela_b = {"trigo", "maleza_2", "maleza_3", "cebada"}

print(f"Parcela A: {parcela_a}")
print(f"Parcela B: {parcela_b}")

# Especies en común (intersección)
especies_comunes = parcela_a.intersection(parcela_b)
print(f"\nEspecies comunes: {especies_comunes}")

# Todas las especies (unión)
todas_especies = parcela_a.union(parcela_b)
print(f"Todas las especies: {todas_especies}")

# Especies únicas de parcela A
unicas_a = parcela_a.difference(parcela_b)
print(f"Únicas en parcela A: {unicas_a}")