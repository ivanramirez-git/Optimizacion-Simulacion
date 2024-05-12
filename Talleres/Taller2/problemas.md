# Ejericio 1
```glpk
set Origen:= 1..2;
set Clientes:= 1..4;


param Costo { i in Origen, j in Clientes };
param Capacidad { i in Origen };
param Demanda { j in Clientes };

var x { i in Origen, j in Clientes } >= 0;

minimize FuncionObjetivo: sum{ i in Origen, j in Clientes } x[i,j] * Costo[i,j];

s.t. RestriccionDeOferta { i in Origen }: sum{ j in Clientes } x[i,j] <= Capacidad [i];
s.t. RestriccionDemanda { j in Clientes }: sum{ i in Origen } x[i,j] >= Demanda [j];
s.t. RestriccionDeServidorCliente { i in Origen, j in Clientes : i=1 and j=1 }: x[i,j] = 0;

data; 
param Costo: 1 2 3 4:= 
			1 25 35 22 40
			2 34 44 54 15;

param Capacidad:= 
			   1 168
			   2 168;

param Demanda:= 1 70
				  2 70
				  3 20
				  4 30;
```

## Summary
### Status	OPTIMAL
#### Objective	5720
#### Direction	MINIMIZATION
#### Number of Rows	8
#### Number of Columns	8
#### Non-zero elements	25
#### Number of integer variables	0
#### Number of binary variables	0


# Ejercicio 2

```glpk
set Marca:= 1..5;

param PrecioVenta { precio in Marca };
param ValorMiseria { precio in Marca };

var miseria { precio in Marca } binary;
var cantidadDeVehiculos { precio in Marca } integer >= 0;

maximize FuncionObjetivo: sum { precio in Marca } miseria[precio]*ValorMiseria[precio] + sum { precio in Marca } cantidadDeVehiculos[precio]*PrecioVenta[precio];

s.t. vendedorVendeAyC { precioA in Marca, precioC in Marca : precioA = 1 and precioC = 3 }: miseria[precioA] <= miseria[precioC];
s.t. cantidadBesElDobleDeE { precioB in Marca, precioE in Marca : precioB = 2 and precioE = 5 }: cantidadDeVehiculos[precioB] >= 2*cantidadDeVehiculos[precioE];
s.t. siBvendeDvende { precioB in Marca, precioD in Marca : precioB = 2 and precioD = 4 }: miseria[precioB] <= miseria[precioD];
s.t. alMenosTresDeA { precioA in Marca : precioA = 1 }: cantidadDeVehiculos[precioA] >= 3;
s.t. soloDiezDeB { precioB in Marca : precioB = 2 }: cantidadDeVehiculos[precioB] <= 10;
s.t. AMasCEsMenorA15 { precioA in Marca, precioC in Marca : precioA = 1 and precioC = 3 }: cantidadDeVehiculos[precioA]+cantidadDeVehiculos[precioC] <= 14;
s.t. DMasEEsMenorA20 { precioD in Marca, precioE in Marca : precioD = 4 and precioE = 5 }: cantidadDeVehiculos[precioD]+cantidadDeVehiculos[precioE] <= 19;
  
data;
param PrecioVenta:=
1 100 
2 80
3 75
4 65 
5 45;

param ValorMiseria:=
1 5
2 8
3 11
4 14 
5 12;
```

## Summary
### Status	OPTIMAL
#### Objective	3485
#### Direction	MAXIMIZATION
#### Number of Rows	8
#### Number of Columns	10
#### Non-zero elements	22
#### Number of integer variables	10
#### Number of binary variables	5

# Ejercicio 3

## TRANSPORTE: 

Una empresa cuenta con una red que tiene los siguientes costos unitarios (si no hay costo, no hay conexión entre los nodos) 

