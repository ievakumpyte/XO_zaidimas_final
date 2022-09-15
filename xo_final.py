import sys
import time
import random
from modules.lentele import Lentele
from modules.tikrinimas_arlaimejo import arlaimejo


def reset_reiksmes():
    lentele.isvalyti(lentele.sarasas)
    uzpildyti_lang.clear()
    lentele.zaidejas = "X"


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

# Žaisti iš naujo metodas
def pakartoti(func1, func2, esamas):
    modas = mode(func1, func2, esamas)
    while True:
        if modas == 1:
            try:
                veiksmas = int(
                    input(
                        "\n1 - Žaisti dar kartą, 2 - Pakeisti žaidimo tipą -> pries kitą žaidėją, 3 - Baigti žaidimą: "))
            except ValueError:
                print("Netinkama reikšmė. Įveskite skaičių (1-2")
        if modas == 2:
            try:
                veiksmas = int(
                    input("\n1 - Žaisti dar kartą, 2 - Pakeisti žaidimo tipą -> prieš kompiuterį 3 - Baigti žaidimą: "))
            except ValueError:
                print("Netinkama reikšmė. Įveskite skaičių (1-2")

        if veiksmas == 1 and modas == 1:
            zaidimas_vs_pc()
        elif veiksmas == 1 and modas == 2:
            zaidimas_vs_player()
        elif veiksmas == 2 and modas == 1:
            print("\nŽAIDIMO TIPAS: Prieš kitą žaidėją")
            x_laimejimai.clear()
            o_laimejimai.clear()
            zaidimas_vs_player()
        elif veiksmas == 2 and modas == 2:
            print("\nŽAIDIMO TIPAS: Prieš kompiuterį:")
            x_laimejimai.clear()
            o_laimejimai.clear()
            zaidimas_vs_pc()
        elif veiksmas == 3:
            sys.exit(0)

# Tikrina ar laimėjo X arba O. Paduodami parametrai zaidimas1, zaidimas2 ir esamas,
# kad galėtų iškviesti funkcija pakartoti() - PLAY AGAIN
def tikrinti(zaidimas1, zaidimas2, esamas):
    if arlaimejo(lentele.sarasas, "X") == True:
        x_laimejimai.append("|")
        print("X: ", len(x_laimejimai), "\nO: ", len(o_laimejimai))
        reset_reiksmes()
        pakartoti(zaidimas1, zaidimas2, esamas)
        breaker = True

    elif arlaimejo(lentele.sarasas, "O") == True:
        o_laimejimai.append("|")
        print("X: ", len(x_laimejimai), "\nO: ", len(o_laimejimai))
        reset_reiksmes()
        pakartoti(zaidimas1, zaidimas2, esamas)
        breaker = True

# Žaidimas prieš kompiuterį
def zaidimas_vs_pc():
    esamas = zaidimas_vs_pc.__name__
    zaidimas1 = zaidimas_vs_pc.__name__
    zaidimas2 = zaidimas_vs_player.__name__
    while lentele.sarasas.__contains__(" "):
        breaker = False
        while lentele.zaidejas == "X":
            try:
                ivesk = int(input(f"\n{lentele.zaidejas} Įvesk skaičių nuo 1 iki 9 (pvz. žr. viršuje):"))
            except ValueError:
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

        tikrinti(zaidimas1,zaidimas2,esamas)

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

        tikrinti(zaidimas1,zaidimas2,esamas)

        if breaker:
            break
    else:
        breaker = True
        print("LYGIOSIOS")
        print("X: ", len(x_laimejimai), "\nO: ", len(o_laimejimai))
        reset_reiksmes()
        pakartoti(zaidimas1, zaidimas2, esamas)

# Žaidimas prieš kitą
def zaidimas_vs_player():
    zaidimas1 = zaidimas_vs_pc.__name__
    zaidimas2 = zaidimas_vs_player.__name__
    esamas = zaidimas_vs_player.__name__
    while lentele.sarasas.__contains__(" "):
        breaker = False
        try:
            ivesk = int(input(f"\n{lentele.zaidejas} Įvesk skaičių nuo 1 iki 9 (pvz. žr. viršuje):"))
        except ValueError:
            print("Netinkama reikšmė. Įveskite skaičiu (1-9)")
        except TypeError:
            print("Netinkama reikšmė. Įveskite skaičių (1-9")

        if ivesk not in uzpildyti_lang and ivesk in range(1, 10):
            uzpildyti_lang.append(ivesk)
            lentele.deti_zenkla(ivesk, lentele.sarasas)
            print(lentele)
            lentele.zaidejas = lentele.switchplayers("X", "O", lentele.zaidejas)
        elif ivesk not in range(1, 10):
            print("Skaičius turi būti nuo 1-9")
        else:
            print("Langelis  užimtas")
        tikrinti(zaidimas1,zaidimas2,esamas)
        if breaker:
            break
    else:
        breaker = True
        print("Lygiosios")
        print("X: ", len(x_laimejimai), "\nO: ", len(o_laimejimai))
        reset_reiksmes()
        pakartoti(zaidimas1, zaidimas2, esamas)

# Grąžina koks žaidimo tipas dabar veikime
def mode(func1, func2, esamas):
    zaidimo_tipas = 0
    if esamas == func1:
        zaidimo_tipas = 1
    if esamas == func2:
        zaidimo_tipas = 2
    return zaidimo_tipas


# Programos pradžia
while True:
    try:
        veiksmas = int(input("\nPasirinkite žaidimo tipa: 1 - prieš kompiuterį, 2 - prieš kitą zaideją 3 - baigti: "))
    except ValueError:
        print("Netinkama reikšmė. Įveskite skaičių (1-2")
    except TypeError:
        print("Netinkama reikšmė. Įveskite skaičių (1-2")

    if veiksmas == 1:
        print("Pries kompiuteri")
        zaidimas_vs_pc()
    elif veiksmas == 2:
        print("Pries zaideja")
        zaidimas_vs_player()
    elif veiksmas == 3:
        sys.exit(0)
