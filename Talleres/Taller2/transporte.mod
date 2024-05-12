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