|         | Nodo D1 | Nodo D2 | Nodo D3 | Nodo D4 | Nodo D5 | Nodo D6 | Nodo D7 | Nodo D8 | Nodo D9 | Nodo D10 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | -------- |
| Nodo O1 | 120     | 80      | 85      | 75      | 94      | 85      | 98      | 105     | 125     | 135      |
| Nodo O2 | 110     |         | 85      | 78      | 92      | 104     | 110     | 112     | 130     | 85       |
| Nodo O3 | 90      |         |         | 74      | 88      |         | 55      | 78      | 80      |          |
| Nodo O4 | 78      | 117     | 60      | 64      |         | 78      | 69      | 77      | 74      | 78       |
| Nodo O5 | 65      | 47      | 78      | 75      | 44      | 122     | 71      | 45      | 68      | 88       |
 

Los nodos fuente tienen la siguiente capacidad: 

| Nodo    | Demanda (unidades) |
| ------- | ------------------ |
| Nodo O1 | 450                |
| Nodo O2 | 110                |
| Nodo O3 | 210                |
| Nodo O4 | 120                |
| Nodo O5 | 250                |
 

Los nodos sumidero requieren las siguientes unidades: 
| Nodo     | Demanda (unidades) |
| -------- | ------------------ |
| Nodo D1  | 85                 |
| Nodo D2  | 95                 |
| Nodo D3  | 110                |
| Nodo D4  | 70                 |
| Nodo D5  | 60                 |
| Nodo D6  | 75                 |
| Nodo D7  | 90                 |
| Nodo D8  | 95                 |
| Nodo D9  | 100                |
| Nodo D10 | 120                |
 
### RESTRICCIONES:

Realice un modelo matemático y soluciónelo en Gusek, de manera que obtenga el menor costo de la operación, teniendo en cuenta las restricciones siguientes: 

1. Las unidades despachadas por el nodo O1, más las del nodo O5, deben ser el doble de las despachadas por el nodo O2 más el nodo O4. 

2. El nodo D4 debe ser atendido por el nodo O3, con al menos 10 unidades, pero no exclusivamente, puede ser atendido por otros nodos también. 

3. El nodo D8 debe ser atendido por el nodo O4, con al menos 15 unidades, pero no exclusivamente, puede ser atendido por otros nodos también. 

4. El nodo O3 debe dar suministro al menos a un nodo tipo D, con no menos de 200 unidades en total para todos los nodos 

5. La suma de lo que entregan los 3 primeros nodo tipo O (O1,O2,O3) debe ser al menos 550 unidades 

6. La demanda debe cumplirse 

7. La capacidad no puede sobrepasarse 



```glpk

set fuentes:=1..5;
set sumidero:=1..10;

param costo{f in fuentes, s in sumidero};
param capacidad{f in fuentes};
param demanda{s in sumidero};

var x{f in fuentes,s in sumidero}integer>=0;

minimize z:sum{f in fuentes,s in sumidero}x[f,s]*costo[f,s];

s.t.capacidad_r{f in fuentes}: sum{s in sumidero}x[f,s]<=capacidad[f];
s.t.demanda_r{s in sumidero}: sum{f in fuentes}x[f,s]>=demanda[s];
s.t.uno_r:sum{s in sumidero}x[1,s]+sum{s in sumidero}x[5,s]=2*(sum{s in sumidero}x[2,s]+sum{s in sumidero}x[4,s]);
s.t.dos_r:x[3,4]>=10;
s.t.dos_r2:x[4,8]>=15;
s.t.dos_r3:sum{s in sumidero}x[3,s]>=200;
s.t.dos_r4:sum{s in sumidero,f in fuentes:f<4}x[f,s]>=550;

data;

param costo:1 2 3 4 5 6 7 8 9 10:=
1	120	80	85	75	94	85	98	105	125	135
2	110	100000	85	78	92	104	110	112	130	85
3	90	100000	100000	74	88	100000	55	78	80	100000
4	78	117	60	64	100000	78	69	77	74	78
5	65	47	78	75	44	122	71	45	68	88;

param capacidad:=
1	450
2	110
3	210
4	120
5	250;


param demanda:=
1	85
2	95
3	110
4	70
5	60
6	75
7	90
8	95
9	100
10	120;

```
## Summary
### Status	OPTIMAL
#### Objective	61945
#### Direction	MINIMIZATION
#### Number of Rows	21
#### Number of Columns	50
#### Non-zero elements	232
#### Number of integer variables	50
#### Number of binary variables	0


# Ejercicio 4


