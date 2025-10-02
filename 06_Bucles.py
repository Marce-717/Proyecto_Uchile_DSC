# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 18:57:35 2025

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
# 3. BUCLES (LOOPS)
# =============================================================================

print("\n\n" + "=" * 60)
print("3. BUCLES")
print("=" * 60)

# --------------- WHILE ---------------


print("\n>>> BUCLE WHILE")
print("-" * 40)

# Simulación de crecimiento de planta
altura_planta = 0
dia = 0
tasa_crecimiento = 2.5  # cm por día

print("Crecimiento de planta:")
while altura_planta < 50:
    dia += 1
    altura_planta += tasa_crecimiento
    print(f"  Día {dia}: {altura_planta:.1f} cm")
    
    if dia > 30:  # Seguridad para evitar bucle infinito
        print("  (Simulación limitada a 30 días)")
        break

print(f"Planta alcanzó {altura_planta:.1f} cm en {dia} días")

# --------------- FOR CON LISTAS ---------------



print("\n\n>>> BUCLE FOR - Listas")
print("-" * 40)

# Análisis de múltiples parcelas
rendimientos_parcelas = [4.5, 5.2, 3.8, 6.1, 4.9, 5.5, 4.2]

print("Análisis de rendimientos:")
total = 0
parcelas_bajo_rendimiento = []

for i, rendimiento in enumerate(rendimientos_parcelas, 1):
    total += rendimiento
    estado = "✓ Normal" if rendimiento >= 4.5 else "⚠ Bajo"
    print(f"  Parcela {i}: {rendimiento} ton/ha - {estado}")
    
    if rendimiento < 4.5:
        parcelas_bajo_rendimiento.append(i)

promedio = total / len(rendimientos_parcelas)
print(f"\nPromedio general: {promedio:.2f} ton/ha")
print(f"Parcelas con bajo rendimiento: {parcelas_bajo_rendimiento}")


# --------------- FOR CON DICCIONARIOS ---------------


print("\n\n>>> BUCLE FOR - Diccionarios")
print("-" * 40)

# Inventario de maquinaria
maquinaria = {
    "Tractor John Deere": {"horas": 1250, "ultimo_mantenimiento": 1200},
    "Cosechadora Case": {"horas": 890, "ultimo_mantenimiento": 850},
    "Pulverizadora": {"horas": 520, "ultimo_mantenimiento": 300}
}

print("Estado de maquinaria:")
for equipo, datos in maquinaria.items():
    horas_desde_mant = datos["horas"] - datos["ultimo_mantenimiento"]
    
    if horas_desde_mant > 200:
        estado = "🔴 MANTENIMIENTO URGENTE"
    elif horas_desde_mant > 100:
        estado = "🟡 Programar mantenimiento"
    else:
        estado = "🟢 Buen estado"
    
    print(f"  {equipo}:")
    print(f"    Horas de uso: {datos['horas']}")
    print(f"    Horas desde mantenimiento: {horas_desde_mant}")
    print(f"    Estado: {estado}")


# --------------- FOR CON RANGE ---------------


print("\n\n>>> BUCLE FOR - Range")
print("-" * 40)

# Proyección de crecimiento poblacional de plaga
poblacion_inicial = 100
tasa_crecimiento_plaga = 1.15  # 15% por semana

print("Proyección de población de plaga:")
poblacion = poblacion_inicial

for semana in range(1, 9):
    poblacion *= tasa_crecimiento_plaga
    print(f"  Semana {semana}: {int(poblacion)} individuos")
    
    if poblacion > 500:
        print(f"    ⚠️ ALERTA: Umbral crítico alcanzado en semana {semana}")
        break


# --------------- CONTINUE Y BREAK ---------------


print("\n\n>>> CONTROL DE FLUJO - Continue y Break")
print("-" * 40)

# Procesar lecturas de sensores (ignorar valores erróneos)
lecturas_sensor = [25.5, -999, 26.1, 24.8, -999, 27.2, 25.9]

print("Lecturas válidas del sensor:")
suma = 0
contador = 0

for lectura in lecturas_sensor:
    if lectura == -999:  # Valor de error
        continue  # Saltar esta iteración
    
    print(f"  {lectura}°C")
    suma += lectura
    contador += 1

promedio_temp = suma / contador if contador > 0 else 0
print(f"Temperatura promedio: {promedio_temp:.2f}°C")
