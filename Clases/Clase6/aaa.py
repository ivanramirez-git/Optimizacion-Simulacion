# La empresa XXX que arrienda equipos a sus clientes trabaja con 4 referencias diferentes. Tiene 5 clientes clave y sobre ellos quiere realizar un análisis que le permita disminuir la cantidad de dias tarde con los que entrega a los clientes, ya que por cada día que entregue tarde, deberá pagarle al cliente una penalización, que al final se descontará del total de la facturación que se le genere a ese cliente.  
# Se van a analizar los 12 pedidos de los próximos 7 dias. La siguiente es la tabla que muestra qué cliente hace qué pedido: (filas: clientes, columnas: pedidos)
# Tabla de los pedidos que hace cada cliente:

# 	1	2	3	4	5	6	7	8	9	10	11	12
# 1	0	1	0	0	0	0	0	0	0	0	0	1
# 2	0	0	0	1	0	0	0	1	0	1	0	0
# 3	0	0	1	0	0	0	1	0	0	0	0	0
# 4	0	0	0	0	1	0	0	0	1	0	0	0
# 5	1	0	0	0	0	1	0	0	0	0	1	0

# La composición, de acuerdo con la cantidad de equipos, de cada pedido se presenta a continuación: (filas: referencias, columnas: pedidos)
# Tabla composición de pedidos: (dada en cantidad de equipos por referencia)

#     1	2	3	4	5	6	7	8	9	10	11	12
# 1	3	4	0	1	2	1	2	5	0	3	2	0
# 2	2	3	0	1	1	3	2	5	0	3	2	0
# 3	4	2	1	1	1	4	2	5	0	0	0	5
# 4	1	4	2	2	1	4	1	1	5	0	0	0


# Cada uno de los 12 pedidos es solicitado para una fecha específica, es decir los equipos que solicita un cliente por medio de un pedido deberían entregarse un día especifico. La siguiente es la tabla que muestra el día en el que debería entregarse el pedido: (filas: día, columnas: pedido)
# Tabla de día de entrega de los equipos al cliente, de acuerdo con cada pedido:

#     1	2	3	4	5	6	7	8	9	10	11	12
# 1	1	0	0	0	0	0	0	0	0	0	0	0
# 2	0	1	1	1	0	0	0	0	0	0	0	0
# 3	0	0	0	0	1	0	0	0	0	0	0	0
# 4	0	0	0	0	0	1	1	1	0	0	0	0
# 5	0	0	0	0	0	0	0	0	1	1	1	1
# 6	0	0	0	0	0	0	0	0	0	0	0	0
# 7	0	0	0	0	0	0	0	0	0	0	0	0


# Asi mismo, los clientes deben regresar (retornar o devolver) los equipos en una fecha específica. A continuación se muestra la fecha en la que el cliente debe regresar los equipos que le fueron entregados en cada pedido: (filas: día, columnas: pedido)
# Tabla de día de retorno de los equipos por parte del cliente a la empresa XXX, de acuerdo con cada pedido:

# 	1	2	3	4	5	6	7	8	9	10	11	12
# 1	0	0	0	0	0	0	0	0	0	0	0	0
# 2	1	0	0	0	0	0	0	0	0	0	0	0
# 3	0	0	1	0	0	0	0	0	0	0	0	0
# 4	0	1	0	1	0	0	0	0	0	0	0	0
# 5	0	0	0	0	1	1	0	0	0	0	0	0
# 6	0	0	0	0	0	0	1	1	0	1	0	0
# 7	0	0	0	0	0	0	0	0	1	0	1	1

# A continuación se muestra la cantidad de equipos con los que cuenta la empresa al inicio del horizonte de análisis:
# Tabla de inventario de equipos: 

# Referencia	Cantidad
# 1	2
# 2	2
# 3	2
# 4	2

# Informacion adicional:
# Los clientes solicitan que los equipos lleguen por la mañana y en el momento en que los devuelve (retorna o regresa), lo hace al finalizar el día.
# La empresa XXX puede entregar los equipos en cualquier día, desde el día que los solicita el cliente, hasta el día que el cliente los retorna (inclusive ese día). Lo anterior quiere decir que, la empresa XXX puede entregar los pedidos incompletos y puede ir suministrando los equipos que falten en los dias siguientes. Esto lo acepta el cliente por la necesidad de equipos que tiene, pero tiene en el contrato una clausula donde penaliza a la empresa XXX por cada día que pase sin recibir el equipo que le falta. 
# Según el contrato que se tiene con cada cliente, el valor (costo) por día, por equipo que no se entregue, para cada clientes es:

# Cliente	Penalización
# 1	100
# 2	120
# 3	80
# 4	70
# 5	125