## ASIGNACION 

Deben asignarse ciertos arquitectos (7) a ciertos proyectos (12). Las condiciones para la asignación son: 

Cada cliente prefiere trabajar con ciertos arquitectos y han manifestado por medio de puntajes (de 1 a 5), la preferencia por cada uno de ellos, para sus proyectos: 

| Arq\Proy | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1        | 4   | 5   | 4   | 3   | 4   | 3   | 2   | 3   | 4   | 5   | 3   | 2   |
| 2        | 3   | 2   | 3   | 2   | 3   | 5   | 5   | 5   | 5   | 2   | 2   | 2   |
| 3        | 5   | 5   | 3   | 3   | 3   | 3   | 4   | 4   | 4   | 5   | 5   | 5   |
| 4        | 1   | 1   | 1   | 1   | 2   | 2   | 2   | 2   | 2   | 4   | 4   | 4   |
| 5        | 3   | 3   | 3   | 3   | 4   | 2   | 2   | 2   | 2   | 3   | 3   | 3   |
| 6        | 5   | 5   | 5   | 5   | 5   | 5   | 5   | 5   | 4   | 4   | 4   | 4   |
| 7        | 4   | 4   | 4   | 4   | 4   | 4   | 4   | 4   | 4   | 4   | 2   | 2   |


Adicionalmente, de acuerdo con la experiencia y estudios de cada arquitecto, los funcionarios solo pueden trabajar en los proyectos que han sido clasificados con 1: 

| Arq\Proj | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1        | 1   | 0   | 0   | 0   | 0   | 1   | 0   | 0   | 1   | 0   | 0   | 1   |
| 2        | 0   | 0   | 1   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 1   | 0   |
| 3        | 1   | 0   | 0   | 1   | 1   | 0   | 1   | 1   | 0   | 1   | 0   | 1   |
| 4        | 0   | 0   | 1   | 1   | 1   | 0   | 1   | 1   | 0   | 1   | 1   | 0   |
| 5        | 0   | 1   | 0   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 1   | 1   |
| 6        | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 0   | 1   | 0   | 0   | 1   |
| 7        | 1   | 1   | 1   | 1   | 0   | 0   | 1   | 0   | 1   | 1   | 1   | 0   |


La cantidad de arquitectos que se requiere para cada proyecto es: 

| 1   | 1   |
| --- | --- |
| 2   | 2   |
| 3   | 1   |
| 4   | 1   |
| 5   | 1   |
| 6   | 1   |
| 7   | 1   |
| 8   | 1   |
| 9   | 1   |
| 10  | 2   |
| 11  | 1   |
| 12  | 1   |


Cada arquitecto puede trabajar en máximo 3 proyectos. 

Realice un modelo matemático y soluciónelo en Gusek. Tenga en cuenta que las restricciones deben ser cumplidas y la función objetivo debe establecerse en términos de maximización de las preferencias de los clientes. (alcanzar el mayor puntaje total (sumado) de todos los clientes) 

```glpk
set arquitectos:=1..7;
set proyectos:=1..12;

param preferencias{a in arquitectos, p in proyectos};
param disponibilidad{a in arquitectos, p in proyectos};
param requerimientos{p in proyectos};

var x{a in arquitectos, p in proyectos}binary;

maximize z:sum{a in arquitectos, p in proyectos}x[a,p]*preferencias[a,p];

s.t.r1{a in arquitectos,p in proyectos}:x[a,p]<=disponibilidad[a,p];
s.t.r2{a in arquitectos}:sum{p in proyectos}x[a,p]<=3;
s.t.r3{p in proyectos}:sum{a in arquitectos}x[a,p]=requerimientos[p];

data;

param disponibilidad:1 2 3 4 5 6 7 8 9 10 11 12:=
1	1	0	0	0	0	1	0	0	1	0	0	1
2	0	0	1	1	0	1	0	1	1	0	1	1
3	1	0	0	1	1	0	0	1	0	1	0	1
4	0	0	1	1	1	0	1	1	0	1	1	0
5	0	1	0	0	0	0	1	0	1	0	1	1
6	1	1	0	0	1	1	1	0	1	0	0	1
7	1	1	1	1	0	0	1	0	1	1	1	0
;

param preferencias:1 2 3 4 5 6 7 8 9 10 11 12:=
1	4	5	4	3	4	3	2	3	4	5	3	2
2	3	2	3	2	3	5	5	5	5	2	2	2
3	5	5	3	3	3	3	4	4	4	5	5	5
4	1	1	1	1	2	2	2	2	2	4	4	4
5	3	3	3	3	4	2	2	2	2	3	3	3
6	5	5	5	5	5	5	5	5	4	4	4	4
7	4	4	4	4	4	4	4	4	4	4	2	2
;

param requerimientos:=
1	1
2	2
3	1
4	1
5	1
6	1
7	1
8	1
9	1
10	2
11	1
12	1
;
```

