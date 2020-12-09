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

En el contexto de la inferencia estadística, uno de los principales problemas que se enfrentan es determinar el valor de un parámetro (o los valores de varios parámetros) de un conjunto posible de alternativas. En este sentido, existen diversas metodologías que nos permiten calcular estimadores distintos de un mismo parámetro de una población, tales como el método de momentos y el método de máxima verosimilitud. Tales metodologías, esencialmente realizan un proceso de Optimización, por lo que naturalmete podemos adecuar este proceso para analizarlo a través de los métodos de Descenso en Gradiente y Newton-Raphson. 

#### Estructura del proyecto:   

```bash
    .
    ├── README.md
    ├── codigo
    │   ├── MLE
    │       └── __init__.py               <- Archivo Contiene la integración de las funciones y clases desarrolladas en python.
    │   └── Maxima_verosimilitud.ipynb    <- Archivo Contiene la ejecución del código con la implementación de dos ejemplos.
    │   └── datasets                      <- This is not a real folder, just a category.
    │       ├── fp.dta                  
    │       └── wheat_yield.txt
    ├── infraestructura                   <- En esta carpeta está la infraestructura utilizada en AWS para el cómputo en la nube.
    │   ├── images
    │   └── IPv4-DNS.txt
    ├── referencias                       <- Fuentes consultadas
    ├── reporte
    │   └── ProyectoFinal_Opt_Equipo5.pdf <- Contiene la exposición del problema, los fundamentos técnicos y el reporte con los resultados.
    └── tests
        ├── __init__.py
        ├── conftest.py
        ├── test.py
        ├── test_normal.py
        └── wheat_yield.txt

```
