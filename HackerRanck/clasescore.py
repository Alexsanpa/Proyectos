'''
Dado los nombres y calificaciones de cada estudiante en una clase  de N estudiantes,
guárdelos en una lista anidada e imprima el nombre(s) de cualquier estudiante(s) que tenga 
la segunda calificación más baja.

Nota: Si hay varios estudiantes con el segundo grado más bajo, ordene sus nombres alfabéticamente
e imprima cada nombre en una nueva línea.
example 
[["chi",20.0], ["Beta", 50.0],["alpha", 50.0]]
La lista ordenada de puntuaciones es [20.0,50.0] , por lo que la segunda puntuación más baja es 50.0. Hay dos estudiantes
con esa puntuación: ["Beta","alpha"]. Ordenados alfabéticamente, los nombres se imprimen como:

La primera línea contiene un entero, N, el número de estudiantes.
Las 2N líneas siguientes describen a cada estudiante sobre líneas.
- La primera línea contiene el nombre del estudiante.
- La segunda línea contiene su grado.

Limitaciones
2<=N<=5
Siempre habrá uno o más estudiantes con el segundo grado más bajo
'''
from decimal import Decimal
calificacion=[37.21,37.21,37.2,41,39]
estudiante=['Harry','Berry','Tina', 'akirity', 'harsh']


python_estudiantes={'Harry': 37.21, 'Berry':37.21, 'Tina': 45, 'Akirity': 37.2, 'Harsh':39}
ordenada =sorted(python_estudiantes.values())
ordenada= sorted(set(ordenada))

python_estudiantes = sorted(python_estudiantes.items())
python_estudiantes = dict(python_estudiantes)

for llave, Valor in python_estudiantes.items():

    if Valor == ordenada[1]:
        print(llave)
        


        











