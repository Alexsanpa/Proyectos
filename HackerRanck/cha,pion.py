'''
Teniendo en cuenta la hoja de resultados de los participantes para el Día de los Deportes de la Universidad, 
se requiere que encuentre la puntuación del subcampeón. Se le dan las puntuaciones n . Guárdelos en una lista y
encuentre la puntuación del subcampeón.
Formato de entrada

La primera línea contiene 'n'. La segunda línea contiene una matriz A[] de enteros 'n' cada uno separado por un espacio.
limitaciones
2 <= n <= 10
-100 <= A[i] <= 100

aclaración
Dada la lista es .[2,3,6,6,5] La puntuación máxima es 6, segundo máximo es 5. Por lo tanto, imprimimos como la puntuación subcampeona.
'''
# n son la cantidad de jugadores que estan participando
# A[i], son los core de cada uno de los jugadores
n=0
while 2 <= n <=10:
    n = int(input())
    arr = map(int, input().split())
    n_arr = list(set(arr))
    n_arr.sort()
    print(n_arr[-2])
else:
    False
