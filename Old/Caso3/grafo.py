matriz = [
    [0, 0.155496761, 0.189134437, 0.376075588, 0.454497079, 0.310501434, 0.179865362, 0.136754465, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0.262017732, 0.15397125, 0, 0.395923486, 0, 0.20393732, 0, 0.120331959, 0.175597187, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0.128877016, 0.444914304, 0.150246742, 0.389639702, 0, 0.475313895, 0, 0, 0, 0, 0, 0.432986787, 0, 0, 0],
    [0, 0, 0, 0, 0.306155449, 0.178937393, 0, 0.159485361, 0, 0.425794223, 0, 0, 0.437349762, 0, 0, 0, 0, 0],
    [0, 0.40767154, 0, 0, 0, 0.135939897, 0.148258889, 0, 0, 0, 0.2615108, 0.28105713, 0.276090304, 0.323998309, 0, 0.295562121, 0.032156173, 0],
    [0, 0, 0, 0, 0, 0, 0.446041736, 0, 0.096876921, 0, 0, 0.296550829, 0.307313312, 0, 0, 0, 0.233174401, 0],
    [0, 0.229074005, 0, 0, 0.268836472, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0.13823556, 0, 0.368923799, 0.396813085, 0.411769069, 0, 0, 0, 0.010525636, 0, 0, 0, 0, 0, 0, 0],
    [0, 0.245357094, 0, 0, 0, 0, 0, 0, 0, 0, 0.254980312, 0, 0, 0, 0, 0, 0, 0.183403077, 0.363651505],
    [0, 0, 0, 0, 0, 0.260857177, 0.426771354, 0.132663905, 0.002422448, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.304628926, 0, 0.088814905, 0.370343865, 0, 0, 0, 0, 0, 0.357933895, 0, 0, 0.198244677, 0.06596253, 0.418015418, 0, 0, 0],
    [0, 0.253812124, 0, 0, 0, 0, 0, 0.230883743, 0.25502673, 0.274452617, 0.457688469, 0, 0, 0, 0, 0, 0, 0.295894717],
    [0.202195793, 0, 0.340920471, 0, 0, 0, 0.1786336, 0.41220521, 0, 0.448361404, 0, 0.2389475, 0, 0.342073283, 0.05891699, 0, 0.042096154, 0],
    [0, 0, 0.374637019, 0.368492473, 0, 0.362144522, 0.20575123, 0.330361441, 0.380288608, 0.049024768, 0, 0.205695017, 0, 0, 0, 0, 0, 0.461125946],
    [0, 0, 0, 0, 0, 0.442864061, 0.43223882, 0.458826034, 0.199974671, 0.070861687, 0, 0, 0.01423145, 0, 0.094364789, 0, 0, 0.188956916],
    [0, 0, 0, 0, 0, 0.222177328, 0.022266805, 0.397317366, 0, 0, 0.148555406, 0.40221623, 0, 0.435138815, 0.439564789, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0.317192939, 0, 0, 0.412463264, 0.207709598, 0, 0, 0, 0, 0.039709049, 0, 0],
    [0, 0, 0, 0, 0, 0.101924874, 0, 0.343341242, 0, 0, 0, 0.012171622, 0.108496178, 0.474826217, 0.421804222, 0.345076873, 0.141982154, 0]
]

#  matriz identica pero que en los valores donde no es 0 se coloca 1 y donde es 0 se coloca 0
matrizs = list(map(lambda x: list(map(lambda y: 1 if y != 0 else 0, x)), matriz))

# Path: dijkstra.py
def dijkstra(matriz, nodo_inicial):
    # Inicializamos las variables
    nodos = len(matriz)
    distancias = [float("inf")] * nodos
    visitados = [False] * nodos
    padre = [None] * nodos
    distancias[nodo_inicial] = 0
    # Ciclo principal
    for i in range(nodos):
        # Buscamos el nodo con la menor distancia
        nodo = None
        for j in range(nodos):
            if not visitados[j] and (nodo is None or distancias[j] < distancias[nodo]):
                nodo = j
        # Marcamos el nodo como visitado
        visitados[nodo] = True
        # Actualizamos las distancias
        for j in range(nodos):
            if matriz[nodo][j] and distancias[nodo] + matriz[nodo][j] < distancias[j]:
                distancias[j] = distancias[nodo] + matriz[nodo][j]
                padre[j] = nodo
    # Retornamos las distancias y los padres
    return distancias, padre

# Path: dijkstra.py
def camino_mas_corto(padre, nodo):
    if padre[nodo] is None:
        return [nodo]
    return camino_mas_corto(padre, padre[nodo]) + [nodo]

# Path: dijkstra.py
def main():
    # Ejecutamos el algoritmo de Dijkstra
    distancias, padre = dijkstra(matriz, 1)
    # Imprimimos la distancia mas corta, 16,17,18
    print("16:")
    print("Camino mas corto:", camino_mas_corto(padre, 16))
    print("Distancia mas corta:", distancias[16])
    print()

if __name__ == "__main__":
    main()
