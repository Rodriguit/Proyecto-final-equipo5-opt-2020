## Proyecto Final del curso Optimización: Equipo 5

Este es el repositorio del Proyecto Final curso Optimización   
Semestre 2020-2  
Maestría en Ciencia de Datos, ITAM  
______

**Ligas de trabajo:**  

* [forked repo erick](https://github.com/Rodriguit/analisis-numerico-computo-cientifico/tree/optimizacion-2020-2/proyecto_final/proyectos/equipos/equipo_hessiano)
* [develop branch](https://github.com/Rodriguit/Proyecto-final-equipo5-opt-2020/tree/develop)
* [construcción reporte](https://www.overleaf.com/project/5fc535eb8fa71982ee3a3c48)
____
**Equipo:**  

| Github_User  | Alumno    | Scrum Rol                      |
|:------------:|:---------:|:------------------------------:|
| @lobolc      | Miguel    | Solución y Programación        |
| @jreyesgar93 | José      | Solución y Programación        |
| @Rodriguit   | Rodrigo   | Programación y Revisión        |
| @ZarCorvus   | José Luis | Project Manager                |


#### Título del proyecto:  

**Método de Máxima Verosimilitud como problema de Optimización**

#### Objetivo del proyecto:   

Resolver un problema de Optimización al maximizar los parámetros de una distribución por Máxima Verosimilitud con Métodos de Descenso.


| Github_User  | Alumno    | Scrum Rol                      |
|:------------:|:---------:|:------------------------------:|
| @lobolc      | Miguel    | Solución y Programación        |
| @jreyesgar93 | José      | Solución y Programación        |
| @Rodriguit   | Rodrigo   | Programación y Revisión        |
| @ZarCorvus   | José Luis | Project Manager                |

### Título del proyecto:


**Método de Máxima Verosimilitud como problema de Optimización**

### Objetivo del proyecto: 

En el contexto de la inferencia estadística, uno de los principales problemas que se enfrentan es determinar el valor de un parámetro (o los valores de varios parámetros) de un conjunto posible de alternativas. En este sentido, existen diversas metodologías que nos permiten calcular estimadores distintos de un mismo parámetro de una población, tales como el método de momentos y el método de máxima verosimilitud. Tales metodologías, esencialmente realizan un proceso de Optimización, por lo que naturalmete podemos adecuar este proceso para analizarlo a través de los métodos de Descenso en Gradiente y Newton-Raphson.  

### Indice del proyecto

1. [Introducción](https://github.com/Rodriguit/Proyecto-final-equipo5-opt-2020/tree/task3_computo_nube#introducci%C3%B3n)
2. [Arquitectura requerida](https://github.com/Rodriguit/Proyecto-final-equipo5-opt-2020/tree/task3_computo_nube#introducci%C3%B3n)

### Introducción
.
. 

### Arquitectura requerida 

Con el propósito de reproducibilidad del proyecto y todos los integrantes tuvieran un entorno común de trabajo, se empleó la imagen de docker basada en Python del curso optimización 2020 (palmoreck/jupyterlab_optimizacion:2.1.4) así como una instancia de AWS. A continuación, se describen los pasos utilizados para la creación de la instancia en AWS para poder trabajar de manera más rápida y eficiente.

**Crear la maquina EC2**

Se utilizó una cuenta de AWS para elegir una Elastic Cloud Compute

**Paso 1:** 

Se lanzó una instancia de AWS de tipo EC2, la Amazon Machine Image (AMI) que se eligió fue una del tipo ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64bits. El tipo de instancia que se eligió fue una t2.micro que cuenta 8 GB de memoria.

![Ejemplo_AMI\textwidth](https://github.com/Rodriguit/Proyecto-final-equipo5-opt-2020/blob/task3_computo_nube/images/AMI.png)

**Paso 2:** 

Se configuró la instancia siguiendo los pasos de la wiki de AWS del curso de optimización. En resumen, se tuvo que configurar una VPC, una subnet pública y un grupo de seguridad. 

![Ejemplo_vpc\textwidth](https://github.com/Rodriguit/Proyecto-final-equipo5-opt-2020/blob/task3_computo_nube/images/vpc.png)
![Ejemplo_sgp\textwidth](https://github.com/Rodriguit/Proyecto-final-equipo5-opt-2020/blob/task3_computo_nube/images/sgp.png)

**Instalación de herramientas de trabajo Docker y Git**
