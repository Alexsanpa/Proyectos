'''
El código suministrado leerá en un diccionario que contiene pares clave/valor de nombre:[marcas]
para una lista de estudiantes. Imprima el promedio de la matriz de marcas para el nombre del 
estudiante proporcionado, mostrando 2 lugares después del decimal.
Ejemplo
marcas Key:value pairs are
'alpha':[30,20,40]
'beta':[30,50,70]
query_name = 'beta'

'''
# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()

student_marks = {'alpha':[30,20,40], 'beta':[30,50,70]}
resultado = sum(student_marks['beta'])/3
print(f'{ resultado:.2f}')