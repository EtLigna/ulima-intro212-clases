# -*- coding: utf-8 -*-

ahorro = 100
tea = 0.05

tem = (1+tea) ** (1/12) - 1

mes1 = ahorro * (1+tem)
print("Mes 1:", mes1)

mes2 = (ahorro + mes1) * (1+tem)
print("Mes 2:", mes2)

mes3 = (ahorro + mes2) * (1+tem)
print("Mes 3:", mes3)

mes4 = (ahorro + mes3) * (1+tem)
print("Mes 4:", mes4)
