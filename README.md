EXAMEN GLOBAL - PROGRAMACIÓN I - PYTHON

Integrantes: Lautaro Mubilla, Adrián Fredes, Matias Gobbi y Facundo Ríos
Comisión: 3

¿Cómo ejecuto y utilizo el programa? (+ Caso de ejemplo)

Ejecutamos directamente el archivo llamado "ejecutable.py".

Nos mostrará un menú de bienvenida en el cual se nos explica cuales son las bases nitrogenadas y que debemos
ingresar el ADN como una secuencia de 6x6, por filas. Las bases nitrogenadas son A (Ademina), T (Timina),
C (Citosina) y G (Guanina).Cada fila debe contener 6 bases nitrogenadas. Es decir, una fila válida sería por 
ejemplo: "ATCGAT".

*CASO DE EJEMPLO*
 | | | | | | | |
 V V V V V V V V 

Supongamos que ingresamos la siguiente secuencia de ADN:

G C A A T A
A C C G T T
A C T A C C
G G T A C G
A T T C G A
G C A T A G

A continuación nos pregunta que deseamos hacer con la secuencia de ADN:
 
1. Detectar mutaciones
   (Busca secuencias de 4 letras iguales en cualquier dirección)

2. Mutar ADN
   (Modifica el ADN creando una secuencia de 4 letras consecutivas iguales)

3. Sanar ADN
   (Si hay mutaciones, genera un nuevo ADN sin mutaciones)

4. Salir del programa

Seleccionamos la opción 1 (Detectar mutaciones). Nos pide que ingresemnos la sensibilidad de detección 
molecular y la precisión genómica en términos de porcentaje, ingresamos 100% en ambos. En este caso al no
detectar mutación, nos imprime el siguiente mensaje: "Análisis completado: Secuencia de ADN normal."

Nos devuelve al menú principal, ahora ingresamos la opción 2 (Mutar ADN). Nos pregunta si queremos mutación
por 1.Radiación (en horizontal o vertical) o 2.Virus (en diagonal), ingresamos la opción 1 (Radiación).

Datos que nos pide y los que ingresamos para mutar el ADN por radiación:

1- ¿ Que base desea repetir? (A, T, C, G): t
2- Numero de fila inicial (0-5): 4
3- Numero de columna inicial (0-5): 3
4- Intensidad de radiación (1-100%): 90
5- Tiempo de exposición (1-365 días): 200
6- Orientación (h: horizontal, v: vertical): v

Se completa la mutación y nos imprime el ADN original y el ADN mutado actual:

Mutación por radiación completada:
Intensidad: 90%
Tiempo de exposición: 200 días
Efecto total de radiación: 180 unidades de daño

ADN Original:
G C A A T A
A C C G T T
A C T A C C
G G T A C G
A T T C G A
G C A T A G

Nuevo ADN mutado:
G C A A T A
A C C G T T
A C T A C C
G G T A C G
A T T T G A
G C A T A G

Ahora seguimos con la 3° opción(SANAR), está función lo que hace es sanar el ADN que acabamos de mutar, esté detecta el mutante y crea un ADN nuevo diferente al anterior sin mutantes:
Analizando el ADN actual...


                                ¡Se encontraron mutaciones!



Generando nuevo ADN sano...
.....
.....
.....
.....


Aplicando tratamiento de potencia 4/5
Duración del tratamiento: 2 días
...
...
...

¡Sanación completada!
G G G C G T
A T T A A C
G A T A G G
G C T A A A
C T G C T T
G C C T C T

Acá se llega al final, la opción 4(Salir) da el cierre al programa.
