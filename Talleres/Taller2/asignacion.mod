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


