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

### Arquitectura requerida 

Con el propósito de reproducibilidad del proyecto y todos los integrantes tuvieran un entorno común de trabajo, se empleó la imagen de docker basada en Python del curso optimización 2020 (palmoreck/jupyterlab_optimizacion:2.1.4) así como una instancia de AWS. A continuación, se describen los pasos utilizados para la creación de la instancia en AWS para poder trabajar de manera más rápida y eficiente.

**Crear la maquina EC2**

Se utilizó una cuenta de AWS para elegir de máquinas EC2.

Paso 1: Se lanzó una instancia de AWS de tipo EC2, la Amazon Machine Image (AMI) que se eligió fue una del tipo ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-20200408

![Ejemplo_AMI\textwidth](https://github.com/Rodriguit/Proyecto-final-equipo5-opt-2020/blob/task3_computo_nube/images/AMI.png)


