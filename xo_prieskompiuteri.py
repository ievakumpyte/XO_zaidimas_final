import sys
import time
import random
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
        while lentele.zaidejas == "X":
            try:
                ivesk = int(input(f"\n{lentele.zaidejas} Įvesk skaičių nuo 1 iki 9 (pvz. žr. viršuje):"))
            except ValueError:
                print("Netinkama reikšmė. Įveskite skaičiu (1-9)")
            except TypeError:
                print("Netinkama reikšmė. Įveskite skaičiu (1-9)")

            if ivesk not in uzpildyti_lang and ivesk in range(1, 10):
                uzpildyti_lang.append(ivesk)
                lentele.deti_zenkla(ivesk, lentele.sarasas)
                lentele.zaidejas = lentele.switchplayers("X", "O", lentele.zaidejas)
                print(lentele)
                break
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
        if lentele.zaidejas == "O":
            logic = lentele.kompiuterio_logika(lentele.sarasas, "X", uzpildyti_lang)
            logika_ats = []
            logika_ats.append(logic)

            if logic == "Nepavyko" and lentele.sarasas.__contains__(" "):
                while True:
                    randomas = random.randint(1, 9)
                    if randomas not in uzpildyti_lang:
                        print("Kompiuteris:")
                        uzpildyti_lang.append(randomas)
                        lentele.deti_zenkla(randomas, lentele.sarasas)
                        lentele.zaidejas = lentele.switchplayers("X", "O", lentele.zaidejas)
                        time.sleep(0.4)
                        if arlaimejo(lentele.sarasas, "X") != True:
                            print(lentele)
                        break
            else:
                print("Kompiuteris:")
                uzpildyti_lang.append(logic)
                time.sleep(0.4)
                lentele.deti_zenkla(logic, lentele.sarasas)
                lentele.zaidejas = lentele.switchplayers("X", "O", lentele.zaidejas)
                if arlaimejo(lentele.sarasas, "X") != True:
                    print(lentele)

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
        print("LYGIOSIOS")
        print("X: ", len(x_laimejimai), "\nO: ", len(o_laimejimai))


zaidimas()
while True:
    try:
        veiksmas = int(input("1 - Žaisti dar kartą, 2 - Baigti žaidimą: "))
    except ValueError:
        print("Netinkama reikšmė. Įveskite skaičių (1-2")
    except TypeError:
        print("Netinkama reikšmė. Įveskite skaičių (1-2")

    if veiksmas == 1:
        lentele = Lentele("X")
        lentele.isvalyti(lentele.sarasas)
        uzpildyti_lang.clear()
        zaidimas()
    elif veiksmas == 2:
        sys.exit(0)
