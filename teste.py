import os
import time
import sys

def estilo(texto, codigo):
    return f"\033[{codigo}m{texto}\033[0m"

def cantar_musica(versos):
    os.system("cls" if os.name == "nt" else "clear")

    for texto, delay, velocidade in versos:
        i = 0
        while i < len(texto):
            if texto[i] == "\033": 
                fim_cor = texto.find("m", i)
                sys.stdout.write(texto[i:fim_cor+1])
                i = fim_cor + 1
            else:
                sys.stdout.write(texto[i])
                sys.stdout.flush()
                time.sleep(velocidade)
                i += 1

        print("") 
        time.sleep(delay)

letra_sincronizada = [
    ("Di-divulga Privacy, OnlyFans", 0.4, 0.05),
    ("E plataforma do tigrin'...", 0.6, 0.05),
    ("Quando é que vai me chamar pra nóis fazer um amadorzin ??'", 1.1, 0.06),
    ("É que tem uns job que ela faz que é nuns horário duvidoso...", 1.0, 0.04),
    ("Nem vem com teus dois reais que ela quer ver o misterioso DJ CAYOO, DJ CAYOO !!", 0.7, 0.04),

    (estilo("Plataforma 'tá pagando com Visa e com xerecard", "1;32"), 0.4, 0.07),
    (estilo("Hoje é couro nas do job, sem leminha e sem massagem", "1;31"), 0.4, 0.06),
    (estilo("Plataforma 'tá pagando com Visa e com xerecard", "1;32"), 0.3, 0.06),
    (estilo("Hoje é couro nas do job, sem leminha e sem massagem", "1;31"), 0.8, 0.06),

    ("E-elas gosta de ParaFAL, só dá pra bandido", 0.7, 0.07),
    ("Ganha água e pau e sai da favela sorrindo...", 1.5, 0.07),
]

cantar_musica(letra_sincronizada)