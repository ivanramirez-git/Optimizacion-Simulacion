<!-- 
Ejemplo glpk

```glpk
/* ASSIGN, Assignment Problem */

/* Written in GNU MathProg by Andrew Makhorin <mao@gnu.org> */

/* The assignment problem is one of the fundamental combinatorial
   optimization problems.
   In its most general form, the problem is as follows:
   There are a number of agents and a number of tasks. Any agent can be
   assigned to perform any task, incurring some cost that may vary
   depending on the agent-task assignment. It is required to perform all
   tasks by assigning exactly one agent to each task in such a way that
   the total cost of the assignment is minimized.
   (From Wikipedia, the free encyclopedia.) */

param m, integer, > 0;
/* number of agents */

param n, integer, > 0;
/* number of tasks */

set I := 1..m;
/* set of agents */

set J := 1..n;
/* set of tasks */

param c{i in I, j in J}, >= 0;
/* cost of allocating task j to agent i */

var x{i in I, j in J}, >= 0;
/* x[i,j] = 1 means task j is assigned to agent i
   note that variables x[i,j] are binary, however, there is no need to
   declare them so due to the totally unimodular constraint matrix */

s.t. phi{i in I}: sum{j in J} x[i,j] <= 1;
/* each agent can perform at most one task */

s.t. psi{j in J}: sum{i in I} x[i,j] = 1;
/* each task must be assigned exactly to one agent */

minimize obj: sum{i in I, j in J} c[i,j] * x[i,j];
/* the objective is to find a cheapest assignment */

solve;

printf "\n";
printf "Agent  Task       Cost\n";
printf{i in I} "%5d %5d %10g\n", i, sum{j in J} j * x[i,j],
   sum{j in J} c[i,j] * x[i,j];
printf "----------------------\n";
printf "     Total: %10g\n", sum{i in I, j in J} c[i,j] * x[i,j];
printf "\n";

data;

/* These data correspond to an example from [Christofides]. */

/* Optimal solution is 76 */

param m := 8;

param n := 8;

param c : 1  2  3  4  5  6  7  8 :=
      1  13 21 20 12  8 26 22 11
      2  12 36 25 41 40 11  4  8
      3  35 32 13 36 26 21 13 37
      4  34 54  7  8 12 22 11 40
      5  21  6 45 18 24 34 12 48
      6  42 19 39 15 14 16 28 46
      7  16 34 38  3 34 40 22 24
      8  26 20  5 17 45 31 37 43 ;

end;


/* TODD, a class of hard instances of zero-one knapsack problems */

/* Written in GNU MathProg by Andrew Makhorin <mao@gnu.org> */

/* Chvatal describes a class of instances of zero-one knapsack problems
   due to Todd. He shows that a wide class of algorithms - including all
   based on branch and bound or dynamic programming - find it difficult
   to solve problems in the Todd class. More exactly, the time required
   by these algorithms to solve instances of problems that belong to the
   Todd class grows as an exponential function of the problem size.

   Reference:
   Chvatal V. (1980), Hard knapsack problems, Op. Res. 28, 1402-1411. */

param n > 0 integer;

param log2_n := log(n) / log(2);

param k := floor(log2_n);

param a{j in 1..n} := 2 ** (k + n + 1) + 2 ** (k + n + 1 - j) + 1;

param b := 0.5 * floor(sum{j in 1..n} a[j]);

var x{1..n} binary;

maximize obj: sum{j in 1..n} a[j] * x[j];

s.t. cap: sum{j in 1..n} a[j] * x[j] <= b;

data;

param n := 15;
/* change this parameter to choose a particular instance */

end;

/* Any Wolfram elementary CA in 6D eucl. Neumann CA grid emulator generator */

/* Implemented, inspected, written and converted to GNU MathProg
   by NASZVADI, Peter, 2016-2017 <vuk@cs.elte.hu> */

/* see background info and more details in wolfra6d.lp */

/* each axis has this two endpoints */
set V := 0..1;

/* this model processes a hypercube in 6d, so 6+1 parallel planes intersect  */
set H := 0..6;

/* denoting all vertices in the 6d unit hypercube */
set Cells := V cross V cross V cross V cross V cross V;


/* input parameters, bup/bdn = number of upper/lower neighbour 6d cells of a (cyclic) segment */
param bup{i in H}, default 1;
param bdn{i in H}, default 2;

/* boolean meaning if a vertex is chosen */
var x{Cells}, binary;

/* temporary calculations to enforce bup/bdn */
var up{Cells}, >=0;
var dn{Cells}, >=0;

/* the total weight of selected cells near the main diagonal */
var obj;

/* up/dn vars denote the number of selected upper/lower neighbours */
s.t. cup{(v1,v2,v3,v4,v5,v6) in Cells: v1+v2+v3+v4+v5+v6<6}:
    sum{(w1,w2,w3,w4,w5,w6) in Cells: max(v1-w1,v2-w2,v3-w3,v4-w4,v5-w5,v6-w6)<=0}
        if (w1+w2+w3+w4+w5+w6) = (1+v1+v2+v3+v4+v5+v6) then x[w1,w2,w3,w4,w5,w6] else 0 =
        up[v1,v2,v3,v4,v5,v6];

s.t. cdn{(v1,v2,v3,v4,v5,v6) in Cells: v1+v2+v3+v4+v5+v6>0}:
    sum{(w1,w2,w3,w4,w5,w6) in Cells: min(v1-w1,v2-w2,v3-w3,v4-w4,v5-w5,v6-w6)>=0}
        if (w1+w2+w3+w4+w5+w6) = (-1+v1+v2+v3+v4+v5+v6) then x[w1,w2,w3,w4,w5,w6] else 0 =
        dn[v1,v2,v3,v4,v5,v6];

/* 4 helper constraints, hences the leading "c" */
s.t. cbup1{(v1,v2,v3,v4,v5,v6) in Cells: v1+v2+v3+v4+v5+v6<6}:
    up[v1,v2,v3,v4,v5,v6] >= bup[v1+v2+v3+v4+v5+v6] * x[v1,v2,v3,v4,v5,v6];

s.t. cbup2{(v1,v2,v3,v4,v5,v6) in Cells: v1+v2+v3+v4+v5+v6<6}:
    up[v1,v2,v3,v4,v5,v6] + (2**6) * x[v1,v2,v3,v4,v5,v6] <= (2**6) + bup[v1+v2+v3+v4+v5+v6];

s.t. cbdn1{(v1,v2,v3,v4,v5,v6) in Cells: v1+v2+v3+v4+v5+v6>0}:
    dn[v1,v2,v3,v4,v5,v6] >= bdn[v1+v2+v3+v4+v5+v6] * x[v1,v2,v3,v4,v5,v6];

s.t. cbdn2{(v1,v2,v3,v4,v5,v6) in Cells: v1+v2+v3+v4+v5+v6>0}:
    dn[v1,v2,v3,v4,v5,v6] + (2**6) * x[v1,v2,v3,v4,v5,v6] <= (2**6) + bdn[v1+v2+v3+v4+v5+v6];

/* these two promoted points should be selected */
s.t. initdiag: x[0,0,0,0,0,0] + x[1,1,1,1,1,1] = 2;

/* obvious */
s.t. sumx: sum{(v1,v2,v3,v4,v5,v6) in Cells} x[v1,v2,v3,v4,v5,v6] = obj;

minimize cobj: obj;

solve;

/* pretty-printing hopefully nontrivial solution */
printf "\nChosen vertex subset:\n";
for{i in H}: {
    printf "Weight=%s\n", i;
    printf{(v1,v2,v3,v4,v5,v6) in Cells: v1+v2+v3+v4+v5+v6 = i+(8-8*x[v1,v2,v3,v4,v5,v6])}
        " %s%s%s%s%s%s\n",v1,v2,v3,v4,v5,v6;
}
printf "\nTotal number of selected cells in the hypercube: %g\n\n", obj;

data;

/* these parameters were chosen in the first run that yielded a solution */
param bup := 0 6
             1 2
             2 3
             3 2
             4 1
             5 1
             6 6;

param bdn := 0 3
             1 1
             2 2
             3 1
             4 4
             5 3
             6 3;

end;
``` 
 -->

