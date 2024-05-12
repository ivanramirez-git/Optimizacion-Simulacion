/*
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


*/

// Importar las librerías
import math from 'mathjs'; // npm install mathjs

// Definir los parámetros
const dias = {
    lunes: {
        media: 150,
        desviacion: 18
    },
    martes: {
        media: 130,
        desviacion: 10
    }
};

const periodicos = {
    tipo1: {
        costo_adquisicion: 2100,
        costo_faltante: 400,
        ingreso_sobrante: 130,
        ingreso_venta: 3500
    },
    tipo2: {
        costo_adquisicion: 2600,
        costo_faltante: 500,
        ingreso_sobrante: 130,
        ingreso_venta: 4500
    }
};

const arriendo = {
    bajo: 180000,
    alto: 250000,
    normal: 200000
};

const parametros = {
    error_media: 10000,
    error_proporcion: 0.2,
    confianza: 0.95,
    muestra_piloto: 30,
    dias_simulacion: 60,
    min: 550,
    max: 750
};

// Generar los números aleatorios
const numeroAleatorio = (min: number, max: number) => {
    return Math.random() * (max - min) + min;
};

const aleatorioTriangular = (min: number, max: number, moda: number) => {
    const a = min;
    const b = max;
    const c = moda;
    const u = Math.random();
    const f = (c - a) / (b - a);

    if (u < f) {
        return a + (Math.sqrt(u * (b - a) * (c - a)) as number);
    } else {
        return b - (Math.sqrt((1 - u) * (b - a) * (b - c)) as number);
    }
}

const distribucionNormal = (media: number, desviacion: number) => {
    let u = 0, v = 0;
    while (u === 0) u = Math.random();
    while (v === 0) v = Math.random();
    const z = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    return media + z * desviacion;

}

class SimulationData {
    public dias: Dia[];
    constructor(numeroSimulacion: number = 0) {
        this.dias = [];
        for (let i = 0; i < parametros.dias_simulacion; i++) {
            this.dias.push(new Dia(i, numeroSimulacion));
        }
    }
}

enum TipoDia { lunes, martes }
class Dia {
    public cantidadPersonas: number;
    public personas: Persona[];
    public numeroDia: number;
    public tipoDia: TipoDia;
    public numeroSimulacion: number;

    constructor(numeroDia: number = 0, numeroSimulacion: number = 0) {
        this.numeroSimulacion = numeroSimulacion;
        this.numeroDia = numeroDia;
        this.tipoDia = this.numeroDia % 2 === 0 ? TipoDia.lunes : TipoDia.martes;

        // Simular las personas que llegan al establecimiento
        this.personas = [];
        this.cantidadPersonas = Math.round(this.tipoDia === TipoDia.lunes ? distribucionNormal(dias.lunes.media, dias.lunes.desviacion) : distribucionNormal(dias.martes.media, dias.martes.desviacion));
        for (let i = 0; i < this.cantidadPersonas; i++) {
            this.personas.push(new Persona());
        }

        // Periodicos adquiridos
        const periodicosAdquiridos = Math.round(numeroAleatorio(parametros.min / 2, parametros.max / 2));
        this.periodicosAdquiridosTipo1 = periodicosAdquiridos;
        this.periodicosAdquiridosTipo2 = periodicosAdquiridos;

        // Periodicos totales intencion de compra
        this.totalIntencionDeCompraPeriodicoTipo1 = 0;
        this.totalIntencionDeCompraPeriodicoTipo2 = 0;
        for (let i = 0; i < this.personas.length; i++) {
            this.totalIntencionDeCompraPeriodicoTipo1 += this.personas[i].datoCompra.periodico1;
            this.totalIntencionDeCompraPeriodicoTipo2 += this.personas[i].datoCompra.periodico2;
        }

        // Periodicos faltantes si es negativo es 0
        this.periodicosFaltantesTipo1 = this.totalIntencionDeCompraPeriodicoTipo1 - this.periodicosAdquiridosTipo1 > 0 ? this.totalIntencionDeCompraPeriodicoTipo1 - this.periodicosAdquiridosTipo1 : 0;
        this.periodicosFaltantesTipo2 = this.totalIntencionDeCompraPeriodicoTipo2 - this.periodicosAdquiridosTipo2 > 0 ? this.totalIntencionDeCompraPeriodicoTipo2 - this.periodicosAdquiridosTipo2 : 0;

        // Periodicos sobrantes si faltante es > 0 no hay sobrante
        this.periodicosSobrantesTipo1 = this.periodicosFaltantesTipo1 > 0 ? 0 : this.periodicosAdquiridosTipo1 - this.totalIntencionDeCompraPeriodicoTipo1;
        this.periodicosSobrantesTipo2 = this.periodicosFaltantesTipo2 > 0 ? 0 : this.periodicosAdquiridosTipo2 - this.totalIntencionDeCompraPeriodicoTipo2;

        // Periodicos vendidos
        this.periodicosVendidosTipo1 = this.totalIntencionDeCompraPeriodicoTipo1 - this.periodicosFaltantesTipo1;
        this.periodicosVendidosTipo2 = this.totalIntencionDeCompraPeriodicoTipo2 - this.periodicosFaltantesTipo2;


        // Calcular el arriendo
        const costoAdquisicion = this.periodicosAdquiridosTipo1 * periodicos.tipo1.costo_adquisicion + this.periodicosAdquiridosTipo2 * periodicos.tipo2.costo_adquisicion;
        const costoFaltante = this.periodicosFaltantesTipo1 * periodicos.tipo1.costo_faltante + this.periodicosFaltantesTipo2 * periodicos.tipo2.costo_faltante;
        const ingresoSobrante = this.periodicosSobrantesTipo1 * periodicos.tipo1.ingreso_sobrante + this.periodicosSobrantesTipo2 * periodicos.tipo2.ingreso_sobrante;
        const ingresoVenta = this.periodicosVendidosTipo1 * periodicos.tipo1.ingreso_venta + this.periodicosVendidosTipo2 * periodicos.tipo2.ingreso_venta;

        // Calcular el arriendo
        this.arriendoDia = 0;
        if (this.periodicosVendidosTipo1 + this.periodicosVendidosTipo2 < 400) {
            this.arriendoDia = arriendo.bajo;
        } else if (this.periodicosVendidosTipo1 + this.periodicosVendidosTipo2 > 480) {
            this.arriendoDia = arriendo.alto;
        } else {
            this.arriendoDia = arriendo.normal;
        }

        // Calcular la utilidad
        this.utilidadDia = ingresoVenta - costoAdquisicion - costoFaltante + ingresoSobrante - this.arriendoDia;
    }

