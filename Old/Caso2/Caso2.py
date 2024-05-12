'''
Problema: Problema de e-commerce con Abandonos

Tecnicompras es un sitio web de comercio electrónico donde los clientes pueden realizar pedidos en línea.
Los clientes visitan el sitio web y agregan productos a sus carritos de compra antes de proceder al proceso
de pago. De esta forma el proceso de compra en línea implica dos etapas: la primera etapa se forma cuando
un cliente agrega productos al carrito de compra, y la segunda etapa ocurre cuando el cliente realiza el
proceso de pago.

De acuerdo con los datos históricos se ha identificado que los clientes visitan el sitio web de acuerdo con
un proceso de llegadas Poisson y comienzan a llenar sus carritos de compra a una tasa de 10 clientes por
minuto. Igualmente, se ha determinado la velocidad a la que los clientes pueden completar la selección de
productos y pasar al proceso de pago, la cual es de 5 clientes por minuto. También, se ha estimado que la
velocidad a la que los clientes pueden completar el proceso de pago y finalizar su compra es 7 clientes por
minuto. Sin embargo, se ha notado que muchos clientes que ingresan al sitio web no completan su compra, es
decir los clientes pueden abandonan el proceso antes de realizar el pago influenciados por factores como la
complejidad del proceso de pago o problemas técnicos entre otros. En este caso, se ha encontrado que, en
promedio, 2 clientes por minuto abandonan el proceso. Todas las tasas encontradas son independientemente
distribuidoras de acuerdo con variables aleatorias exponenciales.

# Datos:
- Llegada de clientes: 10 clientes por minuto
- Selección de productos: 5 clientes por minuto
- Pago: 7 clientes por minuto
- Abandono: 2 clientes por minuto


El objetivo es analizar y optimizar el rendimiento del sistema de comercio electrónico. Para explicar
claramente su análisis del sistema realice un informe que explique claramente todo el trabajo que su grupo 
realizó para estudiar el problema. Tenga en cuenta incluir los siguientes elementos en su estudio:

1.	Realice un diagrama explicativo del e-commerce
2.	Realice el diagrama de flujo del algoritmo que empleará
3.	¿Cuál es el tiempo promedio que un cliente pasa en cada cola antes de completar su compra?
4.	¿Cuál es la tasa efectiva de llegada de clientes que completan una compra?
5.	¿Qué estrategias podrían implementarse para reducir el tiempo de espera y la tasa de abandono?,
proponga un escenario de mejora y explícala claramente de acuerdo al contexto del problema. 

Sustente todas sus preguntas con base en un mínimo de 100 réplicas, mediante intervalos de confianza.

Nota:
La simulación es desde el punto de vista del sistema
Los procesos de Poisson significan que los tiempos entre arribos se distribuyen exponencialmente
Para los abandonos: con los datos dados, para cada cliente, cuando entra al sistema, se le genera
una tolerancia en tiempo (usando una distribución exponencial con media dada), y en cada evento (avance
del reloj) se revisa si dicho umbral máximo de espera ya se cumplió y, por lo tanto, abandonaría la cola.
Ejemplo. Un cliente entra en el reloj en 15seg, se le genera un tiempo máximo de espera, por decir 10 seg,
es decir que cuando el reloj llegue a 25, si el cliente todavía está en la cola, el cliente abandona.
'''


# 1. Diagrama explicativo del e-commerce

# El e-commerce se compone de 4 posibles estados:

# Diagrama explicativo del e-commerce
# Cliente -> Llegada de clientes -> Selección de productos -> [ Abandono, Carrito de compra -> [Pago, Abandono] -> Salida de clientes ]
# Tenemos 2 colas: Cola de selección y Cola de pago por lo que haremos dos simulaciones y luego al final una simulación general

# Importamos las librerias necesarias para solo seleccionar los productos
import random
import math
def poisson(lam):
    L = math.exp(-lam)
    p = 1.0
    k = 0
    while p > L:
        k = k + 1
        u = random.random()
        p = p * u
    return k - 1



