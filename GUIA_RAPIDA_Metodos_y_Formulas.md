# 🌾 GUÍA RÁPIDA: Métodos y Fórmulas Principales
## Data Science en Sistemas Silvoagropecuarios

**Para:** Magister en Ciencias Agrarias - Universidad de Chile  
**Profesor:** Marcelo Toro Miranda  
**Última actualización:** Enero 2025

---

## 📖 ÍNDICE TEMÁTICO

1. [**Estructuras de Datos Básicas**](#1-estructuras-de-datos-básicas)
2. [**Funciones y Control de Flujo**](#2-funciones-y-control-de-flujo)
3. [**NumPy para Análisis Numérico**](#3-numpy-para-análisis-numérico)
4. [**Pandas para Manejo de Datos**](#4-pandas-para-manejo-de-datos)
5. [**Visualización con Matplotlib/Seaborn**](#5-visualización-con-matplotlibseaborn)
6. [**Fórmulas Agronómicas Esenciales**](#6-fórmulas-agronómicas-esenciales)
7. [**Estadística Aplicada**](#7-estadística-aplicada)
8. [**Patrones de Trabajo Comunes**](#8-patrones-de-trabajo-comunes)

---

## 1. Estructuras de Datos Básicas

### 📋 **Listas** (Mutables, Ordenadas)
```python
# Creación y métodos esenciales
cultivos = ['trigo', 'maíz', 'avena']
cultivos.append('cebada')           # ➕ Agregar al final
cultivos.insert(1, 'arroz')         # ➕ Insertar en posición
cultivos.remove('maíz')             # ❌ Eliminar elemento
ultimo = cultivos.pop()             # ❌ Eliminar y obtener último
cultivos.sort()                     # 🔄 Ordenar alfabéticamente
len(cultivos)                       # 📏 Longitud
cultivos[0:2]                       # ✂️ Slicing (primeros 2)
```

### 🔒 **Tuplas** (Inmutables, Ordenadas)
```python
# Datos que no cambian
coordenadas = (33.45, -70.67)       # Lat, Lon Santiago
coordenadas[0]                      # Acceso por índice
coordenadas.count(33.45)            # Contar ocurrencias
coordenadas.index(-70.67)           # Obtener índice
```

### 🎯 **Sets** (Sin duplicados, Sin orden)
```python
# Eliminar duplicados
tipos_suelo = {'arcilloso', 'franco', 'arenoso', 'arcilloso'}
# Resultado: {'arcilloso', 'franco', 'arenoso'}
tipos_suelo.add('limoso')           # ➕ Agregar elemento
tipos_suelo.remove('arenoso')       # ❌ Eliminar elemento
'franco' in tipos_suelo             # ✅ Verificar existencia
```

### 🗂️ **Diccionarios** (Clave-Valor)
```python
# Datos agronómicos estructurados
parcela = {
    'cultivo': 'trigo',
    'superficie': 25.5,
    'rendimiento': 7.2,
    'ph_suelo': 6.8
}
parcela['cultivo']                  # Acceso por clave
parcela['riego'] = 'tecnificado'    # ➕ Agregar nueva clave
parcela.keys()                      # 🔑 Todas las claves
parcela.values()                    # 📊 Todos los valores
parcela.items()                     # 🔄 Pares clave-valor
```

---

## 2. Funciones y Control de Flujo

### 🔧 **Definición de Funciones**
```python
# Función básica para cálculos agrícolas
def calcular_ndvi(nir, red):
    """Calcula el Índice de Vegetación Normalizado"""
    return (nir - red) / (nir + red)

# Función con parámetros por defecto
def clasificar_rendimiento(rendimiento, umbral_bajo=6, umbral_alto=9):
    if rendimiento < umbral_bajo:
        return "Bajo"
    elif rendimiento <= umbral_alto:
        return "Medio"
    else:
        return "Alto"

# Función con múltiples argumentos
def calcular_promedio(*valores):
    return sum(valores) / len(valores)
```

### 🔀 **Estructuras Condicionales**
```python
# Clasificación de pH del suelo
def clasificar_ph(ph):
    if ph < 6.0:
        return "Ácido"
    elif 6.0 <= ph <= 7.5:
        return "Neutro"
    else:
        return "Alcalino"

# Múltiples condiciones
def evaluar_cultivo(temp, humedad, ph):
    if temp >= 18 and humedad > 60 and 6.0 <= ph <= 7.0:
        return "Condiciones óptimas"
    else:
        return "Requiere manejo"
```

### 🔄 **Ciclos (Loops)**
```python
# Procesar lista de rendimientos
rendimientos = [7.2, 6.8, 8.1, 5.9, 7.5]

# FOR: Iterar sobre elementos
for rendimiento in rendimientos:
    categoria = clasificar_rendimiento(rendimiento)
    print(f"Rendimiento: {rendimiento} -> {categoria}")

# WHILE: Condición
contador = 0
while contador < len(rendimientos):
    print(f"Parcela {contador+1}: {rendimientos[contador]}")
    contador += 1

# List comprehension (avanzado)
altos = [r for r in rendimientos if r > 7.0]
```

---

## 3. NumPy para Análisis Numérico

### 📊 **Creación de Arrays**
```python
import numpy as np

# Arrays básicos
temperaturas = np.array([18, 22, 25, 20, 19])
precipitaciones = np.zeros(30)      # 30 días sin lluvia
rendimientos = np.ones(100) * 7.5   # 100 parcelas, 7.5 ton/ha

# Rangos y secuencias
dias = np.arange(1, 366)            # Días del año
muestreo = np.linspace(0, 100, 21)  # 21 puntos entre 0-100m
```

### 🎲 **Números Aleatorios (Simulaciones)**
```python
np.random.seed(42)                  # Reproducibilidad
# Simulación de datos climáticos
temp_diaria = np.random.normal(20, 5, 365)     # μ=20°C, σ=5°C
lluvia_anual = np.random.exponential(2, 365)   # Distribución exponencial
ndvi_random = np.random.uniform(0.3, 0.9, 50)  # NDVI entre 0.3-0.9
```

### 🧮 **Operaciones Estadísticas**
```python
datos = np.array([7.2, 6.8, 8.1, 5.9, 7.5, 6.2, 8.9, 7.1])

# Estadísticas descriptivas
media = datos.mean()                # 📊 Media
mediana = np.median(datos)          # 📊 Mediana  
desv_est = datos.std()              # 📊 Desviación estándar
minimo = datos.min()                # 📊 Valor mínimo
maximo = datos.max()                # 📊 Valor máximo
suma = datos.sum()                  # ➕ Suma total
percentil_75 = np.percentile(datos, 75)  # 📊 Percentil 75
```

---

## 4. Pandas para Manejo de Datos

### 📋 **Creación de DataFrames**
```python
import pandas as pd

# Desde diccionario (más común en agricultura)
datos_agricolas = pd.DataFrame({
    'parcela': ['P001', 'P002', 'P003', 'P004'],
    'cultivo': ['trigo', 'maíz', 'avena', 'trigo'],
    'superficie_ha': [25.5, 18.2, 31.0, 22.8],
    'rendimiento': [7.2, 9.1, 5.8, 6.9],
    'ph_suelo': [6.8, 7.1, 6.3, 6.5]
})

# Desde archivo CSV
df = pd.read_csv('datos_agricolas.csv')
df = pd.read_excel('reporte_anual.xlsx')
```

### 🔍 **Exploración de Datos**
```python
# Información básica
df.head(10)                         # 👁️ Primeras 10 filas
df.tail(5)                          # 👁️ Últimas 5 filas
df.info()                           # ℹ️ Información general
df.describe()                       # 📊 Estadísticas descriptivas
df.shape                            # 📏 (filas, columnas)
df.columns                          # 📋 Nombres de columnas
df.dtypes                           # 🏷️ Tipos de datos
df.isnull().sum()                   # ❌ Contar valores faltantes
```

### 🎯 **Selección y Filtrado**
```python
# Seleccionar columnas
rendimientos = df['rendimiento']                    # Una columna
datos_key = df[['cultivo', 'rendimiento']]         # Múltiples columnas

# Filtrado condicional
trigo = df[df['cultivo'] == 'trigo']               # Solo trigo
alto_rend = df[df['rendimiento'] > 7.0]            # Alto rendimiento
rango_ph = df[(df['ph_suelo'] >= 6.5) & (df['ph_suelo'] <= 7.5)]  # pH neutro

# Usando query (más legible)
buenos_suelos = df.query('ph_suelo >= 6.5 and rendimiento > 6.0')
```

### 📊 **Agrupación y Análisis**
```python
# Agrupar por cultivo
por_cultivo = df.groupby('cultivo')
promedios = por_cultivo['rendimiento'].mean()      # 📊 Promedio por cultivo
estadisticas = por_cultivo.describe()              # 📊 Estadísticas completas

# Múltiples agregaciones
resumen = df.groupby('cultivo').agg({
    'rendimiento': ['mean', 'std', 'count'],
    'superficie_ha': 'sum',
    'ph_suelo': 'median'
})

# Tabla pivote (resumen tipo Excel)
pivot = df.pivot_table(values='rendimiento', 
                       index='cultivo', 
                       columns='region', 
                       aggfunc='mean')
```

### ✏️ **Transformación de Datos**
```python
# Crear nuevas columnas
df['produccion_total'] = df['rendimiento'] * df['superficie_ha']
df['categoria_rend'] = df['rendimiento'].apply(clasificar_rendimiento)

# Categorización automática
df['rango_ph'] = pd.cut(df['ph_suelo'], 
                        bins=[0, 6.0, 7.5, 14], 
                        labels=['Ácido', 'Neutro', 'Alcalino'])

# Reemplazar valores
df['cultivo'] = df['cultivo'].replace({'maiz': 'maíz'})  # Corregir acentos
```

---

## 5. Visualización con Matplotlib/Seaborn

### 📈 **Gráficos Básicos con Matplotlib**
```python
import matplotlib.pyplot as plt

# Configuración inicial
plt.figure(figsize=(10, 6))
plt.style.use('seaborn-v0_8')

# Gráfico de líneas (series temporales)
plt.plot(dias, temperaturas, label='Temperatura', linewidth=2)
plt.xlabel('Días del año')
plt.ylabel('Temperatura (°C)')
plt.title('Evolución de Temperatura Anual')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Gráfico de barras (comparaciones)
cultivos = ['Trigo', 'Maíz', 'Avena']
rendimientos = [7.2, 9.1, 5.8]
plt.bar(cultivos, rendimientos, color=['gold', 'orange', 'wheat'])
plt.ylabel('Rendimiento (ton/ha)')
plt.title('Rendimiento por Cultivo')
```

### 📊 **Visualizaciones Avanzadas con Seaborn**
```python
import seaborn as sns

# Configuración
sns.set_style("whitegrid")
sns.set_palette("husl")

# Distribuciones
sns.histplot(df['rendimiento'], kde=True)           # Histograma + densidad
sns.boxplot(x='cultivo', y='rendimiento', data=df)  # Box plots comparativos
sns.violinplot(x='region', y='ph_suelo', data=df)  # Distribuciones detalladas

# Correlaciones
sns.scatterplot(x='ph_suelo', y='rendimiento', 
                hue='cultivo', data=df)             # Scatter con categorías
sns.regplot(x='ndvi', y='rendimiento', data=df)    # Regresión lineal

# Análisis multivariado
sns.pairplot(df, hue='cultivo')                     # Matriz de correlaciones
sns.heatmap(df.corr(), annot=True, cmap='coolwarm') # Mapa de calor correlaciones
```

### 📊 **Subplots (Múltiples gráficos)**
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Subplot 1: Histograma
axes[0, 0].hist(df['rendimiento'], bins=15, alpha=0.7)
axes[0, 0].set_title('Distribución de Rendimientos')

# Subplot 2: Boxplot
df.boxplot(column='ph_suelo', by='cultivo', ax=axes[0, 1])
axes[0, 1].set_title('pH por Cultivo')

# Subplot 3: Scatter
axes[1, 0].scatter(df['ndvi'], df['rendimiento'])
axes[1, 0].set_xlabel('NDVI')
axes[1, 0].set_ylabel('Rendimiento')

# Subplot 4: Línea temporal
axes[1, 1].plot(range(len(df)), df['rendimiento'].cumsum())
axes[1, 1].set_title('Rendimiento Acumulado')

plt.tight_layout()
plt.show()
```

---

## 6. Fórmulas Agronómicas Esenciales

### 🌱 **Índices de Vegetación**
```python
def calcular_ndvi(nir, red):
    """NDVI: Normalized Difference Vegetation Index"""
    return (nir - red) / (nir + red)
    # Rango: -1 a +1
    # > 0.7: Vegetación densa y saludable
    # 0.5-0.7: Vegetación moderada  
    # 0.2-0.5: Vegetación escasa
    # < 0.2: Sin vegetación

def calcular_savi(nir, red, L=0.5):
    """SAVI: Soil Adjusted Vegetation Index"""
    return ((nir - red) / (nir + red + L)) * (1 + L)

def calcular_evi(nir, red, blue, G=2.5, C1=6, C2=7.5, L=1):
    """EVI: Enhanced Vegetation Index"""
    return G * ((nir - red) / (nir + C1*red - C2*blue + L))
```

### 🌡️ **Unidades de Calor y Crecimiento**
```python
def grados_dia_crecimiento(temp_max, temp_min, temp_base=10):
    """GDD: Growing Degree Days"""
    temp_promedio = (temp_max + temp_min) / 2
    gdd = max(0, temp_promedio - temp_base)
    return gdd

# Acumular GDD durante la temporada
def gdd_acumulado(temperaturas_max, temperaturas_min, temp_base=10):
    gdd_total = 0
    for tmax, tmin in zip(temperaturas_max, temperaturas_min):
        gdd_total += grados_dia_crecimiento(tmax, tmin, temp_base)
    return gdd_total
```

### 💧 **Eficiencias y Balances**
```python
def eficiencia_uso_agua(rendimiento, agua_aplicada):
    """Productividad del agua (kg/m³)"""
    return rendimiento * 1000 / agua_aplicada  # kg/m³

def eficiencia_uso_nitrogeno(rendimiento, n_aplicado):
    """Eficiencia uso de nitrógeno (kg grano/kg N)"""
    return rendimiento * 1000 / n_aplicado  # kg/kg

def indice_cosecha(peso_grano, biomasa_total):
    """Proporción de biomasa destinada a grano"""
    return peso_grano / biomasa_total

def balance_hidrico_simple(precipitacion, riego, evapotranspiracion):
    """Balance hídrico básico"""
    return precipitacion + riego - evapotranspiracion
```

### 🧪 **Fertilización y Suelos**
```python
def dosis_fertilizante(requerimiento, contenido_suelo, eficiencia=0.6):
    """Cálculo de dosis de fertilizante"""
    return (requerimiento - contenido_suelo) / eficiencia

def capacidad_intercambio_cationico(ca, mg, k, na, h):
    """CIC total del suelo (meq/100g)"""
    return ca + mg + k + na + h

def saturacion_bases(ca, mg, k, na, cic_total):
    """Porcentaje de saturación de bases"""
    return ((ca + mg + k + na) / cic_total) * 100
```

---

## 7. Estadística Aplicada

### 📊 **Estadísticas Descriptivas**
```python
import scipy.stats as stats

# Medidas de tendencia central
def estadisticas_basicas(datos):
    return {
        'media': np.mean(datos),
        'mediana': np.median(datos),
        'moda': stats.mode(datos)[0][0],
        'desviacion_std': np.std(datos, ddof=1),  # Muestra
        'coef_variacion': (np.std(datos, ddof=1) / np.mean(datos)) * 100,
        'percentil_25': np.percentile(datos, 25),
        'percentil_75': np.percentile(datos, 75),
        'rango_intercuartil': np.percentile(datos, 75) - np.percentile(datos, 25)
    }

# Detección de outliers
def detectar_outliers_iqr(datos):
    Q1 = np.percentile(datos, 25)
    Q3 = np.percentile(datos, 75)
    IQR = Q3 - Q1
    limite_inf = Q1 - 1.5 * IQR
    limite_sup = Q3 + 1.5 * IQR
    outliers = [x for x in datos if x < limite_inf or x > limite_sup]
    return outliers, limite_inf, limite_sup
```

### 🔗 **Correlaciones y Asociaciones**
```python
# Correlación de Pearson
def correlacion_pearson(x, y):
    return np.corrcoef(x, y)[0, 1]

# Correlación más robusta (Spearman)
def correlacion_spearman(x, y):
    return stats.spearmanr(x, y)[0]

# Matriz completa de correlaciones
def matriz_correlacion(df, metodo='pearson'):
    return df.corr(method=metodo)
```

### 📈 **Regresión Simple**
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def regresion_simple(x, y):
    """Regresión lineal simple y=mx+b"""
    x = np.array(x).reshape(-1, 1)
    y = np.array(y)
    
    modelo = LinearRegression()
    modelo.fit(x, y)
    
    y_pred = modelo.predict(x)
    r2 = r2_score(y, y_pred)
    
    return {
        'pendiente': modelo.coef_[0],
        'intercepto': modelo.intercept_,
        'r_cuadrado': r2,
        'ecuacion': f'y = {modelo.coef_[0]:.3f}x + {modelo.intercept_:.3f}'
    }
```

---

## 8. Patrones de Trabajo Comunes

### 🔄 **Flujo de Trabajo Estándar**
```python
# 1. IMPORTAR Y CONFIGURAR
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. CARGAR DATOS
df = pd.read_csv('datos_agricolas.csv')

# 3. EXPLORACIÓN INICIAL
print(f"Dimensiones: {df.shape}")
print(f"Columnas: {list(df.columns)}")
print(f"Valores faltantes:\n{df.isnull().sum()}")
print(f"Estadísticas:\n{df.describe()}")

# 4. LIMPIEZA DE DATOS
df = df.dropna()                    # Eliminar filas con valores faltantes
df = df[df['rendimiento'] > 0]      # Filtrar valores imposibles
df['cultivo'] = df['cultivo'].str.lower()  # Normalizar texto

# 5. ANÁLISIS EXPLORATORIO
# Distribuciones por grupo
df.groupby('cultivo')['rendimiento'].describe()
# Correlaciones
df.corr()['rendimiento'].sort_values(ascending=False)

# 6. VISUALIZACIÓN
plt.figure(figsize=(12, 8))
sns.boxplot(x='cultivo', y='rendimiento', data=df)
plt.xticks(rotation=45)
plt.title('Distribución de Rendimientos por Cultivo')
plt.tight_layout()
plt.show()

# 7. ANÁLISIS ESPECÍFICO
cultivo_interes = df[df['cultivo'] == 'trigo']
promedio = cultivo_interes['rendimiento'].mean()
print(f"Rendimiento promedio de trigo: {promedio:.2f} ton/ha")

# 8. EXPORTAR RESULTADOS
resumen = df.groupby('cultivo').agg({
    'rendimiento': ['count', 'mean', 'std'],
    'superficie_ha': 'sum'
}).round(2)
resumen.to_csv('resumen_por_cultivo.csv')
```

### 🎯 **Análisis por Categorías**
```python
def analizar_por_categoria(df, columna_categoria, columna_valor):
    """Análisis completo por categorías"""
    resultados = {}
    
    for categoria in df[columna_categoria].unique():
        datos = df[df[columna_categoria] == categoria][columna_valor]
        
        resultados[categoria] = {
            'n': len(datos),
            'media': datos.mean(),
            'mediana': datos.median(),
            'desv_std': datos.std(),
            'minimo': datos.min(),
            'maximo': datos.max(),
            'cv_pct': (datos.std() / datos.mean()) * 100
        }
    
    return pd.DataFrame(resultados).T

# Uso práctico
resumen_cultivos = analizar_por_categoria(df, 'cultivo', 'rendimiento')
print(resumen_cultivos.round(2))
```

### 📊 **Funciones de Visualización Rápida**
```python
def plot_distribucion(df, columna, por_categoria=None):
    """Gráfico rápido de distribución"""
    plt.figure(figsize=(10, 6))
    
    if por_categoria:
        for categoria in df[por_categoria].unique():
            datos = df[df[por_categoria] == categoria][columna]
            plt.hist(datos, alpha=0.7, label=categoria, bins=15)
        plt.legend()
    else:
        plt.hist(df[columna], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    
    plt.xlabel(columna)
    plt.ylabel('Frecuencia')
    plt.title(f'Distribución de {columna}')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_correlacion(df, x, y, categoria=None):
    """Gráfico de correlación rápido"""
    plt.figure(figsize=(8, 6))
    
    if categoria:
        sns.scatterplot(data=df, x=x, y=y, hue=categoria, s=60)
    else:
        plt.scatter(df[x], df[y], alpha=0.6, s=50)
        # Línea de tendencia
        z = np.polyfit(df[x], df[y], 1)
        p = np.poly1d(z)
        plt.plot(df[x].sort_values(), p(df[x].sort_values()), "r--", alpha=0.8)
    
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{y} vs {x}')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
```

---

## 🚀 **Tips para Eficiencia**

### ⚡ **Optimización de Código**
```python
# ✅ HACER: Usar vectorización de pandas/numpy
df['ndvi_class'] = np.where(df['ndvi'] > 0.7, 'Alto', 
                   np.where(df['ndvi'] > 0.5, 'Medio', 'Bajo'))

# ❌ EVITAR: Loops innecesarios
# for i in range(len(df)):
#     if df.loc[i, 'ndvi'] > 0.7:
#         df.loc[i, 'ndvi_class'] = 'Alto'  # MUY LENTO

# ✅ HACER: Usar .apply() para funciones complejas
df['categoria'] = df['rendimiento'].apply(clasificar_rendimiento)

# ✅ HACER: Filtrado eficiente
alto_ndvi = df.query('ndvi > 0.7 and rendimiento > 8')

# ✅ HACER: Múltiples agregaciones en una operación
estadisticas = df.groupby('cultivo').agg({
    'rendimiento': ['mean', 'std', 'count'],
    'superficie_ha': 'sum',
    'ndvi': ['mean', 'median']
})
```

### 🎯 **Buenas Prácticas**
1. **Nombres descriptivos**: `rendimiento_trigo` no `datos1`
2. **Comentarios**: Explicar el "por qué", no el "qué"
3. **Funciones pequeñas**: Una función, una responsabilidad
4. **Validación de datos**: Verificar rangos y tipos esperados
5. **Reproducibilidad**: `np.random.seed(42)` para resultados consistentes
6. **Backup**: Guardar estados intermedios con `.to_csv()` o `.to_pickle()`

---

## 🔍 **Comandos de Depuración**

```python
# Información rápida de DataFrame
def info_rapida(df):
    print(f"📊 Dimensiones: {df.shape}")
    print(f"🔍 Tipos de datos:\n{df.dtypes.value_counts()}")
    print(f"❌ Valores faltantes: {df.isnull().sum().sum()}")
    print(f"🔄 Duplicados: {df.duplicated().sum()}")
    print(f"💾 Memoria: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# Verificar valores únicos
def valores_unicos(df, columna):
    valores = df[columna].unique()
    print(f"📋 {columna}: {len(valores)} valores únicos")
    print(valores[:10])  # Mostrar primeros 10
    if len(valores) > 10:
        print("...")

# Comparar distribuciones
def comparar_grupos(df, grupo, variable):
    return df.groupby(grupo)[variable].describe().round(2)
```

---

**📌 RECORDATORIO FINAL**

- **Siempre explorar** antes de analizar
- **Validar resultados** con conocimiento agronómico  
- **Documentar supuestos** y limitaciones
- **Visualizar patrones** antes de modelar
- **Interpretar en contexto** agrícola real

---

**🎓 ¡Éxito en tu análisis de datos agrícolas!**

*Esta guía es tu compañero de referencia rápida. Manténla cerca durante tus análisis.*
