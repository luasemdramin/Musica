import os
os.system("cls")

import time 
letra = ["Ey, Tití me preguntó si tengo mucha' novia'", "Mucha' novia'", "Hoy tengo a una, mañana otra", "Me las vo'a llevar a toa' pa un VIP, un VIP, EY", "Saluden a Tití", "Vamo a tirarno un selfie, say CHEESE, EY", "Que sonrían las que ya les metí"] 
for linha in letra: 
    for letra in linha: 
        print(letra, end="",flush = True) 
        time.sleep(0.1) 
    print() 
    time.sleep(0.7) 