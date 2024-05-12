# Ivan - Camilo - Javier
# Taller 3 - Optimización y Simulación
# Taller 3 - Vendedor de periódicos

# Entregar en grupos a mas tardar el domingo 21 de abril a las 8 am

# Realice la simulación del vendedor de periódicos utilizando los siguientes parámetros:
# La cantidad de personas que llega al establecimiento se distribuye normal con media 150 y desviación 18 los días lunes y los días martes lo hace con media 130 y desviación 10. El vendedor abre tanto lunes, como martes sin ningún tipo de distinción (uniforme) y solo abre esos días.
# La cantidad de periódicos que compra cada persona se distribuye triangular (mínimo=1, máximo=10, moda=7) 
# El kiosko vende los dos periódicos nacionales. El 70% de la demanda la hace el periódico 1 y el otro 30% el periódico 2. A continuación se presenta la informacion de compra y venta de los dos periódicos:

# |                   | Periódico 1 | Periódico 2 |
# |-------------------|-------------|-------------|
# | Costo adquisición | 2100        | 2600        |
# | Costo faltante    | 400         | 500         |
# | Ingreso sobrante  | 130         | 130         |
# | Ingreso venta     | 3500        | 4500        |


# El vendedor tiene un acuerdo con el propietario del establecimiento (el vendedor paga arriendo diariamente) de manera que cuando vende en total menos de 400 periódicos al día, debe pagarle $180.000 de arriendo y cuando vende más de 480 debe pagarle $250.000. De lo contrario paga la tarifa de siempre que es $200.000.
# La cantidad Q que decida comprar el vendedor corresponde siempre a la suma de la cantidad del periódico 1 y la suma de la cantidad del periódico 2 y las dos sumas deben ser iguales. Por ejemplo, si compra 300 periódicos, la mitad es de periódico 1 y la otra mitad de periódico 2.

# Otros datos de la simulación son:
# * Error para la media=$10.000
# * Error para la proporción=0.2
# * Nivel de confianza=0.95  
# * Muestra piloto=30
# * Días de simulación=60
# * Min=550
# * Max=750

# Preguntas:
# 1.	Calcule el intervalo de confianza para la utilidad promedio y concluya cuanto debe ser el Q recomendado
# 2.	Calcule el intervalo de confianza para la proporción de días en los que el vendedor vende más de $250.000

# ## Recomendaciones:

# 1.	Utilice la siguiente fórmula para la generación de números aleatorios de manera triangular:

# $$ X = \begin{cases} a + \sqrt{U(b-a)(c-a)} & \text{for } 0 < U < F(c) \\ b - \sqrt{(1-U)(b-a)(b-c)} & \text{for } F(c) \leq U < 1 \end{cases} $$

# Donde:
# X es un número aleatorio distribuido de manera triangular
# U es un numero aleatorio entre 0 y 1.


# $$ F(c) = \frac{c-a}{b-a} $$
# $$ a = \text{mínimo} $$
# $$ b = \text{máximo} $$
# $$ c = \text{moda} $$

# 2.	El intervalo para la proporción es:

# $$ P(\hat{P} - Z_{\alpha/2} \sqrt{\frac{\hat{P}\hat{q}}{n}} < p < \hat{P} + Z_{\alpha/2} \sqrt{\frac{\hat{P}\hat{q}}{n}}) \approx 1-\alpha $$

# Donde:
# $\hat{P} = \frac{x}{n}$ siendo x la cantidad de éxitos y n la muestra
# $\hat{q}$ es el complemento de $\hat{P}$
# La fórmula para el tamaño de la muestra es igual a la del parámetro media



import random
import math

# Definir los parámetros
dias = {
    'lunes': {
        'media': 150,
        'desviacion': 18
    },
    'martes': {
        'media': 130,
        'desviacion': 10
    }
}

periodicos = {
    'tipo1': {
        'costo_adquisicion': 2100,
        'costo_faltante': 400,
        'ingreso_sobrante': 130,
        'ingreso_venta': 3500
    },
    'tipo2': {
        'costo_adquisicion': 2600,
        'costo_faltante': 500,
        'ingreso_sobrante': 130,
        'ingreso_venta': 4500
    }
}

arriendo = {
    'bajo': 180000,
    'alto': 250000,
    'normal': 200000
}

parametros = {
    'error_media': 10000,
    'error_proporcion': 0.2,
    'confianza': 0.95,
    'muestra_piloto': 30,
    'dias_simulacion': 60,
    'min': 550,
    'max': 750
}

# Generar los números aleatorios
def numero_aleatorio(min_val, max_val):
    return random.uniform(min_val, max_val)

def aleatorio_triangular(min_val, max_val, moda):
    a = min_val
    b = max_val
    c = moda
    u = random.random()
    f = (c - a) / (b - a)

    if u < f:
        return a + math.sqrt(u * (b - a) * (c - a))
    else:
        return b - math.sqrt((1 - u) * (b - a) * (b - c))

