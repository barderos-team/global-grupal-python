from clases import Detector, Radiacion, Virus, Sanador
from random import randint

def obtener_matriz() -> list[str]:
    mensaje_inicial = """
BIENVENIDO AL ANALIZADOR DE ADN
===============================

El ADN está compuesto por 4 bases nitrogenadas:

- A (Adenina)
- T (Timina)
- C (Citosina)
- G (Guanina)

Necesitamos que ingrese una secuencia de ADN de 6x6.
Esto significa que necesitará ingresar 6 filas, y cada fila debe tener 6 bases.
Por ejemplo: una fila válida seria: ATCGAT

 ingrese el ADN fila por fila:"""
    
    print(mensaje_inicial)
    
    matriz = []
    for i in range(6):
        while True:
            fila = input(f"\nIngrese fila {i+1} (6 letras usando solo A, T, C, G): ").upper()
            if len(fila) == 6 and all(base in 'ATCG' for base in fila):
                matriz.append(fila)
                break
            print("¡Error! La fila debe tener exactamente 6 letras y solo puede contener A, T, C, G")
    return matriz


def mostrar_matriz(matriz: list[str]) -> None:
    for fila in matriz:
        print(' '.join(map(str, fila)))
    print()  

def validar_posicion_mutacion(fila: int, columna: int) -> bool:
    print("Ejecutando validacion de posicion...")
    if fila > 2 or columna > 2: 
        print("\n¡Error! Para mutar correctamente, la fila y columna deben ser máximo 2")
        print("(necesitamos espacio para 4 bases en diagonal)")
        return False
    else:
        print("Posicion evaluada como correcta")    
        return True

