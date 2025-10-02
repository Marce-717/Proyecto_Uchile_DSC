# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 19:13:50 2025

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
# 5. INTRODUCCIÓN A CLASES (POO)
# =============================================================================

print("\n\n" + "=" * 60)
print("5. INTRODUCCIÓN A CLASES")
print("=" * 60)

# --------------- CLASE BÁSICA ---------------

print("\n>>> CLASE BÁSICA")
print("-" * 40)

class Parcela:
    """Clase para representar una parcela agrícola"""
    
    def __init__(self, codigo, area_ha, cultivo):
        """Constructor - inicializa la parcela"""
        self.codigo = codigo
        self.area_ha = area_ha
        self.cultivo = cultivo
        self.rendimiento = 0
    
    def establecer_rendimiento(self, rendimiento_ton_ha):
        """Establece el rendimiento de la parcela"""
        self.rendimiento = rendimiento_ton_ha
    
    def calcular_produccion_total(self):
        """Calcula la producción total en toneladas"""
        return self.area_ha * self.rendimiento
    
    def mostrar_info(self):
        """Muestra información de la parcela"""
        print(f"\nParcela {self.codigo}:")
        print(f"  Área: {self.area_ha} ha")
        print(f"  Cultivo: {self.cultivo}")
        print(f"  Rendimiento: {self.rendimiento} ton/ha")
        print(f"  Producción total: {self.calcular_produccion_total()} ton")

# Crear instancias de la clase
parcela1 = Parcela("P001", 12.5, "Maíz")
parcela1.establecer_rendimiento(8.2)
parcela1.mostrar_info()

parcela2 = Parcela("P002", 15.0, "Trigo")
parcela2.establecer_rendimiento(5.5)
parcela2.mostrar_info()


# --------------- CLASE CON MÉTODOS AVANZADOS ---------------


print("\n\n>>> CLASE AVANZADA")
print("-" * 40)

class SensorSuelo:
    """Clase para gestionar un sensor de suelo"""
    
    def __init__(self, id_sensor, ubicacion, tipo="humedad"):
        self.id_sensor = id_sensor
        self.ubicacion = ubicacion
        self.tipo = tipo
        self.lecturas = []
        self.alarma_activa = False
    
    def agregar_lectura(self, valor):
        """Agrega una nueva lectura del sensor"""
        self.lecturas.append(valor)
        self._verificar_alarma(valor)
    
    def _verificar_alarma(self, valor):
        """Método privado para verificar si se activa alarma"""
        if self.tipo == "humedad" and valor < 15:
            self.alarma_activa = True
            print(f"  ⚠️ ALARMA: Sensor {self.id_sensor} - Humedad crítica: {valor}%")
        else:
            self.alarma_activa = False
    
    def obtener_promedio(self):
        """Calcula el promedio de las lecturas"""
        if len(self.lecturas) == 0:
            return 0
        return sum(self.lecturas) / len(self.lecturas)
    
    def obtener_ultima_lectura(self):
        """Retorna la última lectura registrada"""
        if len(self.lecturas) == 0:
            return None
        return self.lecturas[-1]
    
    def reporte(self):
        """Genera un reporte del sensor"""
        print(f"\n--- Reporte Sensor {self.id_sensor} ---")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Tipo: {self.tipo}")
        print(f"Lecturas registradas: {len(self.lecturas)}")
        if len(self.lecturas) > 0:
            print(f"Última lectura: {self.obtener_ultima_lectura()}%")
            print(f"Promedio: {self.obtener_promedio():.1f}%")
            print(f"Mínima: {min(self.lecturas)}%")
            print(f"Máxima: {max(self.lecturas)}%")
        print(f"Estado alarma: {'🔴 ACTIVA' if self.alarma_activa else '🟢 Normal'}")

# Crear y usar sensor
sensor1 = SensorSuelo("S001", "Parcela Norte", "humedad")

# Simular lecturas a lo largo del día
print("\nRegistrando lecturas del sensor:")
lecturas_dia = [25, 23, 20, 18, 16, 14, 13, 15, 18]

for i, lectura in enumerate(lecturas_dia, 1):
    print(f"Hora {i}: {lectura}%")
    sensor1.agregar_lectura(lectura)

sensor1.reporte()