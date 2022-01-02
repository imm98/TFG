# TFG: Teoría de Nudos
Trabajo de Fin de Grado del Doble Grado en Ingeniería Informática y Matemáticas en la Universidad de Granada.

Este trabajo se dividirá en dos partes, una primera en la que se realizará un estudio matemático de la teoría de nudos y una segunda en la que gracias a una codificación de un nudo trataremos de calcular el grupo de dicho nudo para poder distinguirlo de otros nudos.

Comenzaremos por estudiar la definición de nudo, el concepto de equivalencia de nudos y los llamados invariantes de nudos. Dentro de dichos invariantes, en este trabajo nos centraremos en el grupo de un nudo, para lo cual describiremos el proceso de cálculo de presentaciones de dicho grupo para un nudo admisible cualquiera.

En la segunda parte, describiremos diferentes codificaciones de nudos, que serán necesarias para que un programa informático identifique el nudo que queremos estudiar mediante una cantidad finita de datos. Escogeremos la notación Dowker para identificar a un nudo cualquiera y construiremos una clase llamada Nudo, disponible [aquí](https://github.com/imm98/TFG/blob/main/claseNudo.py), que reciba la notación Dowker de un nudo y lo represente utilizando el módulo Turtle de Python, calcule dos presentaciones del grupo de dicho nudo y represente el nudo con sus espacios asociados requeridos para hallar dichas presentaciones.