def distribucion_normal(media, desviacion):
    u = random.random()
    v = random.random()
    while u == 0:
        u = random.random()
    while v == 0:
        v = random.random()
    z = math.sqrt(-2.0 * math.log(u)) * math.cos(2.0 * math.pi * v)
    return media + z * desviacion

class SimulationData:
    def __init__(self, numero_simulacion=0):
        self.dias = [Dia(i, numero_simulacion) for i in range(parametros['dias_simulacion'])]

class TipoDia:
    lunes = 0
    martes = 1

class Dia:
    def __init__(self, numero_dia=0, numero_simulacion=0):
        self.numero_simulacion = numero_simulacion
        self.numero_dia = numero_dia
        self.tipo_dia = TipoDia.lunes if self.numero_dia % 2 == 0 else TipoDia.martes

        # Simular las personas que llegan al establecimiento
        self.personas = [Persona() for _ in range(round(distribucion_normal(dias['lunes']['media'], dias['lunes']['desviacion'])) if self.tipo_dia == TipoDia.lunes else round(distribucion_normal(dias['martes']['media'], dias['martes']['desviacion'])))]

        # Periodicos adquiridos
        periodicos_adquiridos = round(numero_aleatorio(parametros['min'] / 2, parametros['max'] / 2))
        self.periodicos_adquiridos_tipo1 = periodicos_adquiridos
        self.periodicos_adquiridos_tipo2 = periodicos_adquiridos

        # Periodicos totales intencion de compra
        self.total_intencion_de_compra_periodico_tipo1 = sum(persona.dato_compra.periodico1 for persona in self.personas)
        self.total_intencion_de_compra_periodico_tipo2 = sum(persona.dato_compra.periodico2 for persona in self.personas)

        # Periodicos faltantes si es negativo es 0
        self.periodicos_faltantes_tipo1 = max(self.total_intencion_de_compra_periodico_tipo1 - self.periodicos_adquiridos_tipo1, 0)
        self.periodicos_faltantes_tipo2 = max(self.total_intencion_de_compra_periodico_tipo2 - self.periodicos_adquiridos_tipo2, 0)

        # Periodicos sobrantes si faltante es > 0 no hay sobrante
        self.periodicos_sobrantes_tipo1 = max(self.periodicos_adquiridos_tipo1 - self.total_intencion_de_compra_periodico_tipo1, 0)
        self.periodicos_sobrantes_tipo2 = max(self.periodicos_adquiridos_tipo2 - self.total_intencion_de_compra_periodico_tipo2, 0)

        # Periodicos vendidos
        self.periodicos_vendidos_tipo1 = self.total_intencion_de_compra_periodico_tipo1 - self.periodicos_faltantes_tipo1
        self.periodicos_vendidos_tipo2 = self.total_intencion_de_compra_periodico_tipo2 - self.periodicos_faltantes_tipo2

        # Calcular el arriendo
        costo_adquisicion = self.periodicos_adquiridos_tipo1 * periodicos['tipo1']['costo_adquisicion'] + self.periodicos_adquiridos_tipo2 * periodicos['tipo2']['costo_adquisicion']
        costo_faltante = self.periodicos_faltantes_tipo1 * periodicos['tipo1']['costo_faltante'] + self.periodicos_faltantes_tipo2 * periodicos['tipo2']['costo_faltante']
        ingreso_sobrante = self.periodicos_sobrantes_tipo1 * periodicos['tipo1']['ingreso_sobrante'] + self.periodicos_sobrantes_tipo2 * periodicos['tipo2']['ingreso_sobrante']
        ingreso_venta = self.periodicos_vendidos_tipo1 * periodicos['tipo1']['ingreso_venta'] + self.periodicos_vendidos_tipo2 * periodicos['tipo2']['ingreso_venta']

        # Calcular el arriendo
        if self.periodicos_vendidos_tipo1 + self.periodicos_vendidos_tipo2 < 400:
            self.arriendo_dia = arriendo['bajo']
        elif self.periodicos_vendidos_tipo1 + self.periodicos_vendidos_tipo2 > 480:
            self.arriendo_dia = arriendo['alto']
        else:
            self.arriendo_dia = arriendo['normal']

        # Calcular la utilidad
        self.utilidad_dia = ingreso_venta - costo_adquisicion - costo_faltante + ingreso_sobrante - self.arriendo_dia

    # calcular el numero de periodicos que pidieron de cada tipo
    def imprimir_resumen_del_dia(self):
        print('---------------------------------------------')
        print('Simulación:', self.numero_simulacion)
        print('Día:', self.numero_dia + 1)
        print('Tipo de día:', 'Lunes' if self.tipo_dia == TipoDia.lunes else 'Martes')
        print('Total de personas:', len(self.personas))
        print('Total de periodicos adquiridos:', self.periodicos_adquiridos_tipo1 + self.periodicos_adquiridos_tipo2)

        print('Tipo 1:')
        print('Periódicos adquiridos:', self.periodicos_adquiridos_tipo1)
        print('Total de intención de compra:', self.total_intencion_de_compra_periodico_tipo1)
        print('Periódicos faltantes:', self.periodicos_faltantes_tipo1)
        print('Periódicos sobrantes:', self.periodicos_sobrantes_tipo1)
        print('Periódicos vendidos:', self.periodicos_vendidos_tipo1)
        print('Costo adquisición:', self.periodicos_adquiridos_tipo1 * periodicos['tipo1']['costo_adquisicion'])
        print('Costo faltante:', self.periodicos_faltantes_tipo1 * periodicos['tipo1']['costo_faltante'])
        print('Ingreso sobrante:', self.periodicos_sobrantes_tipo1 * periodicos['tipo1']['ingreso_sobrante'])
        print('Ingreso venta:', self.periodicos_vendidos_tipo1 * periodicos['tipo1']['ingreso_venta'])

        print('Tipo 2:')
        print('Periódicos adquiridos:', self.periodicos_adquiridos_tipo2)
        print('Total de intención de compra:', self.total_intencion_de_compra_periodico_tipo2)
        print('Periódicos faltantes:', self.periodicos_faltantes_tipo2)
        print('Periódicos sobrantes:', self.periodicos_sobrantes_tipo2)
        print('Periódicos vendidos:', self.periodicos_vendidos_tipo2)
        print('Costo adquisición:', self.periodicos_adquiridos_tipo2 * periodicos['tipo2']['costo_adquisicion'])
        print('Costo faltante:', self.periodicos_faltantes_tipo2 * periodicos['tipo2']['costo_faltante'])
        print('Ingreso sobrante:', self.periodicos_sobrantes_tipo2 * periodicos['tipo2']['ingreso_sobrante'])
        print('Ingreso venta:', self.periodicos_vendidos_tipo2 * periodicos['tipo2']['ingreso_venta'])

        print('Arriendo:', self.arriendo_dia)
        print('Utilidad:', self.utilidad_dia)
        print('---------------------------------------------')

