# Importamos la librería necesaria para manejar el cubo
import numpy as np

# Creamos el cubo que guardará la información del horario
# El cubo tendrá dimensiones de 5x5x5 para representar los bloques del campus
horario = np.zeros((5,5,5))

# Agregamos información al cubo indicando los bloques y horas que tiene el estudiante ocupados
horario[1,2,1] = 8   # Bloque 1, hora 8
horario[2,3,2] = 9   # Bloque 2, hora 9
horario[3,1,3] = 10  # Bloque 3, hora 10
horario[4,4,4] = 11  # Bloque 4, hora 11

# Definimos la función que indicará al estudiante el camino a seguir
def indicar_camino(origen, destino):
    # Verificamos que el origen y destino sean diferentes
    if origen == destino:
        print("Ya estás en el bloque de destino")
        return
    
    # Verificamos que el bloque de destino no esté ocupado en la hora que se quiere llegar
    if horario[destino[0], destino[1], destino[2]] != 0:
        print("Lo siento, el bloque de destino está ocupado en esa hora")
        return
    
    # Definimos una función auxiliar para calcular la distancia entre dos bloques
    def distancia(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])
    
    # Creamos una lista con los posibles bloques intermedios entre origen y destino
    intermedios = []
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if horario[i,j,k] == 0 and (i,j,k) != origen and (i,j,k) != destino:
                    intermedios.append((i,j,k))
    
    # Ordenamos los bloques intermedios por distancia a destino
    intermedios.sort(key=lambda b: distancia(b, destino))
    
    # Buscamos el camino más corto desde origen a destino pasando por un bloque intermedio
    mejor_camino = None
    for intermedio in intermedios:
        if distancia(origen, intermedio) + distancia(intermedio, destino) < distancia(origen, mejor_camino) if mejor_camino else float('inf'):
            mejor_camino = intermedio
    
    # Si encontramos un bloque intermedio que permita llegar a destino, indicamos el camino a seguir
    if mejor_camino:
        print(f"Ve al bloque ({mejor_camino[0]+1},{mejor_camino[1]+1},{mejor_camino[2]+1}) y luego al bloque ({destino[0]+1},{destino[1]+1},{destino[2]+1})")
    else:
        print("Lo siento, no hay un camino disponible para llegar al bloque de destino")
        
# Ejemplo de uso
origen = (0,0,0)  
