
from pulp import LpMinimize, LpProblem, LpVariable, lpSum # pip install pulp
# Definir los nodos de origen y destino
origenes = ['O1', 'O2', 'O3', 'O4', 'O5']
destinos = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10']

# Definir los costos de transporte
costos = {
    'O1': [120, 80, 85, 75, 94, 85, 98, 105, 125, 135],
    'O2': [110, 0, 85, 78, 92, 104, 110, 112, 130, 85],
    'O3': [90, 0, 0, 74, 88, 0, 55, 78, 80, 0],
    'O4': [78, 117, 60, 64, 0, 78, 69, 77, 74, 78],
    'O5': [65, 47, 78, 75, 44, 122, 71, 45, 68, 88]
}

# Definir la demanda y la capacidad
demanda = [85, 95, 110, 70, 60, 75, 90, 95, 100, 120]
capacidad = [450, 110, 210, 120, 250]

# Crear el problema de optimización
problema = LpProblem("Problema_de_Transporte", LpMinimize)

# Definir las variables de decisión
x = LpVariable.dicts("Envios", (origenes, destinos), lowBound=0, cat='Integer')

# Definir la función objetivo
problema += lpSum(costos[origen][destino] * x[origen][destino] for origen in origenes for destino in destinos), "Costo_Total_de_Transporte"

# Restricciones de capacidad de los nodos de origen
for origen in origenes:
    problema += lpSum(x[origen][destino] for destino in destinos) <= capacidad[origenes.index(origen)], f"Capacidad_de_{origen}"

# Restricciones de demanda de los nodos de destino
for destino in destinos:
    problema += lpSum(x[origen][destino] for origen in origenes) == demanda[destinos.index(destino)], f"Demanda_de_{destino}"

# Restricción adicional: Las unidades despachadas por O1 y O5 deben ser el doble de las despachadas por O2 y O4
problema += lpSum(x['O1'][destino] + x['O5'][destino] for destino in destinos) >= 2 * lpSum(x['O2'][destino] + x['O4'][destino] for destino in destinos)

# Restricción adicional: Nodo D4 debe ser atendido por O3 con al menos 10 unidades
problema += lpSum(x['O3'][destino] for destino in destinos) >= 10

# Restricción adicional: Nodo D8 debe ser atendido por O4 con al menos 15 unidades
problema += lpSum(x['O4'][destino] for destino in destinos) >= 15

# Restricción adicional: Nodo O3 debe dar suministro a al menos un nodo tipo D con no menos de 200 unidades en total
problema += lpSum(x['O3'][destino] for destino in destinos) >= 200

# Restricción adicional: La suma de lo que entregan O1, O2, O3 debe ser al menos 550 unidades
problema += lpSum(x['O1'][destino] + x['O2'][destino] + x['O3'][destino] for destino in destinos) >= 550

# Resolver el problema
problema.solve()

# Imprimir el resultado
print("Estado de la solución:", LpProblem.status[problema.status])
print("Costo Total de Transporte:", round(problema.objective.value(), 2))
print("Asignaciones:")
for origen in origenes:
    for destino in destinos:
        if x[origen][destino].value() != 0:
            print(f"{origen} -> {destino}: {int(x[origen][destino].value())}")

