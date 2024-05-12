# Taller 3 - Vendedor de periódicos
Entregar en grupos a mas tardar el domingo 21 de abril a las 8 am

Realice la simulación del vendedor de periódicos utilizando los siguientes parámetros:
La cantidad de personas que llega al establecimiento se distribuye normal con media 150 y desviación 18 los días lunes y los días martes lo hace con media 130 y desviación 10. El vendedor abre tanto lunes, como martes sin ningún tipo de distinción (uniforme) y solo abre esos días.
La cantidad de periódicos que compra cada persona se distribuye triangular (mínimo=1, máximo=10, moda=7) 
El kiosko vende los dos periódicos nacionales. El 70% de la demanda la hace el periódico 1 y el otro 30% el periódico 2. A continuación se presenta la informacion de compra y venta de los dos periódicos:

|                   | Periódico 1 | Periódico 2 |
|-------------------|-------------|-------------|
| Costo adquisición | 2100        | 2600        |
| Costo faltante    | 400         | 500         |
| Ingreso sobrante  | 130         | 130         |
| Ingreso venta     | 3500        | 4500        |


El vendedor tiene un acuerdo con el propietario del establecimiento (el vendedor paga arriendo diariamente) de manera que cuando vende en total menos de 400 periódicos al día, debe pagarle $180.000 de arriendo y cuando vende más de 480 debe pagarle $250.000. De lo contrario paga la tarifa de siempre que es $200.000.
La cantidad Q que decida comprar el vendedor corresponde siempre a la suma de la cantidad del periódico 1 y la suma de la cantidad del periódico 2 y las dos sumas deben ser iguales. Por ejemplo, si compra 300 periódicos, la mitad es de periódico 1 y la otra mitad de periódico 2.

Otros datos de la simulación son:
* Error para la media=$10.000
* Error para la proporción=0.2
* Nivel de confianza=0.95  
* Muestra piloto=30
* Días de simulación=60
* Min=550
* Max=750

Preguntas:
1.	Calcule el intervalo de confianza para la utilidad promedio y concluya cuanto debe ser el Q recomendado
2.	Calcule el intervalo de confianza para la proporción de días en los que el vendedor vende más de $250.000

## Recomendaciones:

1.	Utilice la siguiente fórmula para la generación de números aleatorios de manera triangular:

$$ X = \begin{cases} a + \sqrt{U(b-a)(c-a)} & \text{for } 0 < U < F(c) \\ b - \sqrt{(1-U)(b-a)(b-c)} & \text{for } F(c) \leq U < 1 \end{cases} $$

Donde:
X es un número aleatorio distribuido de manera triangular
U es un numero aleatorio entre 0 y 1.


$$ F(c) = \frac{c-a}{b-a} $$
$$ a = \text{mínimo} $$
$$ b = \text{máximo} $$
$$ c = \text{moda} $$

2.	El intervalo para la proporción es:

$$ P(\hat{P} - Z_{\alpha/2} \sqrt{\frac{\hat{P}\hat{q}}{n}} < p < \hat{P} + Z_{\alpha/2} \sqrt{\frac{\hat{P}\hat{q}}{n}}) \approx 1-\alpha $$

Donde:
$\hat{P} = \frac{x}{n}$ siendo x la cantidad de éxitos y n la muestra
$\hat{q}$ es el complemento de $\hat{P}$
La fórmula para el tamaño de la muestra es igual a la del parámetro media