# Explicación de tablas con ejemplo numérico:
# De acuerdo con las tablas suministradas, un ejemplo según los datos sería el siguiente:
# El cliente 5 hizo el pedido 11. Ese pedido está compuesto por 2 equipos de la referencia 1 y 2 equipos de la referencia 2. De esos equipos solicitados, deberá entregar los equipos que tenga disponibles en el día 5, en la mañana. Si no tiene los 4 equipos completos, puede entregar los equipos faltantes el día 6, e inclusive el día 7 (hasta que los complete, si puede). En el día 7, en la noche, el cliente devuelve a la empresa XXX los equipos que le fueron arrendados. Si recibió 2 equipos, regresa 2 equipos, si recibió 4 equipos regresa 4 equipos, si no recibió nada, no regresa nada.
# Escenario 1:
# Si el cliente solo recibió 1 equipo el día 5, el faltante es de 3
# Si el cliente no recibió nada en el día 6, el faltante es de 3
# Si el cliente no recibió nada en el día 7, el faltante es de 3
# Total monto a penalizar para ese cliente: 3*(125) + 3*(125) + 3*(125) = 1.125
# Cantidad de equipos a devolver en el día 7:  1
# Escenario 2:
# Si el cliente solo recibió 1 equipo el día 5, el faltante es de 3
# Si el cliente recibió otro equipo en el día 6, el faltante es de 2
# Si el cliente no recibió nada en el día 7, el faltante es de 2
# Total monto a penalizar para ese cliente: 3*(125) + 2*(125) + 2*(125) = 875
# Cantidad de equipos a devolver en el día 7:  2


# Desarrollo:
# Construya y solucione con el uso de la librearía PULP (Pyhton) o Gusek un modelo que permita minimizar el monto total de penalización que va a recibir la empresa XXX, por entregar tarde los equipos a sus clientes. Todas las restricciones deben cumplirse.
# Diligencie la siguiente tabla con los resultados del modelo (filas: clientes, columnas: dias). Debe registrar la cantidad de equipos que quedaron sin entregar en cada día, para cada cliente.


# cliente	Dia 1	Dia 2	Dia 3	Dia 4	Dia 5	Dia 6	Dia 7
# 1							
# 2							
# 3							
# 4							
# 5							
# Total Función objetivo	


# Restricciones:
# Debe cumplir con todas las restricciones generadas a partir de las tablas del contexto del problema.
# Recuerde que, el cliente solo recibe, como máximo, lo que pidió, puede recibir menos, pero no más equipos.
# Recuerde que, si la empresa XXX no tiene completos los pedidos, igual puede ir haciendo entregas parciales, inclusive en el mismo día que el cliente debe devolverlos
# Recuerde que, la empresa presta los equipos en la mañana y el cliente se los devuelve en la noche.
# Recomendaciones:
# Utilice la formula del inventario. Tenga en cuenta que la empresa cuenta con un inventario inicial de equipos. Las salidas de unidades son los equipos que se entregan a los clientes y las entradas de unidades son los retornos o regresos que hacen los clientes cuando se cumple el día de regreso de estos. Los clientes solo pueden regresar, retornar o devolver los equipos que efectivamente se le entregaron. El retorno se hace en el día acordado, no antes, no después.
# Utilice las tablas suministradas como desee, es decir puede generar nuevas tablas a partir de las dadas, siempre y cuando no cambie el enunciado, contexto, ni los datos del problema.
# Es importante que tenga en cuenta que, como hay penalización, no debe incluir restricción de cumplimiento de demanda. Si se puede cumplir la demanda, se cumple y si no se genera penalización.

# Solución:

from pulp import * # pip install pulp

modelo = LpProblem("Empresa de arriendo de equipos", LpMinimize)
clientes = [1, 2, 3, 4, 5]
dias = [1, 2, 3, 4, 5, 6, 7]
pedidos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
referencias = [1, 2, 3, 4]
penalizacion = {1: 100, 2: 120, 3: 80, 4: 70, 5: 125}
inventario = {1: 2, 2: 2, 3: 2, 4: 2}

# Se van a analizar los 12 pedidos de los próximos 7 dias. La siguiente es la tabla que muestra qué cliente hace qué pedido: (filas: clientes, columnas: pedidos)
# Tabla de los pedidos que hace cada cliente:
pedidos_cliente = {
    1: {1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 1},
    2: {1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 1, 9: 0, 10: 1, 11: 0, 12: 0},
    3: {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 1, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0},
    4: {1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 0, 7: 0, 8: 0, 9: 1, 10: 0, 11: 0, 12: 0},
    5: {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 0, 9: 0, 10: 0, 11: 1, 12: 0}
}

