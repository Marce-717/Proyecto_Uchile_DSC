# 🌾 Data Science en Sistemas Naturales
## Universidad de Chile - Escuela de Postgrado

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-green?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-blue?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-red?logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-purple)

**Magister en Ciencias Agrarias - Primavera 2025**

</div>

---

## 📋 Información del Curso

| **Detalle** | **Información** |
|-------------|-----------------|
| **Profesor** | Marcelo Toro Miranda - Ing. Agrónomo, MSc. Data Science |
| **Co-instructor** | Rodrigo Callejas - Ing. Agr. Dr. en Fruticultura |
| **Nivel** | Postgrado - Magister en Ciencias Agrarias |
| **Semestre** | Primavera 2025 |
| **Modalidad** | Presencial con componente práctico |
| **Prerrequisitos** | Conocimientos básicos de estadística |

---

## 🎯 Objetivos de Aprendizaje

Al completar este curso, los estudiantes serán capaces de:

1. **Programación Aplicada**: Aplicar técnicas de programación en Python para resolver problemas complejos en sistemas naturales
2. **Análisis Avanzado**: Implementar técnicas de análisis de datos para modelar y simular escenarios en sistemas agrícolas
3. **Gestión de Big Data**: Manejar grandes volúmenes de información para proyectos colaborativos en agricultura de precisión

---

## 📚 Contenido del Repositorio

### 🗂️ Estructura de Archivos

```
📦 Data Science Recursos Naturales
├── 📄 README.md                                    # Este archivo
├── 📋 Programa_dataScience__V6.pdf                 # Programa oficial del curso
├── 🐍 **Scripts Python**
│   ├── 02_Estructuras_datos.py                     # Listas, tuplas, sets, diccionarios
│   ├── 04_b_condicionales.py                       # Estructuras condicionales
│   └── 05_ciclos.py                                 # Bucles while y for
├── 📊 **Datos de Ejemplo**
│   ├── winequalityred.csv                          # Dataset vinos (ejercicio básico)
│   └── datos_agricolas_5000.csv                    # Dataset agricultura (proyecto final)
├── 📚 **Material Didáctico**
│   ├── Métodos_y_Fórmulas_Principales_-_Resumen_por_Temática.md
│   └── Guia_Matplotlib_Seaborn_SistemasNaturales.md
└── 📝 **Evaluaciones**
    ├── Catedra_1_DataScienceRecursosNarurales_Drive.docx
    └── Catedra_2_DataScienceRecursosNaturales_v02.docx
```

---

## 🚀 Instalación y Configuración

### Prerrequisitos de Sistema

```bash
# Python 3.8 o superior
python --version

# Gestor de paquetes pip
pip --version
```

### Instalación de Librerías

```bash
# Librerías principales
pip install pandas numpy matplotlib seaborn --break-system-packages

# Librerías adicionales (opcional)
pip install jupyter notebook scipy scikit-learn --break-system-packages
```

### Configuración del Entorno

```python
# Configuración estándar para el curso
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de gráficos
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Configuración de pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
```

---

## 📖 Unidades Temáticas

### **Unidad 1: Introducción a la Ciencia de Datos**
- Ética y gestión de datos
- Tipos de sistemas y actividades de procesamiento
- Datos estructurados vs no estructurados
- **Archivo**: `02_Estructuras_datos.py`

### **Unidad 2: Fundamentos y Lógica de Programación**
- Variables, números y cadenas de texto
- Estructuras de datos (listas, tuplas, sets, diccionarios)
- Operadores y estructuras de control
- **Archivos**: `04_b_condicionales.py`, `05_ciclos.py`

### **Unidad 3: Limpieza y Análisis de Datos**
- Módulos Pandas y NumPy
- Creación y manipulación de DataFrames
- Análisis exploratorio de variables
- **Dataset**: `datos_agricolas_5000.csv`

### **Unidad 4: Visualización de Datos**
- Módulos Matplotlib y Seaborn
- Histogramas, boxplots, scatterplots
- **Guía**: `Guia_Matplotlib_Seaborn_SistemasNaturales.md`

---

## 🎮 Empezar Rápido

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Marce-717/Proyecto_Uchile_DSC.git
cd Proyecto_Uchile_DSC
```

### 2. Ejecutar tu Primer Script

```python
# Ejecutar análisis de estructuras de datos
python 02_Estructuras_datos.py

# Ver datasets disponibles
import pandas as pd
df_agricola = pd.read_csv('datos_agricolas_5000.csv')
print(df_agricola.head())
```

### 3. Explorar Datos Agrícolas

```python
# Análisis básico del dataset agrícola
df = pd.read_csv('datos_agricolas_5000.csv')

# Información general
print("Información del dataset:")
print(df.info())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Análisis por región
print("\nRendimiento promedio por región:")
print(df.groupby('Region')['Rendimiento_ton_ha'].mean())
```

---

## 📊 Datasets Incluidos

### 🌾 Dataset Agrícola Principal (`datos_agricolas_5000.csv`)
- **Registros**: 5,000 parcelas
- **Variables**: 11 columnas
- **Contenido**: Datos reales de agricultura chilena
  - Parcela_ID, Región, Cultivo
  - Superficie (ha), Rendimiento (ton/ha)
  - pH del suelo, Precipitación (mm)
  - Sistema de riego, Producción total

### 🍷 Dataset Complementario (`winequalityred.csv`)
- **Registros**: 1,599 muestras
- **Variables**: Calidad de vinos
- **Uso**: Ejercicios básicos de análisis

---

## 🛠️ Principales Métodos y Fórmulas

### **Estructuras de Datos**
```python
# Listas
lista = [1, 2, 3]
lista.append(4)          # Agregar elemento
lista.pop()              # Eliminar último

