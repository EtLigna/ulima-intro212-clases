# -*- coding: utf-8 -*-

'''
Pide: Cuantos NUEVOS infectados se reportaran
el 5 de abril de 2020.

nuevos_infectados = total_infectados_5_abr - total_infectados_4_abr

Formula infectados totales:
N(t) = N0 * e^5t

Por dato del problema:
    N0 = 5
    t_1abr = 0
    t_4abr = 3
    t_5abr = 4
    
nuevos_infectados = N(4) - N(3)
'''
N0 = 5
e = 2.72
t_4abr = 3
t_5abr = 4

N_4abr = N0 * e ** (5 * t_4abr)

N_5abr = N0 * e ** (5 * t_5abr)

nuevos_infectados = int(N_5abr - N_4abr)

print("Nuevos infectados el 5 de abril: ", nuevos_infectados)


