# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 18:55:45 2025

@author: marce
"""

# --------------- CONDICIONALES CON AND/OR ---------------

print("\n\n>>> OPERADORES LÓGICOS")
print("-" * 40)

def evaluar_condiciones_riego(temp, humedad, viento):
    """Evalúa si es apropiado regar"""
    if temp > 30 and humedad < 15:
        return "RIEGO URGENTE - Alta temperatura y baja humedad"
    elif (temp > 25 or humedad < 20) and viento < 15:
        return "Riego recomendado"
    elif viento > 20:
        return "NO REGAR - Viento muy fuerte"
    else:
        return "Condiciones normales"

# Evaluar diferentes escenarios
print("Evaluación de condiciones de riego:")
print(f"T=32°C, H=12%, V=8km/h: {evaluar_condiciones_riego(32, 12, 8)}")
print(f"T=26°C, H=18%, V=10km/h: {evaluar_condiciones_riego(26, 18, 10)}")
print(f"T=24°C, H=25%, V=25km/h: {evaluar_condiciones_riego(24, 25, 25)}")