# funcion que busca un numero de poisson menor al proporcionado
def limit_poisson(lam, limit):
    while True:
        num = poisson(lam)
        if num < limit:
            return num
# Definimos las variables necesarias
tiempo_simulacion = 60  # minutos # llegan aproximadamente 100 clientes
tiempo_transcurrido = 0  # minutos
clientes_llegados = 0

# Variables para el seguimiento de clientes en las colas de selección y pago
cola_seleccion = []  # Almacena el tiempo de entrada de los clientes en la cola de selección
cola_pago = []  # Almacena el tiempo de entrada de los clientes en la cola de pago
tiempo_promedio_seleccion = 0  # Almacena el tiempo promedio en la cola de selección
tiempo_promedio_pago = 0  # Almacena el tiempo promedio en la cola de pago

clientes_llegados = 0  # Almacena el total de clientes que llegan al sistema
clientes_seleccionados = 0  # Almacena el total de clientes que seleccionan productos
clientes_abandonan_seleccion = 0  # Almacena el total de clientes que abandonan la cola de selección
# Variables para el seguimiento de clientes en la cola de pago
tiempo_promedio_pago = 0  # Almacena el tiempo promedio en la cola de pago
clientes_pagados = 0  # Almacena el total de clientes que completaron el pago
clientes_abandonan_pago = 0  # Almacena el total de clientes que abandonan la cola de pago

ti_pago = []  # Almacena el tiempo de llegada y salida de los clientes en la cola de pago

        
clientes_tiempos = []  # Almacena el numero de clientes que llegan en cada minuto y saca los clientes que pasan al siguiente estado o que llevan mas de 15 minutos en la cola de seleccion
clientes_sacados_por_tiempo = 0  # Almacena el numero de clientes que se sacan por tiempo de la cola de seleccion


# tabla de tiempo de clientes que avanzan de la seleccion al pago
ti_seleccion = [] # [[tiempo de llegada, tiempo de salida], [tiempo de llegada, tiempo de salida], ...]
while tiempo_transcurrido < tiempo_simulacion:
    # Llegada de clientes 10 clientes por minuto
    ingresos = poisson(10) # clientes que llegan en el minuto actual
    clientes_tiempos.append(ingresos) # se agrega el numero de clientes que llegan en el minuto actual a una lista para luego eliminarlos cuando pasen al siguiente estado, pago o abandono, o cuando lleven mas de 15 minutos en la cola de seleccion
    clientes_llegados += ingresos
    
    # Seleccion de productos 5 clientes por minuto, no deben ser mas de los que estan en la cola de seleccion
    clientes_con_productos_seleccionados = limit_poisson(5, clientes_llegados)
    clientes_seleccionados += clientes_con_productos_seleccionados
    
    # Abandono 2 clientes por minuto, no deben ser mas de los que estan en la cola de seleccion
    # sumatoria de clientes_tiempos
    total_clientes_acumulados = 0
    for i in range(len(clientes_tiempos)):
        total_clientes_acumulados += clientes_tiempos[i]
        
    # clientes que abandonan la cola de seleccion
    clientes_abandonan_seleccion_ahora = limit_poisson(2, total_clientes_acumulados - clientes_con_productos_seleccionados)
    clientes_abandonan_seleccion +=  clientes_abandonan_seleccion_ahora
        
    # Eliminar los clientes que pasan al siguiente estado o que se van por abandono
    aux = clientes_abandonan_seleccion_ahora + clientes_con_productos_seleccionados
    for i in range(len(clientes_tiempos)):
        tiempo_desde_llegada = tiempo_transcurrido - i
        # Reccorrer la lista desde el principio al final para eliminar los clientes que pasan al siguiente estado o que se van por abandono
        while clientes_tiempos[i] > 0:
            clientes_tiempos[i] -= 1
            aux -= 1
            if aux == 0:
                break
        if aux == 0:
            # calcular el tiempo promedio de los clientes que estan en la cola de seleccion y pasan al siguiente estado solo los que van para el estado de pago
            for i in range (clientes_con_productos_seleccionados):
                ti_seleccion.append([tiempo_desde_llegada, tiempo_transcurrido])
            break
        
    
    # Pago 7 clientes por minuto, no deben ser más de los que están en la cola de selección
    clientes_a_pagar = limit_poisson(7, clientes_con_productos_seleccionados)
    clientes_pagados += clientes_a_pagar

    # Abandono en la cola de pago
    clientes_abandonan_pago_ahora = limit_poisson(2, clientes_con_productos_seleccionados - clientes_a_pagar)
    clientes_abandonan_pago += clientes_abandonan_pago_ahora

    # Eliminar los clientes que pasan al siguiente estado (pago) o que se van por abandono en la cola de pago
    aux_pago = clientes_abandonan_pago_ahora + clientes_a_pagar
    for i in range(len(ti_seleccion)):
        tiempo_desde_llegada = tiempo_transcurrido - ti_seleccion[i][1]
        while ti_seleccion[i][1] > 0:
            ti_seleccion[i][1] -= 1
            aux_pago -= 1
            if aux_pago == 0:
                break
        if aux_pago == 0:
            for _ in range(clientes_a_pagar):
                ti_pago.append([ti_seleccion[i][1], tiempo_transcurrido])
            break
        
    # eliminar los clientes que llevan 15 minutos en la cola, sesabe porque el indice de la lista clientes_tiempos es igual al minuto en el que llegaron y si la diferencia entre el tiempo transcurrido y el indice es mayor a 15 se elimina
    for i in range(len(clientes_tiempos)):
        if tiempo_transcurrido - i > 15:
            clientes_sacados_por_tiempo += clientes_tiempos[i]
            clientes_tiempos[i] = 0
    
    tiempo_transcurrido += 1
    

