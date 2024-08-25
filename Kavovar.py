class kavovar:
    def __init__(self, kafe, voda, mliko, kelimek, odpad, elektryna):
        self.kafe = kafe
        self.voda = voda
        self.mliko = mliko
        self.kelimek = kelimek
        self.odpad = odpad
        self.__elektryna = elektryna

    def __bool__(self, elektryna):
        self.__elektryna = elektryna

    def get_kafe(self):
        return self.kafe
    def get_voda(self):
        return self.voda
    def get_mliko(self):
        return self.mliko
    def get_kelimek(self):
        return self.kelimek
    def get_odpad(self):
        return self.odpad
    def get_elektrina(self):
        return self.__elektryna

    def get_me(self):
        print(f"KAFE      - {self.kafe}G")
        print(f"VODA      - {self.voda}ML")
        print(f"MLIKO     - {self.mliko}ML")
        print(f"KELIMKU   - {self.kelimek}KS")
        print(f"ODPAD     - {self.odpad}MC3")
        print(f"ELEKTRINA - {self.__elektryna}")
        print()

    def doplnit(self):
        a = int(input(f"KAFE - {self.kafe}G      +"))
        self.kafe+=a
        a = int(input(f"VODA - {self.voda}ML     +"))
        self.voda += a
        a = int(input(f"MLIKO - {self.mliko}ML    +"))
        self.mliko += a
        a = int(input(f"KELIMKU - {self.kelimek}KS  +"))
        self.kelimek += a
        print("-")
        self.get_me()

    def vycistit_odpad(self):
        self.odpad = 0
        print(f"ODPAD     - {self.odpad}MC3")
        print()

    def zapojit_do_el(self):
        print(f"ELEKTRINA - {self.__elektryna}")
        print()

    def vypojit_z_el(self):
        print(f"ELEKTRINA - {self.__elektryna}")
        print()

    def late(self):
        x = 0
        if self.get_kafe() < 300:
            print(f"MALO KAFE - {self.kafe}G - POTREBA: 300G")
            x=1
        if self.get_voda() < 250:
            print(f"MALO VODY - {self.voda}ML - POTREBA: 250ML")
            x=1
        if self.get_kelimek() < 1:
            print(f"MALO KELIMKU - {self.kelimek}KS - POTREBA: 1KS")
            x=1
        if self.get_odpad() > 500:
            print(f"MOC ODPADU - {self.odpad}CM3")
            x=1
        if self.get_elektrina() == False:
            print("NENI ELEKTRINA")
            x=1
        if x == 0:
            self.kafe -= 300
            self.voda -= 250
            self.kelimek -= 1
            self.odpad += 6
            print("+1 LATE")
            self.get_me()
        else:
            print()

    def espresso(self):
        x = 0
        if self.get_kafe() < 350:
            print(f"MALO KAFE - {self.kafe}G - POTREBA: 350G")
            x=1

        if self.get_voda() < 300:
            print(f"MALO VODY - {self.voda}ML - POTREBA: 300ML")
            x=1

        if self.get_mliko() < 200:
            print(f"MALO MLIKA - {self.mliko}ML - POTREBA: 200ML")
            x=1

        if self.get_kelimek() < 1:
            print(f"MALO KELIMKU - {self.kelimek}KS - POTREBA: 1KS")
            x=1

        if self.get_odpad() > 500:
            print(f"MOC ODPADU - {self.odpad}CM3")
            x=1

        if self.get_elektrina() == False:
            print("NENI ELEKTRINA")
            x=1

        if x == 0:
            self.kafe -= 350
            self.voda -= 300
            self.mliko -= 200
            self.kelimek -= 1
            self.odpad += 7
            print("+1 ESPRESSO")
            self.get_me()
        else:
            print()


if __name__=='__main__':
    print("1 - DOPLNIT AUTOMATICKY")
    a = int(input("2 - DOPLNIT MANUALNE"))
    print()
    if a ==1:
        kavovar1 = kavovar(666, 500, 600, 100, 0, True)
    else:
        k = int(input("KAFE - G                          (int)"))
        v = int(input("VODA - ML                         (int)"))
        m = int(input("MLIKO - ML                        (int)"))
        ke = int(input("KELIMKU - KS                      (int)"))
        o = int(input("ODPAD - MC3                       (int)"))
        e = bool(input("ELEKTRINA                         (bool)"))
        print()
        kavovar1 = kavovar(k, v, m, ke, o, e)
    run = 1
    while run == 1:
        print("1 - ZJISTIT OBSAH KAVOVARU")
        print("2 - DOPLNIT OBSAH KAVOVARU")
        print("3 - VYCISTIT KAVOVAR")
        print("4 - ZAPOJIT DO ELEKTRINY")
        print("5 - VYPOJIT Z ELEKTRINY")
        print("6 - UDELAT LATE")
        z = int(input("7 - UDELAT ESPRESSO"))
        print()

        if z == 1:
            kavovar1.get_me()
        elif z == 2:
            kavovar1.doplnit()
        elif z == 3:
            kavovar1.vycistit_odpad()
        elif z == 4:
            kavovar1.zapojit_do_el()
        elif z == 5:
            kavovar1.vypojit_z_el()
        elif z == 6:
            kavovar1.late()
        elif z == 7:
            kavovar1.espresso()
        else:
            run = 2

