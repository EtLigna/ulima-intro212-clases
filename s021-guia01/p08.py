# -*- coding: utf-8 -*-
peso_libras = float(input("Ingrese peso en libras: "))
estatura_pulgadas = float(input("Ingrese estatura en pulgadas: "))

peso_kg = peso_libras * 0.4536
estatura_metros = estatura_pulgadas * 0.0254

imc = peso_kg / (estatura_metros)**2

print("El IMC es: ", imc)