# Calculamos el tiempo promedio en la cola de seleccion
tiempo_promedio_seleccion = 0
for i in range(len(ti_seleccion)):
    tiempo_promedio_seleccion += ti_seleccion[i][1] - ti_seleccion[i][0]
tiempo_promedio_seleccion /= len(ti_seleccion)

# Imprimimos los resultados
print("Tiempo promedio en la cola de seleccion: ", tiempo_promedio_seleccion)

# imprimir los resultados
print("Numero de clientes que llegaron: ", clientes_llegados)
print("Numero de clientes que seleccionaron productos: ", clientes_seleccionados)
print("Numero de clientes que abandonaron por propia voluntad: ", clientes_abandonan_seleccion)
print("Numero de clientes que se sacaron por tiempo: ", clientes_sacados_por_tiempo)



# Calculamos el tiempo promedio en la cola de pago
tiempo_promedio_pago = 0
for i in range(len(ti_pago)):
    tiempo_promedio_pago += ti_pago[i][1] - ti_pago[i][0]
tiempo_promedio_pago /= len(ti_pago)


# Imprimimos los resultados
print("Tiempo promedio en la cola de selección: ", tiempo_promedio_seleccion)
print("Tiempo promedio en la cola de pago: ", tiempo_promedio_pago)
print("Número de clientes que llegaron: ", clientes_llegados)
print("Número de clientes que seleccionaron productos: ", clientes_seleccionados)
print("Número de clientes que abandonaron la cola de selección: ", clientes_abandonan_seleccion)
print("Número de clientes que abandonaron la cola de pago: ", clientes_abandonan_pago)
print("Número de clientes que completaron el pago: ", clientes_pagados)
    

# Estrategias para reducir el tiempo de espera y la tasa de abandono
"""
Logramos identificar un problema en el que los clientes que llegan al sistema y se van por abandono y por tiempo ya que la plataforma no puede procesar carritos en ams de 5 clientes por minuto, si aumentaramos esta cantidad podriamos reducir el tiempo de espera y la tasa de abandono.
"""