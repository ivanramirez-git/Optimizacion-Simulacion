# Clase 3: Como funciona simplex

## Ejericio 2

Ejemplo 2:
Una empresa fabrica 2 tipos de producto, a partir de una materia prima. Los productos se venden a granel. Se
cuenta con una cantidad especifica de materia prima en el inventario y se quiere maximizar el ingreso de la
empresa, entendiendo que esta dado por el precio de cada producto y la cantidad de kilos que se venda de
cada uno
Los productos se fabrican en la misma maquina y ésta tiene una capacidad máxima de 300 kilos de producto
terminado.
La cantidad de materia prima que hay en el inventario es 800 kilos

| Producto | Cantidad requerida por materia prima por kilo de producto terminado | Precio por kilo | Cantidad minima de kilos a producir |
|----------|---------------------------------------------------------------------|-----------------|-------------------------------------|
| A        | 1.3                                                                 | $ 3700          | 68                                  |
| B        | 3.1                                                                 | $ 4000          | 80                                  |

Conjuntos:
• producto
Parámetros:
• Precio
• CapacidadMaquina
• InventarioMax
• CantidadMinima
• CantidadRequerida
Función objetivo:
Maximizar: Cantidad * precio

Variables:
X: cantidad de kilos de cada tipo de producto
Restricciones:

1. El consumo de materia prima debe ser inferior o igual a la cantidad de materia prima que esta disponible
2. La cantidad de producto fabricado debe ser inferior a la cantidad de producto que puede hacer la maquina
3. La cantidad de producto que se fabrique debe ser superior a la cantidad que se solicita

### Modelo matemático

Max 3700A + 4000B

Sujeto a:

1.3A + 3.1B <= 800
A + B <= 300
A >= 68
B >= 80
A, B >= 0

## Como funciona simplex

$
3700A + 4000B + S1                   = 800
$

$
    A +     B +    S2                = 300
$

$
    A -               E3    + R3     = 68
$

$
            B -          E4 +    R4  = 80
$

Variables Basicas:

$S1, S2, E3, E4, R3, R4$

Donde las R toman el valor de la cantidad minima de kilos a producir

Variables No Basicas:
A, B

Funcion objetivo:
$
3700A + 4000B + 0S1 + 0S2 + 0E3 + 0E4 - 1000R3 - 1000R4
$

$
3700A + 4000B - 68000 - 80000 = 3700A + 4000B - 148000
$

$
3700A + 4000B - 148000
$