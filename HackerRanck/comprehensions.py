'''
¡Aprendamos sobre las comprensiones de la lista! Le dan tres números enteros X, Y y  Z que representan
las dimensiones de un cuboide junto con un número entero N.
Imprima una lista de todas las coordenadas posibles dadas por en una cuadrícula(I J K) 3D donde la suma d( i + j + k)
no es igual a N. Aquí, 0 < i x; 0<j<y; 0 < k < z. Por favor, utilice las comprensiones de la lista en lugar de múltiples 
bucles,como un ejercicio de aprendizaje.
'''

Largo_cuboide = 2
columna =[]
x=3
y=2
z=3
Largo_cuboide=abs(Largo_cuboide)
Largo_cuboide+=1
# for i in range(Largo_cuboide+1):
#     if i <= x:
#         for j in range(Largo_cuboide+1):
#             if j <= y:
#                 for k in range(Largo_cuboide+1):
#                     if k <= z:
#                         columna.append([i,j,k])
                
# print(columna)
                        

# array = [ [i,j,k] for i in range(0,Largo_cuboide)if i <= x  for j in range(0,Largo_cuboide)if j <= y for k in range(0,Largo_cuboide)if k <= z and i+k+j != Largo_cuboide]
# print(array)
array = [ [i,j,k] for i in range(x+1)if i <= x  for j in range(y+1)if j <= y for k in range(z+1)if  i+k+j != Largo_cuboide]
print(array)
      
