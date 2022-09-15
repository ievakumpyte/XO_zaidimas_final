import sys
from modules.lentele import Lentele
from modules.tikrinimas_arlaimejo import arlaimejo

breaker = False
uzpildyti_lang = []
x_laimejimai = []
o_laimejimai = []
lentele = Lentele("X")

print("""   
             ________________ 
            |  7 |  8  |  9  | 
            |----------------|
            |  4 |  5  |  6  |
            |----------------|
            |  1 |  2  |  3  |   
            |________________|

                        """)


def zaidimas():
    while lentele.sarasas.__contains__(" "):
        breaker = False
        try:
            ivesk = int(input(f"\n{lentele.zaidejas} Įvesk skaičių nuo 1 iki 9 (pvz. žr. viršuje):"))
        except ValueError:
            print("Netinkama reikšmė. Įveskite skaičiu (1-9)")

        if ivesk not in uzpildyti_lang and ivesk in range(1, 10):
            uzpildyti_lang.append(ivesk)
            lentele.deti_zenkla(ivesk, lentele.sarasas)
            print(lentele)
            lentele.zaidejas = lentele.switchplayers("X", "O", lentele.zaidejas)
        elif ivesk not in range(1, 10):
            print("Skaičius turi būti nuo 1-9")
        else:
            print("Langelis  užimtas")

        if arlaimejo(lentele.sarasas, "X") == True:
            x_laimejimai.append("|")
            print("X: ", len(x_laimejimai), "\nO: ", len(o_laimejimai))
            breaker = True
            break
        elif arlaimejo(lentele.sarasas, "O") == True:
            o_laimejimai.append("|")
            print("X: ", len(x_laimejimai), "\nO: ", len(o_laimejimai))
            breaker = True
            break

        if breaker:
            break
    else:
        breaker = True
        print("Lygiosios")
        print("X: ", len(x_laimejimai), "\nO: ", len(o_laimejimai))


zaidimas()
while True:
    try:
        veiksmas = int(input("1 - Žaisti dar kartą, 2 - Baigti žaidimą: "))
    except ValueError:
        print("Netinkama reikšmė. Įveskite skaičių (1-2")

    if veiksmas == 1:
        lentele = Lentele("X")
        lentele.isvalyti(lentele.sarasas)
        uzpildyti_lang.clear()
        zaidimas()
    elif veiksmas == 2:
        sys.exit(0)
