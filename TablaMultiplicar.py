#Tabla de multiplicar

print("|Bienvenido a el generador de tablas de multiplicar|")

numero=int(input("Digite el numero de la tabla de multiplicar ➙ "))

for i in range(1, 11, 1):
  print(f"{numero} X {i} = {numero*i} ")

