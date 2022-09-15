

class Lentele:
    def __init__(self, zaidejas, a=" ", b=' ', c=' ', d=' ', e=' ', f=' ', g=' ', h=' ', i=' '):
        self.zaidejas = zaidejas
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.sarasas = [a, b, c, d, e, f, g, h, i]

    def __repr__(self):
        return f"--------------------\n" \
               f"  {self.g}   |  {self.h}   |  {self.i}   \n" \
               f"--------------------\n" \
               f"  {self.d}   |  {self.e}   |  {self.f}   \n" \
               f"--------------------\n" \
               f"  {self.a}   |  {self.b}   |  {self.c}   \n" \
               f"--------------------\n"

    def switchplayers(self, player1, player2, kitas):
        if kitas == player1:
            kitas = player2
            return kitas
        if kitas == player2:
            kitas = player1
            return kitas


    def isvalyti(self, sarasas):
        sarasas[0] = " "
        sarasas[1] = " "
        sarasas[2] = " "
        sarasas[3] = " "
        sarasas[4] = " "
        sarasas[5] = " "
        sarasas[6] = " "
        sarasas[7] = " "
        sarasas[8] = " "
        self.a = " "
        self.b = " "
        self.c = " "
        self.d = " "
        self.e = " "
        self.f = " "
        self.g = " "
        self.h = " "
        self.i = " "

        return sarasas, self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i

    def kompiuterio_logika(self, sarasas, kas, uzpildyti):
        nepavyko = "Nepavyko"

        # GYNYBA
        if sarasas[0] == kas and sarasas[1] == kas and 3 not in uzpildyti:
            sarasas[2] = "O"
            self.c = "O"
            return 3
        if sarasas[6] == kas and sarasas[4] == kas and 3 not in uzpildyti:
            sarasas[2] = "O"
            self.c = "O"
            return 3
        if sarasas[8] == kas and sarasas[4] == kas and 1 not in uzpildyti:
            sarasas[0] = "O"
            self.a = "O"
            return 1
        elif sarasas[3] == kas and sarasas[4] == kas and 6 not in uzpildyti:
            sarasas[5] = "O"
            self.f = "O"
            return 6
        elif sarasas[6] == kas and sarasas[7] == kas and 9 not in uzpildyti:
            sarasas[8] = "O"
            self.i = "O"
            return 9
        elif sarasas[0] == kas and sarasas[3] == kas and 7 not in uzpildyti:
            sarasas[6] = "O"
            self.g = "O"
            return 7
        elif sarasas[1] == kas and sarasas[4] == kas and 8 not in uzpildyti:
            sarasas[7] = "O"
            self.h = "O"
            return 8
        elif sarasas[2] == kas and sarasas[5] == kas and 9 not in uzpildyti:
            sarasas[8] = "O"
            self.i = "O"
            return 9
        elif sarasas[6] == kas and sarasas[2] == kas and 5 not in uzpildyti:
            sarasas[4] = "O"
            self.e = "O"
            return 5
        elif sarasas[0] == kas and sarasas[8] == kas and 5 not in uzpildyti:
            sarasas[4] = "O"
            self.e = "O"
            return 5
        if sarasas[0] == kas and sarasas[4] == kas and 9 not in uzpildyti:
            sarasas[8] = "O"
            self.i = "O"
            return 9
        elif sarasas[2] == kas and sarasas[4] == kas and 7 not in uzpildyti:
            sarasas[6] = "O"
            self.g = "O"
            return 7
        elif sarasas[1] == kas and sarasas[2] == kas and 1 not in uzpildyti:
            sarasas[0] = "O"
            self.a = "O"
            return 1
        elif sarasas[7] == kas and sarasas[8] == kas and 7 not in uzpildyti:
            sarasas[6] = "O"
            self.g = "O"
            return 7
        elif sarasas[4] == kas and sarasas[5] == kas and 4 not in uzpildyti:
            sarasas[3] = "O"
            self.d = "O"
            return 4
        elif sarasas[4] == kas and sarasas[7] == kas and 2 not in uzpildyti:
            sarasas[1] = "O"
            self.b = "O"
            return 2
        elif sarasas[6] == kas and sarasas[3] == kas and 1 not in uzpildyti:
            sarasas[0] = "O"
            self.a = "O"
            return 1
        elif sarasas[8] == kas and sarasas[5] == kas and 3 not in uzpildyti:
            sarasas[2] = "O"
            self.c = "O"
            return 3
        elif sarasas[1] == kas and sarasas[7] == kas and 5 not in uzpildyti:
            sarasas[4] = "O"
            self.e = "O"
            return 5
        elif sarasas[6] == kas and sarasas[0] == kas and 4 not in uzpildyti:
            sarasas[3] = "O"
            self.d = "O"
            return 4
        elif sarasas[8] == kas and sarasas[2] == kas and 6 not in uzpildyti:
            sarasas[5] = "O"
            self.f = "O"
            return 6

        # ATAKA
        elif sarasas[0] == kas and not (sarasas[3] == kas or sarasas[1] == kas) and 5 not in uzpildyti:
            sarasas[4] = "O"
            self.e = "O"
            return 5
        elif sarasas[6] == kas and not (sarasas[3] == kas or sarasas[7] == kas) and 5 not in uzpildyti:
            sarasas[4] = "O"
            self.e = "O"
            return 5
        elif sarasas[8] == kas and not (sarasas[7] == kas or sarasas[5] == kas) and 5 not in uzpildyti:
            sarasas[4] = "O"
            self.e = "O"
            return 5
        elif sarasas[2] == kas and not (sarasas[5] == kas or sarasas[1] == kas) and 5 not in uzpildyti:
            sarasas[4] = "O"
            self.e = "O"
            return 5
        elif sarasas[4] == kas and not (
                sarasas[3] == kas or sarasas[1] == kas or sarasas[2] == kas or sarasas[5] == kas or sarasas[8] == kas or
                sarasas[7] == kas or sarasas[6] == kas) and 1 not in uzpildyti:
            sarasas[0] = "O"
            self.a = "O"
            return 1
        elif sarasas[4] == kas and not (
                sarasas[3] == kas or sarasas[1] == kas or sarasas[2] == kas or sarasas[5] == kas or sarasas[8] == kas or
                sarasas[7] == kas or sarasas[0] == kas) and 7 not in uzpildyti:
            sarasas[6] = "O"
            self.g = "O"
            return 7
        elif sarasas[4] == kas and not (
                sarasas[3] == kas or sarasas[1] == kas or sarasas[2] == kas or sarasas[5] == kas or sarasas[0] == kas or
                sarasas[7] == kas or sarasas[6] == kas) and 9 not in uzpildyti:
            sarasas[8] = "O"
            self.i = "O"
            return 9
        elif sarasas[4] == kas and not (
                sarasas[0] == kas or sarasas[1] == kas or sarasas[2] == kas or sarasas[5] == kas or sarasas[8] == kas or
                sarasas[7] == kas or sarasas[6] == kas) and 3 not in uzpildyti:
            sarasas[2] = "O"
            self.c = "O"
            return 3

        # LAIMEJIMUI
        if sarasas[0] == "O" and sarasas[1] == "O" and 3 not in uzpildyti:
            sarasas[2] = "O"
            self.c = "O"
            return 3
        if sarasas[6] == "O" and sarasas[4] == "O" and 3 not in uzpildyti:
            sarasas[2] = "O"
            self.c = "O"
            return 3
        if sarasas[8] == "O" and sarasas[4] == "O" and 1 not in uzpildyti:
            sarasas[0] = "O"
            self.a = "O"
            return 1
        elif sarasas[3] == "O" and sarasas[4] == "O" and 6 not in uzpildyti:
            sarasas[5] = "O"
            self.f = "O"
            return 6
        elif sarasas[6] == "O" and sarasas[7] == "O" and 9 not in uzpildyti:
            sarasas[8] = "O"
            self.i = "O"
            return 9
        elif sarasas[0] == "O" and sarasas[3] == "O" and 7 not in uzpildyti:
            sarasas[6] = "O"
            self.g = "O"
            return 7
        elif sarasas[1] == "O" and sarasas[4] == "O" and 8 not in uzpildyti:
            sarasas[7] = "O"
            self.h = "O"
            return 8
        elif sarasas[2] == "O" and sarasas[5] == "O" and 9 not in uzpildyti:
            sarasas[8] = "O"
            self.i = "O"
            return 9
        elif sarasas[6] == "O" and sarasas[2] == "O" and 5 not in uzpildyti:
            sarasas[4] = "O"
            self.e = "O"
            return 5
        elif sarasas[0] == "O" and sarasas[8] == "O" and 5 not in uzpildyti:
            sarasas[4] = "O"
            self.e = "O"
            return 5
        if sarasas[0] == "O" and sarasas[4] == "O" and 9 not in uzpildyti:
            sarasas[8] = "O"
            self.i = "O"
            return 9
        elif sarasas[2] == "O" and sarasas[4] == "O" and 7 not in uzpildyti:
            sarasas[6] = "O"
            self.g = "O"
            return 7
        elif sarasas[1] == "O" and sarasas[2] == "O" and 1 not in uzpildyti:
            sarasas[0] = "O"
            self.a = "O"
            return 1
        elif sarasas[7] == "O" and sarasas[8] == "O" and 7 not in uzpildyti:
            sarasas[6] = "O"
            self.g = "O"
            return 7
        elif sarasas[4] == "O" and sarasas[5] == "O" and 4 not in uzpildyti:
            sarasas[3] = "O"
            self.d = "O"
            return 4
        elif sarasas[4] == "O" and sarasas[7] == "O" and 2 not in uzpildyti:
            sarasas[1] = "O"
            self.b = "O"
            return 2
        elif sarasas[6] == "O" and sarasas[3] == "O" and 1 not in uzpildyti:
            sarasas[0] = "O"
            self.a = "O"
            return 1
        elif sarasas[8] == "O" and sarasas[5] == "O" and 3 not in uzpildyti:
            sarasas[2] = "O"
            self.c = "O"
            return 3
        elif sarasas[1] == "O" and sarasas[7] == "O" and 5 not in uzpildyti:
            sarasas[4] = "O"
            self.e = "O"
            return 5
        elif sarasas[6] == "O" and sarasas[0] == "O" and 4 not in uzpildyti:
            sarasas[3] = "O"
            self.d = "O"
            return 4
        elif sarasas[8] == "O" and sarasas[2] == "O" and 6 not in uzpildyti:
            sarasas[5] = "O"
            self.f = "O"
            return 6
        else:
            return nepavyko

    def deti_zenkla(self, ivestis, sarasas):
        if ivestis == 1:
            self.a = self.zaidejas
            sarasas[0] = self.zaidejas
            return self.a
        if ivestis == 2:
            self.b = self.zaidejas
            sarasas[1] = self.zaidejas
            return self.b
        if ivestis == 3:
            self.c = self.zaidejas
            sarasas[2] = self.zaidejas
            return self.c
        if ivestis == 4:
            self.d = self.zaidejas
            sarasas[3] = self.zaidejas
            return self.d
        if ivestis == 5:
            self.e = self.zaidejas
            sarasas[4] = self.zaidejas
            return self.e
        if ivestis == 6:
            self.f = self.zaidejas
            sarasas[5] = self.zaidejas
            return self.f
        if ivestis == 7:
            self.g = self.zaidejas
            sarasas[6] = self.zaidejas
            return self.g
        if ivestis == 8:
            self.h = self.zaidejas
            sarasas[7] = self.zaidejas
            return self.h
        if ivestis == 9:
            self.i = self.zaidejas
            sarasas[8] = self.zaidejas
            return self.i