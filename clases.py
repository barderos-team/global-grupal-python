
from typing import List
import random
from random import randint

class Detector:
    "Clase para detectar mutaciones en secuencias de ADN"
    def __init__(self, 
                 sensibilidad: int = None,
                 precision: int = None):
        
        if sensibilidad is None:
            self.sensibilidad = randint(70, 100)  
        elif sensibilidad < 1 or sensibilidad > 100:
            raise ValueError(f"La sensibilidad debe estar entre 1% y 100%. Valor recibido: {sensibilidad}%")
        else:
            self.sensibilidad = sensibilidad
            
        
        if precision is None:
            self.precision = randint(70, 100)  
        elif precision < 1 or precision > 100:
            raise ValueError(f"La precisión debe estar entre 1% y 100%. Valor recibido: {precision}%")
        else:
            self.precision = precision
    
    def detectar_mutantes(self, matriz: List[str]) -> bool:
        """
        Detecta si hay mutaciones en la matriz de ADN
        Args:
            matriz: Matriz de ADN a analizar
        Returns:
            booleano: True si hay mutaciones, False si no
        """
        return any([
            self._detectar_horizontal(matriz),
            self._detectar_vertical(matriz),
            any(self._detectar_diagonal(matriz, (i, j)) 
                for i in range(len(matriz)) 
                for j in range(len(matriz[0])))
        ])
    
    def _detectar_horizontal(self, matriz):
        for fila in matriz:
            if self._detectar_secuencia(fila):
                return True
        return False
    
    def _detectar_vertical(self, matriz):
        for j in range(len(matriz[0])):
            columna = [matriz[i][j] for i in range(len(matriz))]
            if self._detectar_secuencia(columna):
                return True
        return False
    
    def _detectar_diagonal(self, matriz, posicion):
        fila, columna = posicion
        secuencia = matriz[fila][columna]
        contador = 1
        
        # diagonal hacia abajo-derecha
        i, j = fila + 1, columna + 1
        while i < len(matriz) and j < len(matriz[0]) and matriz[i][j] == secuencia:
            contador += 1
            i += 1
            j += 1
        
        # diagonal hacia abajo-izquierda
        i, j = fila + 1, columna - 1
        while i < len(matriz) and j >= 0 and matriz[i][j] == secuencia:
            contador += 1
            i += 1
            j -= 1
        
        return contador >= 4
    
    def _detectar_secuencia(self, secuencia):
        for i in range(len(secuencia)-3):
            if len(set(secuencia[i:i+4])) == 1:
                return True
        return False

class Mutador:
    "Clase base para crear mutaciones"
    def __init__(self, base_nitrogenada: str, intensidad: float, duracion: int):
        self.base_nitrogenada = base_nitrogenada
        self.intensidad = intensidad
        self.duracion = duracion
    
    def crear_mutante(self):
        "Método base para crear mutantes"
        pass

class Radiacion(Mutador):
    """Clase para crear mutaciones por radiación"""
    def __init__(self, base: str, 
                 intensidad: int = None,
                 duracion: int = None):
        self.base_nitrogenada = base
        
        # Intensidad en porcentaje
        if intensidad is None:
            self.intensidad = randint(1, 100)
        elif intensidad < 1 or intensidad > 100:
            raise ValueError(f"La intensidad de radiación debe estar entre 1% y 100%. Valor recibido: {intensidad}%")
        else:
            self.intensidad = intensidad
            
        # Duración en días (1-365)
        if duracion is None:
            self.duracion = randint(1, 365)
        elif duracion < 1 or duracion > 365:
            raise ValueError(f"La duración debe estar entre 1 y 365 días. Valor recibido: {duracion}")
        else:
            self.duracion = duracion
        
        # Calcula el efecto total según intensidad y días
        self.efecto_total = (self.duracion * self.intensidad) // 100
    
    def crear_mutante(self, matriz: List[str], posicion_inicial: tuple, 
                     orientacion_de_la_mutacion: str) -> List[str]:
        """
        Crea mutaciones horizontales o verticales
        Args:
            matriz: Matriz de ADN a mutar
            posicion_inicial: Tupla (x,y) donde inicia la mutación
            orientacion_de_la_mutacion: 'H' para horizontal, 'V' para vertical
        Returns:
            List[str]: Matriz mutada
        """
        x, y = posicion_inicial
        matriz_mutada = [list(fila) for fila in matriz]
        
        if orientacion_de_la_mutacion.upper() == 'H':
            for i in range(4):
                if y > 2:
                    if y + i < len(matriz_mutada[0]):
                        matriz_mutada[x][y - i] = self.base_nitrogenada
                else:
                    if y + i < len(matriz_mutada[0]):
                        matriz_mutada[x][y + i] = self.base_nitrogenada    
        
        elif orientacion_de_la_mutacion.upper() == 'V':
            for i in range(4):
                if x > 2:
                    if x + i < len(matriz_mutada):
                        matriz_mutada[x - i][y] = self.base_nitrogenada
                else:
                    if x + i < len(matriz_mutada):
                        matriz_mutada[x + i][y] = self.base_nitrogenada    
        
        return [''.join(fila) for fila in matriz_mutada]

