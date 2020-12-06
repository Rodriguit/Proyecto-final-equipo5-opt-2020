
## Proyecto Final del curso Optimización: Equipo 5

Este es el repositorio de Proyecto Final para la materia de Optimización del semestre 2020-2 en la Maestría en Ciencia de Datos, ITAM

**Integrantes:**

* José Reyes Garza - 142207

* Miguel López Cruz - 197967

* José Luis Zárate Cortés - 183347

* Rodrigo Suárez Segovia - 191351

### Título del proyecto:

**PCA: Aplicación en Compresión de Imágenes**

### Objetivo del proyecto: 

Uso de PCA para la compresión y reconstrucción de imágenes de rostros de personas empleando el lenguaje de programación Python. El alcance del proyecto se orienta al estudio de la reducción de dimensionalidad a través de PCA, entendimiento de los algoritmos y aplicación en reconstrucción de imágenes.

### Indice del proyecto

1. [Introducción]()
2. [Arquitectura requerida]()

### Introducción

El análisis de componentes principales (PCA) es una técnica para reducir la dimensionalidad de los conjuntos de datos, aprovechando el hecho de que las imágenes de estos conjuntos de datos tienen algo en común. Por ejemplo, en un conjunto de datos que consta de fotografías faciales, cada fotografía tendrá rasgos faciales como ojos, nariz, boca. En lugar de codificar esta información píxel a píxel, podríamos hacer una plantilla de cada tipo de estas características y luego simplemente combinar estas plantillas para generar cualquier rostro en el conjunto de datos. En este enfoque, cada plantilla seguirá teniendo una dimensión de 64x64 = 4096, pero como reutilizaremos estas plantillas (funciones básicas) para generar cada cara en el conjunto de datos, la cantidad de plantillas necesarias será pequeña. 

## Arquitectura requerida 