    public totalIntencionDeCompraPeriodicoTipo1: number;
    public totalIntencionDeCompraPeriodicoTipo2: number;

    public periodicosAdquiridosTipo1: number;
    public periodicosAdquiridosTipo2: number;

    public periodicosFaltantesTipo1: number;
    public periodicosFaltantesTipo2: number;

    public periodicosSobrantesTipo1: number;
    public periodicosSobrantesTipo2: number;

    public periodicosVendidosTipo1: number;
    public periodicosVendidosTipo2: number;

    public arriendoDia: number;
    public utilidadDia: number;

    // calcular el numero de periodicos que pidieron de cada tipo
    public imprimirResumenDelDia() {
        console.log('---------------------------------------------');
        console.log('Simulación: ' + this.numeroSimulacion);
        console.log('Día: ' + (this.numeroDia + 1));
        console.log('Tipo de día: ' + (this.tipoDia === TipoDia.lunes ? 'Lunes' : 'Martes'));
        console.log('Total de personas: ' + this.cantidadPersonas);
        console.log('Total de periodicos adquiridos: ' + (this.periodicosAdquiridosTipo1 + this.periodicosAdquiridosTipo2));

        console.table({
            'Tipo 1': {
                'Periódicos adquiridos': this.periodicosAdquiridosTipo1,
                'Total de intención de compra': this.totalIntencionDeCompraPeriodicoTipo1,
                'Periódicos faltantes': this.periodicosFaltantesTipo1,
                'Periódicos sobrantes': this.periodicosSobrantesTipo1,
                'Periódicos vendidos': this.periodicosVendidosTipo1,
                'Costo adquisición': this.periodicosAdquiridosTipo1 * periodicos.tipo1.costo_adquisicion,
                'Costo faltante': this.periodicosFaltantesTipo1 * periodicos.tipo1.costo_faltante,
                'Ingreso sobrante': this.periodicosSobrantesTipo1 * periodicos.tipo1.ingreso_sobrante,
                'Ingreso venta': this.periodicosVendidosTipo1 * periodicos.tipo1.ingreso_venta,
            },
            'Tipo 2': {
                'Periódicos adquiridos': this.periodicosAdquiridosTipo2,
                'Total de intención de compra': this.totalIntencionDeCompraPeriodicoTipo2,
                'Periódicos faltantes': this.periodicosFaltantesTipo2,
                'Periódicos sobrantes': this.periodicosSobrantesTipo2,
                'Periódicos vendidos': this.periodicosVendidosTipo2,
                'Costo adquisición': this.periodicosAdquiridosTipo2 * periodicos.tipo2.costo_adquisicion,
                'Costo faltante': this.periodicosFaltantesTipo2 * periodicos.tipo2.costo_faltante,
                'Ingreso sobrante': this.periodicosSobrantesTipo2 * periodicos.tipo2.ingreso_sobrante,
                'Ingreso venta': this.periodicosVendidosTipo2 * periodicos.tipo2.ingreso_venta,
            }
        });

        console.log('Arriendo: ' + this.arriendoDia);
        console.log('Utilidad: ' + this.utilidadDia);
        console.log('---------------------------------------------');
    }

}