def main() -> None:
    matriz = obtener_matriz()
    
    # Al inicio
    print("\nMatriz inicial:")
    mostrar_matriz(matriz)
    
    while True:
        menu_principal = """
========================================
                MENU PRINCIPAL
========================================

¿Qué desea hacer con esta secuencia de ADN?

1. Detectar mutaciones
   (Busca secuencias de 4 letras iguales en cualquier dirección)

2. Mutar ADN
   (Modifica el ADN creando una secuencia de 4 letras consecutivas iguales)

3. Sanar ADN
   (Si hay mutaciones, genera un nuevo ADN sin mutaciones)

4. Salir del programa

Seleccione una opción (1-2-3-4): """
        
        opcion = input(menu_principal)
        
        if opcion == "1":
            mensaje_detector = """
========================================
           DETECTOR DE MUTACIONES
========================================

Configurando secuenciador de ADN...
Este dispositivo analiza las secuencias de bases nitrogenadas.

La sensibilidad indica la capacidad de detectar mutaciones reales.
La precisión determina la exactitud al identificar bases mutadas."""
            print(mensaje_detector)

            while True:
                try:
                    print("\nPor favor, calibre el secuenciador:")
                    sensibilidad = int(input("Sensibilidad de detección molecular (1-100%): "))
                    precision = int(input("Precisión en el análisis genómico (1-100%): "))
                    detector = Detector(sensibilidad, precision)
                    break
                except ValueError as e:
                    print(f"\n¡Error de calibración! {e}")
                    print("Por favor, ajuste nuevamente los parámetros.")

            print(f"\nIniciando análisis genético con:")
            print(f"- Sensibilidad molecular: {detector.sensibilidad}%")
            print(f"- Precisión genómica: {detector.precision}%")
            print("\nAnalizando secuencia de bases nitrogenadas...")
            print("Buscando patrones de mutación...")
            
            if detector.detectar_mutantes(matriz):
                resultado_deteccion = """
¡ALERTA! Mutación detectada en la secuencia de ADN.

Se han identificado 4 bases nitrogenadas idénticas consecutivas,
lo cual indica una alteración en la estructura genética normal.
(secuencia encontrada en dirección horizontal, vertical o diagonal)"""
            else:
                resultado_deteccion = """
Análisis completado: Secuencia de ADN normal.

No se detectaron alteraciones en el patrón de bases nitrogenadas.
La estructura genética mantiene su configuración estándar."""

            print(resultado_deteccion)
                
        elif opcion == "2":
            mensaje_mutacion = """
========================================
           CREADOR DE MUTACIONES
========================================

 tipos de mutaciones que podemos crear:

1. Mutacion por Radiación - Crea mutaciones rectas (horizontal o vertical)

2. Mutacion por Virus - Crea mutaciones diagonales"""


            print(mensaje_mutacion)
            
        
            
            tipo = input("\nSeleccione el tipo de mutación (1 o 2): ")
            base = input("¿ Que base desea repetir? (A, T, C, G): ").upper()
            print("\nLas filas y columnas se numeran del 0 al 5")
            fila = int(input("Numero de fila inicial (0-5): "))
            columna = int(input("Numero de columna inicial (0-5): "))

             
            if validar_posicion_mutacion(fila, columna):
                while True:  
                    if tipo == "1":  
                            try:
                                print("\nConfigurando mutación por radiación:")
                                intensidad = int(input("Intensidad de radiación (1-100%): "))
                                duracion = int(input("Tiempo de exposición (1-365 días): "))
                                mutador = Radiacion(base, intensidad, duracion)

                                orientacion = input("Orientación (h: horizontal, v: vertical): ")
                                matriz_original = matriz.copy()  
                                matriz = mutador.crear_mutante(matriz, (fila, columna), orientacion)
                                print(f"\nMutación por radiación completada:")
                                print(f"Intensidad: {mutador.intensidad}%") 
                                print(f"Tiempo de exposición: {mutador.duracion} días")
                                print(f"Efecto total de radiación: {mutador.efecto_total} unidades de daño")
                
                                # Solo mostrar una vez el resultado
                                print("\nADN Original:")
                                mostrar_matriz(matriz_original)
                                print("Nuevo ADN mutado:")
                                mostrar_matriz(matriz)
                                break
                            except ValueError as e:
                                print(f"\n¡Error! {e}")
                                print("Por favor, ajuste los parámetros nuevamente.\n")            
                    else:
                
                        while True:
                            try:
                                print("\nConfigurando mutación viral:")
                                intensidad = int(input("Agresividad del virus (1-100%): "))
                                duracion = int(input("Período de infección (1-14 días): "))
                                mutador = Virus(base, intensidad, duracion)
                                break
                            except ValueError as e:
                                print(f"\n¡Error! {e}")
                                print("Por favor, ajuste los parámetros nuevamente.\n")
                    
                        matriz_original = matriz.copy()  
                        matriz = mutador.crear_mutante(matriz, (fila, columna))
                        print(f"\nInfección viral completada:")
                        print(f"Agresividad: {mutador.intensidad}%")
                        print(f"Período de infección: {mutador.duracion} días")
                        print(f"Efecto total viral: {mutador.efecto_total} unidades de daño")                  
            else:
                print("\nNo se pudo crear la mutación en esa posicion")
                continue

        elif opcion == "3":
            mensaje_sanador = """
========================================
            SANADOR DE ADN
========================================

Analizando el ADN actual..."""


            print(mensaje_sanador)
            
            sanador = Sanador(
                potencia=randint(1, 5),     
                tiempo=randint(2, 6)        
            )
            matriz_nueva = sanador.sanar_mutantes(matriz)
            
            if matriz_nueva != matriz:
                resultado_sanacion = f"""

                                ¡Se encontraron mutaciones!

                
                
Generando nuevo ADN sano...
.....
.....
.....
.....


Aplicando tratamiento de potencia {sanador.potencia}/5
Duración del tratamiento: {sanador.tiempo} días
...
...
...

¡Sanación completada!"""


                matriz = matriz_nueva
            else:
                resultado_sanacion = "\nEl ADN está sano, no necesita sanación."
            print(resultado_sanacion)
            mostrar_matriz(matriz)
                
        elif opcion == "4":
            print("\n¡Gracias por usar el analizador de ADN!\n¡Hasta luego!")
            break
            
        else:
            print("\n¡Error! Por favor, seleccione una opción válida (1-4).")

if __name__ == "__main__":
    main()