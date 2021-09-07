# -*- coding: utf-8 -*-
subtotal = float(input("Ingrese subtotal: "))
porc_gratuidad = float(input("Ingrese porcentaje de gratuidad: "))

gratuidad = subtotal * porc_gratuidad / 100
total = subtotal + gratuidad

print("Gratuidad:", gratuidad)
print("Total: ", total)