class Persona {
    public datoCompra: DatoCompraPeriodico;
    constructor() {
        this.datoCompra = new DatoCompraPeriodico();
    }
}

class DatoCompraPeriodico {
    public total: number;
    public periodico1: number;
    public periodico2: number;
    constructor() {
        this.total = Math.round(aleatorioTriangular(1, 10, 7));
        this.periodico1 = this.total * 0.7;
        this.periodico2 = this.total * 0.3;

        // debe ser discreto
        this.periodico1 = Math.round(this.periodico1);
        this.periodico2 = Math.round(this.periodico2);

        // validar si la suma es igual al total
        if (this.periodico1 + this.periodico2 !== this.total) {
            this.periodico1 += this.total - (this.periodico1 + this.periodico2);
        }
    }
}

// Simulaciones para la muestra piloto
let simulacionesDatosMuestraPiloto: SimulationData[] = []
for (let i = 0; i < parametros.muestra_piloto; i++) {
    const simulationData = new SimulationData(i);
    simulacionesDatosMuestraPiloto.push(simulationData);

}


// // Imprimir el resumen del top 5 dias con mayor utilidad de la muestra piloto, como es una matriz se debe hacer un doble sort
const todosLosDiasMuestraPiloto = simulacionesDatosMuestraPiloto.map(simulationData => simulationData.dias).reduce((a, b) => a.concat(b), []);
const top5DiasMuestraPiloto = todosLosDiasMuestraPiloto.sort((a, b) => b.utilidadDia - a.utilidadDia).slice(0, 5);
console.log('Top 5 días con mayor utilidad de la muestra piloto');
for (let i = 0; i < top5DiasMuestraPiloto.length; i++) {
    top5DiasMuestraPiloto[i].imprimirResumenDelDia();
}



// 1.	Calcule el intervalo de confianza para la utilidad promedio y concluya cuanto debe ser el Q recomendado
// 2.	Calcule el intervalo de confianza para la proporción de días en los que el vendedor vende más de $250.000

// Calcular la utilidad promedio
const utilidades = todosLosDiasMuestraPiloto.map(dia => dia.utilidadDia);
const mediaUtilidades = Math.round(utilidades.reduce((a, b) => a + b, 0) / utilidades.length);
const errorMedia = parametros.error_media;
const z = 1.96; // 95% de confianza
const intervaloConfianzaUtilidad = z * (errorMedia / Math.sqrt(utilidades.length));
console.log('Utilidad promedio: ' + mediaUtilidades);
console.log('Intervalo de confianza para la utilidad promedio: ', (mediaUtilidades - intervaloConfianzaUtilidad) + ' - ' + (mediaUtilidades + intervaloConfianzaUtilidad));


// Calcular el Q recomendado
const diasConQRecomendado = todosLosDiasMuestraPiloto.filter(dia => dia.utilidadDia > mediaUtilidades);
const totalPeriodicosAdquiridos = diasConQRecomendado.map(dia => dia.periodicosAdquiridosTipo1 + dia.periodicosAdquiridosTipo2).reduce((a, b) => a + b, 0);
const qRecomendado = totalPeriodicosAdquiridos / diasConQRecomendado.length;
console.log('Q recomendado: ' + qRecomendado);


// Calcular la proporción de días en los que el vendedor vende más de $250.000
const diasMayor250000 = todosLosDiasMuestraPiloto.filter(dia => dia.utilidadDia > 250000);
const proporcionDiasMayor250000 = diasMayor250000.length / todosLosDiasMuestraPiloto.length;
const errorProporcion = parametros.error_proporcion;
const intervaloConfianzaProporcion = z * Math.sqrt((proporcionDiasMayor250000 * (1 - proporcionDiasMayor250000)) / todosLosDiasMuestraPiloto.length);
console.log('Proporción de días en los que el vendedor vende más de $250.000: ' + proporcionDiasMayor250000);
console.log('Intervalo de confianza para la proporción de días en los que el vendedor vende más de $250.000: ', (proporcionDiasMayor250000 - intervaloConfianzaProporcion) + ' - ' + (proporcionDiasMayor250000 + intervaloConfianzaProporcion));