# TALLER 1 OPTIMIZACION Y SIMULACION 

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


### SOLUCIÓN

#### MODELO MATEMÁTICO


##### Función Objetivo

Minimizar el costo total de transporte

$$\text{Min} Z = \sum_{i=1}^{5}\sum_{j=1}^{10} C_{ij}X_{ij}$$

##### Restricciones

1. La capacidad de los nodos fuente debe ser igual a la demanda de los nodos sumidero

$$\sum_{j=1}^{10} X_{ij} = D_i \quad \forall i \in \{1,2,3,4,5\}$$

$$\sum_{i=1}^{5} X_{ij} = O_j \quad \forall j \in \{1,2,3,4,5,6,7,8,9,10\}$$

2. Las unidades despachadas por el nodo O1, más las del nodo O5, deben ser el doble de las despachadas por el nodo O2 más el nodo O4.

$$X_{11} + X_{15} = 2(X_{21} + X_{24})$$

3. El nodo D4 debe ser atendido por el nodo O3, con al menos 10 unidades, pero no exclusivamente, puede ser atendido por otros nodos también.

$$X_{34} \geq 10$$

4. El nodo D8 debe ser atendido por el nodo O4, con al menos 15 unidades, pero no exclusivamente, puede ser atendido por otros nodos también.

$$X_{48} \geq 15$$

