import numpy as np
import random
import time

file=open ("Tiempos.txt",'w')

#TIEMPO EN QUE SE DEMORAR EN EJECUTAR EL CODIGO GUARDADO EN UN ARCHIVO .TXT
#TIEMPO MATRIZ 10*10
inicio1=time.time()
matriz1=np.random.randint(9, size=(10,10))
matriz2=np.random.randint(9, size=(10,10))
matriz_mult1=np.dot(matriz1,matriz2)
file.write('El tiempo de la primera multiplicacion es: '+str((time.time()-inicio1)*100)+"\n")

#TIEMPO MATRIZ 100*100
inicio2=time.time()
matriz3=np.random.randint(9, size=(100,100))
matriz4=np.random.randint(9, size=(100,100))
matriz_mult2=np.dot(matriz3,matriz4)
file.write('El tiempo de la segunda multiplicacion es: '+str((time.time()-inicio2)*100)+"\n")

#TIEMPO MATRIZ 1000*1000
inicio3=time.time()
matriz5=np.random.randint(9, size=(1000,1000))
matriz6=np.random.randint(9, size=(1000,1000))
matriz_mult3=np.dot(matriz5,matriz6)
file.write('El tiempo de la tercera multiplicacion es: '+str((time.time()-inicio3)*100)+"\n")

file.close()