## Summary
### Status	OPTIMAL
#### Objective	65
#### Direction	MAXIMIZATION
#### Number of Rows	104
#### Number of Columns	84
#### Non-zero elements	336
#### Number of integer variables	84
#### Number of binary variables	84


# Ejercicio 5

```glpk
set estudiantes:= 1..6;
set grupos:= 1..5;
 
 
param matri{j in grupos, i in estudiantes};
 
 
var x{j in grupos} binary;
 
maximize fo: sum {j in grupos} x[j];
 
s.t. restri1{i in estudiantes}:sum{j in grupos}matri[j,i]*x[j]<=1;
 
data;
 
param matri: 1 2 3 4 5 6:=
           1 1 1 0 0 0 0
           2 1 0 1 0 0 0
           3 0 1 0 1 0 0
           4 0 0 1 0 1 0
           5 0 0 1 1 0 1;
```

## Summary
### Status	OPTIMAL
#### Objective	2
#### Direction	MAXIMIZATION
#### Number of Rows	7
#### Number of Columns	5
#### Non-zero elements	16
#### Number of integer variables	5
#### Number of binary variables	5


# Ejercicio 6

Se deben seleccionar, de una lista de contenedores, hasta 4 posibles tipos de contenedores (sin importar a qué proveedor se le compre) que deben ser enviados a diferentes puntos de venta (POS), ubicados a lo largo de la ciudad. Los costos asociados al envío de los contenedores varían de acuerdo con el recorrido que se debe realizar (desde los proveedores a los POS) y al tipo de contenedor. Cada contenedor tiene una capacidad máxima, la cual es usada para retirar el desecho de los puntos de venta, dado que de cada punto de venta debe ser evacuada cierta cantidad de toneladas, por medio de estos contenedores. 
Los datos son los siguientes: 
Toneladas que cada cliente va a desechar y para lo cual requiere los contenedores: (en los contenedores deposita el desecho)

|                      | Cliente 1 | Cliente 2 | Cliente 3 | Cliente 4 |
| -------------------- | --------- | --------- | --------- | --------- |
| Toneladas a desechar | 100       | 70        | 80        | 50        |

Los costos variables dependen de, el proveedor, el tipo de contenedor y el cliente al cual se le entrega dicho contenedor.
Costos variables (unitarios) de los contenedores desde los proveedores a los clientes:

| Provedor 1   | Cliente 1 | Cliente 2 | Cliente 3 | Cliente 4 |
| ------------ | --------- | --------- | --------- | --------- |
| Contenedor 1 | 70        | 80        | 50        | 60        |
| Contenedor 2 | 80        | 90        | 110       | 100       |
| Contenedor 3 | 110       | 140       | 130       | 120       |
| Contenedor 4 | 140       | 145       | 150       | 130       |
| Contenedor 5 | 155       | 145       | 155       | 150       |

| Provedor 2   | Cliente 1 | Cliente 2 | Cliente 3 | Cliente 4 |
| ------------ | --------- | --------- | --------- | --------- |
| Contenedor 1 | 82        | 92        | 62        | 42        |
| Contenedor 2 | 92        | 102       | 92        | 82        |
| Contenedor 3 | 122       | 152       | 112       | 102       |
| Contenedor 4 | 152       | 155       | 132       | 112       |
| Contenedor 5 | 160       | 157       | 135       | 130       |

