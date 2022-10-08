
sueldobase =int(input("Este es el sueldo base"))
venta1=int(input("Esta es la primera venta: "))
venta2=int(input("Esta es la segunda venta: "))
venta3=int(input("Esta es la tercera venta: "))
comision=(venta1+venta2+venta3)*0.10

print("La comision es igual a: ",comision)
print("Mas las comisiones de las ventas: ",sueldobase+comision)