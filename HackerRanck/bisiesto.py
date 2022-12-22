'''

Un día adicional se agrega al calendario casi cada cuatro años como el 29 de febrero,y el día se llama un día bisiesto. 
Corrige el calendario por el hecho de que nuestro planeta tarda aproximadamente 365,25 días en orbitar el sol.
Un año bisiesto contiene un día bisiesto. En el calendario gregoriano, se utilizan tres condiciones para identificar los años bisiestos:
El año puede ser dividido uniformemente por 4, es un año bisiesto,
a menos que: El año puede ser dividido uniformemente por 100, NO es un año bisiesto,
a menos que: El año también es divisible uniformemente por 400. Entonces es un año bisiesto.     
Esto significa que en el calendario gregoriano, los años 2000 y 2400 son años bisiestos, mientras que
1800, 1900, 2100, 2200, 2300 y 2500 NO son años bisiestos. Fuente
'''

no_bisiestos=[1800, 1900, 2100, 2200, 2300, 2500]
año = 1994
def bisisesto(año):
    if año not in no_bisiestos:
        if (año%400)%4 == 0:
            return f'Si es'
    return f'No es'

print(bisisesto(1990))












