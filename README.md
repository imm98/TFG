# TFG: Teoría de Nudos
Trabajo de Fin de Grado del Doble Grado en Ingeniería Informática y Matemáticas en la Universidad de Granada.

Este trabajo se divide en dos partes: una primera, dedicada al estudio matemático de la teoría de nudos, y una segunda, en la que, mediante la codificación de un nudo, se calculará su grupo fundamental para distinguirlo de otros nudos.

Comenzaremos analizando la definición de nudo, el concepto de equivalencia entre nudos y los llamados invariantes de nudos. Dentro de estos invariantes, nos centraremos en el grupo fundamental de un nudo. Para ello, describiremos el proceso de cálculo de presentaciones de dicho grupo para cualquier nudo admisible.

En la segunda parte, presentaremos distintas codificaciones de nudos, necesarias para que un programa informático pueda identificarlos a partir de una cantidad finita de datos. Optaremos por la notación Dowker para representar un nudo cualquiera y construiremos una clase llamada **Nudo** (disponible [aquí](https://github.com/imm98/TFG/blob/main/claseNudo.py)), que recibirá la notación Dowker de un nudo, lo representará gráficamente mediante el módulo Turtle de Python, calculará dos presentaciones de su grupo fundamental y visualizará el nudo junto con los espacios asociados necesarios para obtener dichas presentaciones.

# Final Degree Project: Knot Theory
Undergraduate Thesis for the Double Degree in Computer Science and Mathematics at the University of Granada.

This project is divided into two parts: the first part focuses on the mathematical study of knot theory, while the second part involves encoding a knot to compute its fundamental group, thereby distinguishing it from other knots.

We will begin by examining the definition of a knot, the concept of knot equivalence, and so-called knot invariants. Among these invariants, we will concentrate on the fundamental group of a knot. To this end, we will describe the process of computing group presentations for any admissible knot.

In the second part, we will introduce different knot encodings, which are necessary for a computer program to identify a knot using a finite set of data. We will choose Dowker notation to represent an arbitrary knot and construct a class called **Knot** (available [here](https://github.com/imm98/TFG/blob/main/claseNudo.py)), which will take a knot's Dowker notation as input, visualize it using Python's Turtle module, compute two presentations of its fundamental group, and display the knot along with the associated spaces required for deriving these presentations.
