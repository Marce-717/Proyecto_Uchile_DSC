# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 18:53:39 2025

@author: marce
"""

# =============================================================================
# 2. CONDICIONALES
# =============================================================================

print("\n\n" + "=" * 60)
print("2. CONDICIONALES")
print("=" * 60)

# --------------- IF SIMPLE ---------------
print("\n>>> IF SIMPLE")
print("-" * 40)

temperatura = 28
if temperatura > 25:
    print(f"Temperatura {temperatura}°C: Activar riego")


# --------------- IF-ELSE ---------------

print("\n\n>>> IF-ELSE")
print("-" * 40)

humedad_suelo = 15  # porcentaje

if humedad_suelo < 20:
    print(f"Humedad {humedad_suelo}%: RIEGO NECESARIO")
else:
    print(f"Humedad {humedad_suelo}%: Nivel adecuado")
    
    
# --------------- IF-ELIF-ELSE ---------------

print("\n\n>>> IF-ELIF-ELSE")
print("-" * 40)

def clasificar_ph(ph):
    """Clasifica el pH del suelo"""
    if ph < 5.5:
        return "Ácido - Requiere encalado"
    elif ph >= 5.5 and ph <= 6.5:
        return "Ligeramente ácido - Óptimo para mayoría de cultivos"
    elif ph > 6.5 and ph <= 7.5:
        return "Neutro - Excelente condición"
    elif ph > 7.5 and ph <= 8.5:
        return "Ligeramente alcalino - Monitorear disponibilidad de nutrientes"
    else:
        return "Alcalino - Requiere acidificación"

# Probar con diferentes valores
ph_valores = [4.8, 6.0, 7.2, 8.0, 9.0]
print("Clasificación de pH:")
for ph in ph_valores:
    clasificacion = clasificar_ph(ph)
    print(f"  pH {ph}: {clasificacion}")
