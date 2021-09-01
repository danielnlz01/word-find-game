import random
import string

sopa_de_letras=[[]]

tamanio_sopa_de_letras=30

palabras_archivo=open("PalabrasSopaDeLetras.txt","r")

palabras=[]
for palabra in palabras_archivo:
  palabra_string=palabra.replace("\n","")
  palabra_list=palabra_string.split(";")
  palabras.append(palabra_list)
  
print(palabras)

palabra=random.choice(palabras)

print(palabra)


def llenar_matriz_sopa_de_letras():
  for i in range(tamanio_sopa_de_letras):
    sopa_de_letras_fila=[]
    for j in range(tamanio_sopa_de_letras):
      sopa_de_letras_fila.append(random.choice(string.ascii_letters))
    sopa_de_letras.append(sopa_de_letras_fila)

def pintar_sopa_de_letras():
  for i in range(len(sopa_de_letras)):
    for j in range(len(sopa_de_letras[i])):
      print(sopa_de_letras[i][j],end=" ")
    print("")
    
def meter_palabra_horizontal(palabra):
  fila_aleatoria=random.randint(0,29)
  columna_aleatoria=random.randint(0,17)
  print(columna_aleatoria)
  print(fila_aleatoria)
  for i in range(len(palabra)):
    sopa_de_letras[fila_aleatoria][columna_aleatoria+i]=palabra[i]

def meter_palabra_vertical (palabra):
  fila_aleatoria=random.randint(0,17)
  columna_aleatoria=random.randint(0,29)
  print(columna_aleatoria)
  print(fila_aleatoria)
  for i in range(len(palabra)):
    sopa_de_letras[fila_aleatoria+i][columna_aleatoria]=palabra[i]

def meter_palabra_diagonal (palabra):
  fila_aleatoria=random.randint(0,17)
  columna_aleatoria=random.randint(0,17)
  print(columna_aleatoria)
  print(fila_aleatoria)
  for i in range(len(palabra)):
    sopa_de_letras[fila_aleatoria+i][columna_aleatoria+i]=palabra[i]

llenar_matriz_sopa_de_letras()
opcion_acomodo=random.randint(0,3)
if opcion_acomodo==0:
  meter_palabra_horizontal(palabra[1])
  print("Horizontal")
elif opcion_acomodo==1:
  meter_palabra_vertical(palabra[1])
  print("Vertical")
else:
  meter_palabra_diagonal(palabra[1])
  print("Diagonal")
pintar_sopa_de_letras()

print(palabra[0])
respuesta=input()
if respuesta==palabra[1]:
  print("Ya ganaste")
else:
  print("perdiste")

