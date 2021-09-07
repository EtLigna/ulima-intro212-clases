# -*- coding: utf-8 -*-
PI = 3.14159
longitud = float(input("Ingrese longitud: "))
radio = float(input("Ingrese radio: "))

area = PI * radio * radio
volumen = area * longitud

print("El valor del area es:", area)
print("El valor del volumen es:", volumen)