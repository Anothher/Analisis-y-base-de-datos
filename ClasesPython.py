#Variables


x=int(input("Porfavor digite un valor entero X: "));
operacion1=1/x
operacion2=x+operacion1
operacion3=x+1/operacion2
operacion4=x+1/operacion3
y=1/operacion4
print("Resultado es",y)


#variables


print("Para el genero Niño...")
xnBraga=int(input("Ingrese la cantidad soliciada del articulo Braga: "))
xnJean=int(input("Ingrese la cantidad soliciada del articulo Jean: "))
xnPantalon=int(input("Ingrese la cantidad soliciada del articulo Pantalon: "))

print("Para el genero Mujer...")
xmBraga=int(input("Ingrese la cantidad soliciada del articulo Braga: "))
xmJean=int(input("Ingrese la cantidad soliciada del articulo Jean: "))
xmPantalon=int(input("Ingrese la cantidad soliciada del articulo Pantalon: "))

print("Para el genero Hombre...")
xhBraga=int(input("Ingrese la cantidad soliciada del articulo Braga: "))
xhJean=int(input("Ingrese la cantidad soliciada del articulo Jean: "))
xhPantalon=int(input("Ingrese la cantidad soliciada del articulo Pantalon: "))
print("\n")
print("Total de cantidades pedidas del genero niño es:", xnBraga + xnJean + xnPantalon)
print("Total de cantidades pedidas del genero Mujer es:", xmBraga + xmJean + xmPantalon)
print("Total de cantidades pedidas del genero Hombre es:", xhBraga + xhJean + xhPantalon, "\n" )

print("Total de cantidades pedidas del Articulo Braga fue de:", xnBraga + xmBraga + xhBraga)
print("Total de cantidades pedidas del Articulo Jeans fue de:", xnJean + xmJean + xhJean)
print("Total de cantidades pedidas del Articulo Pantalon fue de:", xnPantalon + xmPantalon + xhPantalon)


#bucles


nombre= input("Cual es tu nombre? ")
print(f"Hola {nombre} bienvenido a el contador de numeros")
i= int(input("Digita el numero inicial: "))
o= int(input("De cuanto en cuanto quieres que sume? "))
u= int(input("Hasta que numero quieres sumar? "))

while i <= u:
  print(i)
  i += o
print("La suma total es: " )


#bucles 2 variable centinela


sw = 0
while(sw == 0):
  numero =int(input("Digite un numero "))
  if numero % 2 == 0:
    print(f"El numero {numero} es par")
  else:
    print("Lo siento, Digistaste un numero impar")
    sw = 1

