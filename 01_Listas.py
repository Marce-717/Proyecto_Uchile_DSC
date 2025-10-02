# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 18:38:33 2025

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
# 1. ESTRUCTURAS DE DATOS
# =============================================================================

print("=" * 60)
print("1. ESTRUCTURAS DE DATOS")
print("=" * 60)

# --------------- LISTAS ---------------
print("\n>>> LISTAS (list)")
print("-" * 40)

# Datos de rendimiento de parcelas (ton/ha)
rendimientos = [4.5, 5.2, 3.8, 6.1, 4.9]
print(f"Rendimientos iniciales: {rendimientos}")

# Agregar nueva medición
rendimientos.append(5.5)
print(f"Después de append(5.5): {rendimientos}")

# Insertar en posición específica
rendimientos.insert(0, 4.0)
print(f"Después de insert(0, 4.0): {rendimientos}")

# Calcular estadísticas básicas
promedio = sum(rendimientos) / len(rendimientos)
maximo = max(rendimientos)
minimo = min(rendimientos)

print(f"\nEstadísticas:")
print(f"  Promedio: {promedio:.2f} ton/ha")
print(f"  Máximo: {maximo} ton/ha")
print(f"  Mínimo: {minimo} ton/ha")

# Slicing - obtener primeras 3 parcelas
primeras_tres = rendimientos[0:3]
print(f"\nPrimeras 3 parcelas: {primeras_tres}")