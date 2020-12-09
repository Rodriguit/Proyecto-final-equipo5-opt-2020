
### Arquitectura requerida 

Con el propósito de reproducibilidad del proyecto y todos los integrantes tuvieran un entorno común de trabajo, se empleó la imagen de docker basada en Python del curso optimización 2020 (palmoreck/jupyterlab_optimizacion:2.1.4) así como una instancia de AWS. A continuación, se describen los pasos utilizados para la creación de la instancia en AWS para poder trabajar de manera más rápida y eficiente.

**Crear la maquina EC2**

Se utilizó una cuenta de AWS para elegir una Elastic Cloud Compute

**Paso 1:** 

Se lanzó una instancia de AWS de tipo EC2, la Amazon Machine Image (AMI) que se eligió fue una del tipo ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64bits. El tipo de instancia que se eligió fue una t2.micro que cuenta 8 GB de memoria.

![Ejemplo_AMI\textwidth](https://github.com/Rodriguit/Proyecto-final-equipo5-opt-2020/blob/main/infraestructura/images/AMI.png)

**Paso 2:** 

Se configuró la instancia siguiendo los pasos de la wiki de AWS del curso de optimización. En resumen, se tuvo que configurar una VPC, una subnet pública y un grupo de seguridad. 

![Ejemplo_vpc\textwidth](https://github.com/Rodriguit/Proyecto-final-equipo5-opt-2020/blob/main/infraestructura/images/vpc.png)
![Ejemplo_sgp\textwidth](https://github.com/Rodriguit/Proyecto-final-equipo5-opt-2020/blob/main/infraestructura/images/sgp.png)

**Instalación de herramientas de trabajo Docker y Git**
![Ejemplo_vpc\textwidth](https://github.com/Rodriguit/Proyecto-final-equipo5-opt-2020/blob/task3_computo_nube/images/vpc.png)