class Virus(Mutador):
    """Clase para crear mutaciones diagonales"""
    def __init__(self, base: str,
                 intensidad: int = None,
                 duracion: int = None):
        self.base = base
        
        # Intensidad en porcentaje
        if intensidad is None:
            self.intensidad = randint(1, 100)
        elif intensidad < 1 or intensidad > 100:
            raise ValueError(f"La agresividad viral debe estar entre 1% y 100%. Valor recibido: {intensidad}%")
        else:
            self.intensidad = intensidad
            
        # Duración en días (período de cuarentena)
        if duracion is None:
            self.duracion = randint(1, 14)
        elif duracion < 1 or duracion > 14:
            raise ValueError(f"El período de infección debe estar entre 1 y 14 días. Valor recibido: {duracion}")
        else:
            self.duracion = duracion
    
    def crear_mutante(self, matriz: List[str], posicion_inicial: tuple) -> List[str]:
        """
        Crea mutaciones diagonales
        Args:
            matriz: Matriz de ADN a mutar
            posicion_inicial: Tupla (x,y) donde inicia la mutación
        Returns:
            List[str]: Matriz mutada
        """
        x, y = posicion_inicial
        matriz_mutada = [list(fila) for fila in matriz]
        
        # Mutación diagonal
        for i in range(4):
            if (x + i < len(matriz_mutada) and 
                y + i < len(matriz_mutada[0])):
                matriz_mutada[x + i][y + i] = self.base_nitrogenada
        
        return [''.join(fila) for fila in matriz_mutada]

class Sanador:
    """Clase para sanar mutaciones en el ADN"""
    def __init__(self, 
                 potencia: int = None,
                 tiempo: int = None):
        # Validar potencia
        if potencia is None:
            self.potencia = randint(1, 5)
        elif potencia < 1 or potencia > 5:
            raise ValueError(f"La potencia debe estar entre 1 y 5. Valor recibido: {potencia}")
        else:
            self.potencia = potencia
            
        # Validar tiempo
        if tiempo is None:
            self.tiempo = randint(2, 6)
        elif tiempo < 2 or tiempo > 6:
            raise ValueError(f"El tiempo debe estar entre 2 y 6. Valor recibido: {tiempo}")
        else:
            self.tiempo = tiempo
    
    def sanar_mutantes(self, matriz: List[List[str]]) -> List[List[str]]:
        """
        Sana la matriz de ADN si contiene mutaciones
        Args:
            matriz: Matriz de ADN a sanar
        Returns:
            List[List[str]]: Nueva matriz de ADN sin mutaciones
        """
        detector = Detector(1.0, 1.0)
        if detector.detectar_mutantes(matriz):
            return self._generar_matriz_sana(len(matriz))
        return matriz
    
    def _generar_matriz_sana(self, n: int) -> List[List[str]]:
        """Genera una matriz de ADN aleatoria sin mutaciones"""
        bases = ['A', 'T', 'C', 'G']
        while True:
            matriz = [[random.choice(bases) for _ in range(n)] for _ in range(n)]
            detector = Detector(1.0, 1.0)
            if not detector.detectar_mutantes(matriz):
                return matriz