| Provedor 3   | Cliente 1 | Cliente 2 | Cliente 3 | Cliente 4 |
| ------------ | --------- | --------- | --------- | --------- |
| Contenedor 1 | 102       | 113       | 84        | 74        |
| Contenedor 2 | 112       | 123       | 94        | 84        |
| Contenedor 3 | 142       | 173       | 114       | 115       |
| Contenedor 4 | 172       | 178       | 134       | 114       |
| Contenedor 5 | 187       | 178       | 139       | 134       |

Los costos, la capacidad y la cantidad de los contenedores son: (es igual para cada proveedor)

| Contenedor   | Costo por unidad | Capacidad en toneladas | Cantidad disponible de contenedores |
| ------------ | ---------------- | ---------------------- | ----------------------------------- |
| Contenedor 1 | $1200            | 12                     | 3                                   |
| Contenedor 2 | $1500            | 18                     | 4                                   |
| Contenedor 3 | $2000            | 20                     | 2                                   |
| Contenedor 4 | $2800            | 22                     | 2                                   |
| Contenedor 5 | $4000            | 30                     | 1                                   |

Adicionalmente, por cada proveedor con que se negocie, por abrir el proceso de contratación y estudio de crédito y demás, se incurre en un costo de $50.000. (si se le compra al proveedor, se paga, sino, no se paga)
Establezca un modelo que le permita definir cuantos contenedores, de qué tipo, a qué proveedor se le van a comprar y a qué cliente se le van a enviar. Minimice el costo total

Por favor tenga en cuenta que el parámetro correspondiente al costo variable debe ingresarse de la siguiente manera a Gusek:

```glpk
param costovariable{t in tipo, c in cliente, p in proveedor};
```

Y su data, de la siguiente manera:

```glpk
param costovariable[*,*,1]:
	1	2	3	4:=
1	70	80	50	60
2	80	90	110	100
3	110	140	130	120
4	140	145	150	130
5	155	145	155	150
[*,*,2]:
	1	2	3	4:=
1	82	92	62	42
2	92	102	92	82
3	122	152	112	102
4	152	155	132	112
5	160	157	135	130
[*,*,3]:
	1	2	3	4:=
1	102	113	84	74
2	112	123	94	84
3	142	173	114	115
4	172	178	134	114
5	187	178	139	134;
```


```glpk
set tipo:=1..5;
set cliente:=1..4;
set proveedor:=1..3;

param costovariable{t in tipo, c in cliente, p in proveedor};
param costocontenedor{t in tipo};
param capacidadcontenedor{t in tipo};
param cantidadcontenedor{t in tipo};
param costoproceso:=50000;

var x{t in tipo, c in cliente, p in proveedor} binary;
var y{p in proveedor} binary;

minimize z: sum{t in tipo, c in cliente, p in proveedor} x[t,c,p]*costovariable[t,c,p]+sum{p in proveedor} y[p]*costoproceso;

s.t. restri1{c in cliente}: sum{t in tipo, p in proveedor} x[t,c,p]=1;
s.t. restri2{t in tipo}: sum{c in cliente, p in proveedor} x[t,c,p]<=cantidadcontenedor[t];
s.t. restri3{c in cliente}: sum{t in tipo, p in proveedor} x[t,c,p]<=4;
s.t. restri4{p in proveedor}: sum{t in tipo, c in cliente} x[t,c,p]<=4*y[p];

data;

param costovariable[*,*,1]:
	1	2	3	4:=
1	70	80	50	60
2	80	90	110	100
3	110	140	130	120
4	140	145	150	130
5	155	145	155	150
[*,*,2]:
	1	2	3	4:=
1	82	92	62	42
2	92	102	92	82
3	122	152	112	102
4	152	155	132	112
5	160	157	135	130
[*,*,3]:
	1	2	3	4:=
1	102	113	84	74
2	112	123	94	84
3	142	173	114	115
4	172	178	134	114
5	187	178	139	134;

param costocontenedor:=
1	1200
2	1500
3	2000
4	2800
5	4000;

param capacidadcontenedor:=
1	12
2	18
3	20
4	22
5	30;

param cantidadcontenedor:=
1	3
2	4
3	2
4	2
5	1;


```