# Diccionarios
datos = {'cultivo': 'trigo', 'rendimiento': 7.5}
datos.keys()             # Obtener claves
datos.values()           # Obtener valores
```

### **Pandas Esenciales**
```python
# Crear DataFrame
df = pd.DataFrame(datos)

# Análisis exploratorio
df.head()                # Primeras 5 filas
df.info()                # Información general
df.describe()            # Estadísticas descriptivas
df.groupby('region').mean()  # Agrupación y promedio
```

### **Visualización**
```python
# Gráfico básico
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Título del Gráfico')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()

# Seaborn avanzado
sns.boxplot(data=df, x='region', y='rendimiento')
sns.pairplot(df, hue='cultivo')
```

---

## 📝 Sistema de Evaluación

| **Instrumento** | **Ponderación** | **Descripción** |
|-----------------|-----------------|-----------------|
| 1ª Entrega | 30% | Análisis exploratorio básico |
| 2ª Entrega | 30% | Limpieza y transformación de datos |
| Controles | 10% | Evaluaciones periódicas |
| Trabajo Final | 30% | Proyecto aplicado a sistemas naturales |

### Criterios de Evaluación
- ✅ Código reproducible y bien documentado
- ✅ Interpretación agronómica correcta
- ✅ Visualizaciones con contexto profesional
- ✅ Análisis estadístico apropiado
- ✅ Repositorio GitHub organizado

---

## 🔧 Aplicaciones Prácticas

### **Agricultura de Precisión**
- Análisis de mapas de rendimiento
- Optimización de fertilización
- Monitoreo de índices de vegetación (NDVI)

### **Sistemas Silvoagropecuarios**
- Modelado de crecimiento forestal
- Análisis de biodiversidad
- Gestión de recursos hídricos

### **Análisis de Datos Climáticos**
- Procesamiento de series temporales
- Modelos predictivos meteorológicos
- Análisis de variabilidad climática

---

## 🤔 FAQ - Preguntas Frecuentes

<details>
<summary><b>¿Necesito experiencia previa en programación?</b></summary>
<br>
No es indispensable. El curso está diseñado para estudiantes con background agronómico. Comenzamos desde conceptos básicos de programación.
</details>

<details>
<summary><b>¿Qué software necesito instalar?</b></summary>
<br>
- Python 3.8+ (recomendamos Anaconda)
- Editor de código (VS Code, PyCharm, o Jupyter)
- Git para control de versiones
</details>

<details>
<summary><b>¿Los datos son reales o simulados?</b></summary>
<br>
Utilizamos tanto datos reales de la agricultura chilena como datasets simulados con características realistas para ejercicios específicos.
</details>

<details>
<summary><b>¿Cómo accedo al material complementario?</b></summary>
<br>
Todo el material está disponible en este repositorio. Material adicional se comparte via U-Campus de la Universidad de Chile.
</details>

---

## 🤝 Contribuciones y Colaboración

### Para Estudiantes
- Fork el repositorio para tus proyectos personales
- Crea branches para diferentes ejercicios
- Documenta tu código apropiadamente
- Comparte insights agronómicos en discusiones

### Para Colaboradores
- Reporta bugs o mejoras via Issues
- Propón nuevos datasets agrícolas
- Sugiere ejercicios aplicados
- Comparte recursos adicionales

---

## 📞 Soporte y Contacto

### **Profesor Responsable**
- **Marcelo Toro Miranda**
- Ingeniero Agrónomo, MSc. Data Science
- Universidad de Chile - Escuela de Postgrado
- 📧 Email: [contacto disponible via U-Campus]

### **Horarios de Consulta**
- Miércoles: 11:00 - 13:00 hrs
- Previa coordinación para consultas adicionales

### **Recursos Adicionales**
- [Documentación Python](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

---

## 📚 Bibliografía Recomendada

### **Textos Principales**
- **Deitel & Deitel (2021)** - "Intro to Python for Computer Science and Data Science"
- **Grus, J. (2019)** - "Data Science from Scratch: First Principles with Python"
- **Bruce & Bruce (2017)** - "Practical Statistics for Data Scientists"

### **Recursos Complementarios**
- **Hidalgo, C. (2015)** - "Why Information Grows: The Evolution of Order"
- **McKinney, W.** - "Python for Data Analysis" (Pandas creator)

---

## 🏆 Reconocimientos

Este material ha sido desarrollado considerando:
- Estándares internacionales de Data Science
- Necesidades específicas del sector silvoagropecuario chileno
- Retroalimentación continua de estudiantes
- Mejores prácticas en educación técnica superior

---

## 📄 Licencia y Uso

Este material educativo está disponible bajo los términos de uso académico de la Universidad de Chile. El código y datasets pueden ser utilizados con fines educativos citando apropiadamente la fuente.

**Cita sugerida:**
```
Toro Miranda, M. (2025). Data Science en Sistemas Naturales. 
Universidad de Chile, Escuela de Postgrado. 
GitHub: https://github.com/Marce-717/Proyecto_Uchile_DSC
```

---

<div align="center">

### 🌾 ¡Bienvenidos al Mundo de Data Science Agrícola! 🌾

**"Transformando datos en decisiones para una agricultura más sostenible"**

---

[![GitHub stars](https://img.shields.io/github/stars/Marce-717/Proyecto_Uchile_DSC?style=social)](https://github.com/Marce-717/Proyecto_Uchile_DSC)
[![GitHub forks](https://img.shields.io/github/forks/Marce-717/Proyecto_Uchile_DSC?style=social)](https://github.com/Marce-717/Proyecto_Uchile_DSC/fork)

*Última actualización: Enero 2025*

</div>
