#while ejercicio
print("Bienvenido a la tienda don pepito")
totalProducto, totalCompra = 0, 0

entrada = 1 
salida = 2

while (entrada != salida):
  nombre= input("Nombre del producto: ")
  precio= int(input("Precio del producto: "))
  cantidad= int(input("Cantidad del producto: "))

  totalProducto += cantidad
  totalCompra += (cantidad * precio)
  
  entrada= int(input("Desea continuar agregando productos? 1.Seguir | 2.Salir : "))

print(f"Total de la compra: {totalCompra}")
print(f"Total de productos comprados: {totalProducto}")