# La composición, de acuerdo con la cantidad de equipos, de cada pedido se presenta a continuación: (filas: referencias, columnas: pedidos)
# Tabla composición de pedidos: (dada en cantidad de equipos por referencia)
composicion = {
    1: {1: 3, 2: 4, 3: 0, 4: 1, 5: 2, 6: 1, 7: 2, 8: 5, 9: 0, 10: 3, 11: 2, 12: 0},
    2: {1: 2, 2: 3, 3: 0, 4: 1, 5: 1, 6: 3, 7: 2, 8: 5, 9: 0, 10: 3, 11: 2, 12: 0},
    3: {1: 4, 2: 2, 3: 1, 4: 1, 5: 1, 6: 4, 7: 2, 8: 5, 9: 0, 10: 0, 11: 0, 12: 5},
    4: {1: 1, 2: 4, 3: 2, 4: 2, 5: 1, 6: 4, 7: 1, 8: 1, 9: 5, 10: 0, 11: 0, 12: 0}
}

# Cada uno de los 12 pedidos es solicitado para una fecha específica, es decir los equipos que solicita un cliente por medio de un pedido deberían entregarse un día especifico. La siguiente es la tabla que muestra el día en el que debería entregarse el pedido: (filas: día, columnas: pedido)
# Tabla de día de entrega de los equipos al cliente, de acuerdo con cada pedido:
entrega = {
    1: {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0},
    2: {1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0},
    3: {1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0},
    4: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 1, 8: 1, 9: 0, 10: 0, 11: 0, 12: 0},
    5: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 1, 11: 1, 12: 1},
    6: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0},
    7: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
}

# Asi mismo, los clientes deben regresar (retornar o devolver) los equipos en una fecha específica. A continuación se muestra la fecha en la que el cliente debe regresar los equipos que le fueron entregados en cada pedido: (filas: día, columnas: pedido)
# Tabla de día de retorno de los equipos por parte del cliente a la empresa XXX, de acuerdo con cada pedido:
retorno = {
    1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0},
    2: {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0},
    3: {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0},
    4: {1: 0, 2: 1, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0},
    5: {1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0},
    6: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1, 9: 0, 10: 1, 11: 0, 12: 0},
    7: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 0, 11: 1, 12: 1}
}

x = LpVariable.dicts("x", (clientes, dias, pedidos), lowBound=0, upBound=1, cat="Binary")

# La función objetivo es minimizar la penalización
# Formula: Sumatoria de la penalización por la cantidad de equipos que no se entregaron
modelo += lpSum(penalizacion[c] * x[c][d][p] for c in clientes for d in dias for p in pedidos)

# Restricciones

# Restricción de que solo se puede entregar un pedido por día
# Formula: Sumatoria de los pedidos por cliente por día es menor o igual a 1
for c in clientes:
    for d in dias:
        modelo += lpSum(x[c][d][p] for p in pedidos) <= 1
        
# Restricción de que la cantidad de equipos entregados es igual a la cantidad de equipos que pidió el cliente
# Formula: Sumatoria de los pedidos por cliente por día es igual a la cantidad de equipos que pidió el cliente
for p in pedidos:
    modelo += lpSum(x[c][d][p] for c in clientes for d in dias) == 1
    
# Restricción de que la cantidad de equipos entregados es igual a la cantidad de equipos que pidió el cliente
# Formula: Sumatoria de los pedidos por cliente por día es igual a la cantidad de equipos que pidió el cliente
for c in clientes:
    for p in pedidos:
        modelo += lpSum(x[c][d][p] for d in dias) == pedidos_cliente[c][p]
        
# Restricción de que la cantidad de equipos entregados es igual a la cantidad de equipos que pidió el cliente
# Formula: Sumatoria de los pedidos por cliente por día es igual a la cantidad de equipos que pidió el cliente
for p in pedidos:
    for r in referencias:
        modelo += lpSum(x[c][d][p] * composicion[r][p] for c in clientes for d in dias) <= inventario[r]

# Restricción de que la cantidad de equipos entregados es igual a la cantidad de equipos que pidió el cliente
# Formula: Sumatoria de los pedidos por cliente por día es igual a la cantidad de equipos que pidió el cliente
for c in clientes:
    for p in pedidos:
        modelo += lpSum(x[c][d][p] for d in dias) == entrega[c][p]
        
# Restricción de que la cantidad de equipos entregados es igual a la cantidad de equipos que pidió el cliente
# Formula: Sumatoria de los pedidos por cliente por día es igual a la cantidad de equipos que pidió el cliente
for c in clientes:
    for p in pedidos:
        modelo += lpSum(x[c][d][p] for d in dias) == retorno[c][p]
        
# Resolver el modelo
modelo.solve()

# Tabla 
# Diligencie la siguiente tabla con los resultados del modelo (filas: clientes, columnas: dias). Debe registrar la cantidad de equipos que quedaron sin entregar en cada día, para cada cliente.
print(f"Estado: {LpStatus[modelo.status]}")
print("Cliente\tDia 1\tDia 2\tDia 3\tDia 4\tDia 5\tDia 6\tDia 7")
for c in clientes:
    print(c, end="\t")
    for d in dias:
        print(lpSum(x[c][d][p].varValue for p in pedidos), end="\t")
    print()
print(f"Total Función objetivo: {value(modelo.objective)}")
