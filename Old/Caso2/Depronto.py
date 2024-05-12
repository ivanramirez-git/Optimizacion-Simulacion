
import random
import math
import statistics as stats

# Parámetros del sistema
tasa_llegada = 10  # Tasa de llegada de clientes por minuto
tasa_seleccion = 5  # Tasa de selección de productos por minuto
tasa_pago = 7  # Tasa de pago de compra por minuto
tasa_abandono = 2  # Tasa de abandono de clientes por minuto
tiempo_simulacion = 60  # Tiempo de simulación en minutos
num_replicas = 100  # Número de réplicas para el análisis

# Listas para almacenar resultados
tiempos_en_cola_seleccion = []
tiempos_en_cola_pago = []
tasa_llegada_efectiva = []

# Función para la distribución exponencial
def exponencial(tasa):
    return -math.log(1.0 - random.random()) / tasa

# Función para la simulación del sistema Monte Carlo
def simulacion():
    # Variables de estado
    estado = 0  # 0: llegada, 1: selección, 2: pago, 3: abandono
    tiempo = 0.0  # Tiempo de simulación
    tiempo_prox_llegada = exponencial(tasa_llegada)  # Tiempo para la próxima llegada
    tiempo_prox_seleccion = float('inf')  # Tiempo para la próxima selección
    tiempo_prox_pago = float('inf')  # Tiempo para el próximo pago
    tiempo_prox_abandono = float('inf')  # Tiempo para el próximo abandono
    tiempo_prox_evento = tiempo_prox_llegada  # Tiempo para el próximo evento
    tiempo_ultimo_evento = 0.0  # Tiempo del último evento
    tiempo_en_cola_seleccion = 0.0  # Tiempo en cola de selección
    tiempo_en_cola_pago = 0.0  # Tiempo en cola de pago
    cola_seleccion = 0  # Cola de selección
    cola_pago = 0  # Cola de pago
    clientes_abandonan = 0  # Clientes que abandonan el proceso

    # Simulación del sistema
    while tiempo < tiempo_simulacion:
        tiempo_ultimo_evento = tiempo
        tiempo = tiempo_prox_evento

        if tiempo_prox_llegada < tiempo_prox_seleccion and tiempo_prox_llegada < tiempo_prox_pago and tiempo_prox_llegada < tiempo_prox_abandono:
            # Llegada de un cliente
            tiempo_prox_llegada = tiempo + exponencial(tasa_llegada)
            if estado == 0:
                # El cliente pasa a la cola de selección
                estado = 1
                tiempo_prox_seleccion = tiempo + exponencial(tasa_seleccion)
            elif estado == 1:
                # El cliente pasa a la cola de selección
                cola_seleccion += 1
            elif estado == 2:
                # El cliente pasa a la cola de pago
                cola_pago += 1
            elif estado == 3:
                # El cliente pasa a la cola de selección
                cola_seleccion += 1
                clientes_abandonan += 1
            else:
                print('Error de estado')
        elif tiempo_prox_seleccion < tiempo_prox_pago and tiempo_prox_seleccion < tiempo_prox_abandono:
            # Selección de productos
            tiempo_en_cola_seleccion += (tiempo - tiempo_ultimo_evento) * cola_seleccion
            cola_seleccion -= 1
            if cola_seleccion > 0:
                tiempo_prox_seleccion = tiempo + exponencial(tasa_seleccion)
            else:
                tiempo_prox_seleccion = float('inf')
            if estado == 1:
                # El cliente pasa al proceso de pago
                estado = 2
                tiempo_prox_pago = tiempo + exponencial(tasa_pago)
            elif estado == 2:
                # El cliente pasa al proceso de pago
                cola_pago += 1
            elif estado == 3:
                # El cliente pasa al proceso de pago
                cola_pago += 1
                clientes_abandonan += 1
            else:
                print('Error de estado')
        elif tiempo_prox_pago < tiempo_prox_abandono:
            # Pago de compra
            tiempo_en_cola_pago += (tiempo - tiempo_ultimo_evento) * cola_pago
            cola_pago -= 1
            if cola_pago > 0:
                tiempo_prox_pago = tiempo + exponencial(tasa_pago)
            else:
                tiempo_prox_pago = float('inf')
            if estado == 2:
                # El cliente finaliza su compra
                estado = 0
            elif estado == 3:
                # El cliente finaliza su compra
                estado = 0
                clientes_abandonan -= 1
            else:
                print('Error de estado')
        else:
            # Abandono de cliente
            cola_seleccion -= 1
            if cola_seleccion > 0:
                tiempo_prox_abandono = tiempo + exponencial(tasa_abandono)
            else:
                tiempo_prox_abandono = float('inf')
            if estado == 1:
                # El cliente abandona el proceso
                estado = 3
            elif estado == 2:
                # El cliente abandona el proceso
                estado = 3
                clientes_abandonan += 1
            elif estado == 3:
                # El cliente abandona el proceso
                clientes_abandonan += 1
            else:
                print('Error de estado')
                
        # Actualización de la tasa de llegada efectiva
        if estado == 0:
            tasa_llegada_efectiva.append(1.0 / (tiempo - tiempo_ultimo_evento))
            
        # Actualización del tiempo para el próximo evento
        tiempo_prox_evento = min(tiempo_prox_llegada, tiempo_prox_seleccion, tiempo_prox_pago, tiempo_prox_abandono)
        
    # Actualización de los tiempos en cola
    tiempos_en_cola_seleccion.append(tiempo_en_cola_seleccion / tiempo)
    tiempos_en_cola_pago.append(tiempo_en_cola_pago / tiempo)
    
    # Actualización de los clientes que abandonan el proceso
    clientes_abandonan += cola_seleccion
    clientes_abandonan += cola_pago
    clientes_abandonan += 1 if estado == 1 else 0
    clientes_abandonan += 1 if estado == 2 else 0
    clientes_abandonan += 1 if estado == 3 else 0
    
    return clientes_abandonan

# Simulación del sistema
for i in range(num_replicas):
    simulacion()
    
# Resultados
print('Resultados de la simulación:')
print('Tiempo promedio en cola de selección:', stats.mean(tiempos_en_cola_seleccion))
print('Tiempo promedio en cola de pago:', stats.mean(tiempos_en_cola_pago))
print('Tasa efectiva de llegada de clientes:', stats.mean(tasa_llegada_efectiva))
print('Tasa de abandono de clientes:', tasa_abandono)
print('Tasa de abandono de clientes simulada:', stats.mean(tasa_llegada_efectiva) - tasa_seleccion - tasa_pago)
print('Clientes que abandonan el proceso:', stats.mean(tasa_llegada_efectiva) - tasa_seleccion - tasa_pago - tasa_abandono)
print('Clientes que abandonan el proceso simulado:', stats.mean(tasa_llegada_efectiva) - tasa_seleccion - tasa_pago - stats.mean(tasa_llegada_efectiva) + tasa_seleccion + tasa_pago)

# Intervalos de confianza
print('Intervalos de confianza:')