5. El nodo O3 debe dar suministro al menos a un nodo tipo D, con no menos de 200 unidades en total para todos los nodos

$$\sum_{i=1}^{5} X_{3j} \geq 200 \quad \forall j \in \{1,2,3,4,5,6,7,8,9,10\}$$

6. La suma de lo que entregan los 3 primeros nodo tipo O (O1,O2,O3) debe ser al menos 550 unidades

$$\sum_{j=1}^{10} X_{1j} + \sum_{j=1}^{10} X_{2j} + \sum_{j=1}^{10} X_{3j} \geq 550$$

7. La demanda debe cumplirse

$$X_{ij} \geq 0 \quad \forall i \in \{1,2,3,4,5\} \quad \forall j \in \{1,2,3,4,5,6,7,8,9,10\}$$

8. La capacidad no puede sobrepasarse

$$X_{ij} \leq O_j \quad \forall i \in \{1,2,3,4,5\} \quad \forall j \in \{1,2,3,4,5,6,7,8,9,10\}$$

##### GUSEK

```glpk
/* TRANSPORTE */

param m := 5; /* número de nodos fuente */
param n := 10; /* número de nodos sumidero */

/* Costos de transporte */
param c :=
1 1 2 3 4 5 6 7 8 9 10 :=
1 120 80 85 75 94 85 98 105 125 135
2 110 0 85 78 92 104 110 112 130 85
3 90 0 0 74 88 0 55 78 80 0
4 78 117 60 64 0 78 69 77 74 78
5 65 47 78 75 44 122 71 45 68 88;

/* Oferta y demanda */
param supply := 1 450 2 110 3 210 4 120 5 250;
param demand := 1 85 2 95 3 110 4 70 5 60 6 75 7 90 8 95 9 100 10 120;

/* Resuelve el problema de transporte */
minimize costo_transporte: sum{i in 1..m, j in 1..n} c[i,j] * x[i,j];
subject to oferta{i in 1..m}: sum{j in 1..n} x[i,j] = supply[i];
subject to demanda{j in 1..n}: sum{i in 1..m} x[i,j] = demand[j];
solve;
display x;

end;

```


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

### SOLUCIÓN

#### MODELO MATEMÁTICO

##### Función Objetivo

Maximizar el puntaje total de los clientes

$$\text{Max} Z = \sum_{i=1}^{7}\sum_{j=1}^{12} P_{ij}X_{ij}$$

##### Restricciones

1. Cada arquitecto puede trabajar en máximo 3 proyectos.

$$\sum_{j=1}^{12} X_{ij} \leq 3 \quad \forall i \in \{1,2,3,4,5,6,7\}$$

2. Cada proyecto debe ser atendido por la cantidad de arquitectos requeridos.

$$\sum_{i=1}^{7} X_{ij} = P_j \quad \forall j \in \{1,2,3,4,5,6,7,8,9,10,11,12\}$$

3. Los arquitectos solo pueden trabajar en los proyectos que han sido clasificados con 1.

$$X_{ij} \leq 1 \quad \forall i \in \{1,2,3,4,5,6,7\} \quad \forall j \in \{1,2,3,4,5,6,7,8,9,10,11,12\}$$

4. La demanda debe cumplirse

$$X_{ij} \geq 0 \quad \forall i \in \{1,2,3,4,5,6,7\} \quad \forall j \in \{1,2,3,4,5,6,7,8,9,10,11,12\}$$

##### GUSEK

```glpk
/* ASIGNACION */

param m := 7; /* número de arquitectos */
param n := 12; /* número de proyectos */

/* Puntajes de los clientes */
param P :=
1 1 2 3 4 5 6 7 8 9 10 11 12 :=
1 4 5 4 3 4 3 2 3 4 5 3 2
2 3 2 3 2 3 5 5 5 5 2 2 2
3 5 5 3 3 3 3 4 4 4 5 5 5
4 1 1 1 1 2 2 2 2 2 4 4 4
5 3 3 3 3 4 2 2 2 2 3 3 3
6 5 5 5 5 5 5 5 5 4 4 4 4
7 4 4 4 4 4 4 4 4 4 4 2 2;

/* Requerimientos de cada proyecto */
param P_j :=
1 1
2 2
3 1
4 1
5 1
6 1
7 1
8 1
9 1
10 2
11 1
12 1;

/* Resuelve el problema de asignación */
maximize puntaje_total: sum{i in 1..m, j in 1..n} P[i,j] * x[i,j];
subject to max_proyectos{i in 1..m}: sum{j in 1..n} x[i,j] <= 3;
subject to req_proyectos{j in 1..n}: sum{i in 1..m} x[i,j] = P_j[j];
subject to only_assigned{i in 1..m, j in 1..n}: x[i,j] <= 1;
solve;
display x;
    
end;

```