class Persona:
    def __init__(self):
        self.dato_compra = DatoCompraPeriodico()

class DatoCompraPeriodico:
    def __init__(self):
        self.total = round(aleatorio_triangular(1, 10, 7))
        self.periodico1 = round(self.total * 0.7)
        self.periodico2 = round(self.total * 0.3)

        # debe ser discreto
        if self.periodico1 + self.periodico2 != self.total:
            self.periodico1 += self.total - (self.periodico1 + self.periodico2)

# Simulaciones para la muestra piloto
simulaciones_datos_muestra_piloto = [SimulationData(i) for i in range(parametros['muestra_piloto'])]

# Imprimir el resumen del top 5 dias con mayor utilidad de la muestra piloto
todos_los_dias_muestra_piloto = [dia for simulacion in simulaciones_datos_muestra_piloto for dia in simulacion.dias]
top5_dias_muestra_piloto = sorted(todos_los_dias_muestra_piloto, key=lambda dia: dia.utilidad_dia, reverse=True)[:5]
print('Top 5 días con mayor utilidad de la muestra piloto')
for dia in top5_dias_muestra_piloto:
    dia.imprimir_resumen_del_dia()

# Calcular la utilidad promedio
utilidades = [dia.utilidad_dia for dia in todos_los_dias_muestra_piloto]
media_utilidades = round(sum(utilidades) / len(utilidades))
error_media = parametros['error_media']
z = 1.96  # 95% de confianza
intervalo_confianza_utilidad = z * (error_media / math.sqrt(len(utilidades)))
print('Utilidad promedio:', media_utilidades)
print('Intervalo de confianza para la utilidad promedio:', (media_utilidades - intervalo_confianza_utilidad), '-', (media_utilidades + intervalo_confianza_utilidad))

# Calcular el Q recomendado
dias_con_q_recomendado = [dia for dia in todos_los_dias_muestra_piloto if dia.utilidad_dia > media_utilidades]
total_periodicos_adquiridos = sum(dia.periodicos_adquiridos_tipo1 + dia.periodicos_adquiridos_tipo2 for dia in dias_con_q_recomendado)
q_recomendado = total_periodicos_adquiridos / len(dias_con_q_recomendado)
print('Q recomendado:', q_recomendado)

# Calcular la proporción de días en los que el vendedor vende más de $250.000
dias_mayor_250000 = [dia for dia in todos_los_dias_muestra_piloto if dia.utilidad_dia > 250000]
proporcion_dias_mayor_250000 = len(dias_mayor_250000) / len(todos_los_dias_muestra_piloto)
error_proporcion = parametros['error_proporcion']
intervalo_confianza_proporcion = z * math.sqrt((proporcion_dias_mayor_250000 * (1 - proporcion_dias_mayor_250000)) / len(todos_los_dias_muestra_piloto))
print('Proporción de días en los que el vendedor vende más de $250.000:', proporcion_dias_mayor_250000)
print('Intervalo de confianza para la proporción de días en los que el vendedor vende más de $250.000:', (proporcion_dias_mayor_250000 - intervalo_confianza_proporcion), '-', (proporcion_dias_mayor_250000 + intervalo_confianza_proporcion))
