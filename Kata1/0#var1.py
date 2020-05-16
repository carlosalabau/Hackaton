"""
Una panaderia vende barras de pan a 3.49€ cada una. El pan que no es del dia tiene un descuento del 60%.
Escribe un programa que comience leyendo el numero de barras vendidas que no son del dia. Despues tu programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final de total

"""

precio = 3.49
descuento = 1 - 0.6
precio_descuento = precio * descuento

barras = int(input("Introduce el numero de barras vendidas:"))
print("Precio habitual " + str(precio))
print("Descuento " + str(precio_descuento))
print("Coste final: " + str(barras * precio_descuento))