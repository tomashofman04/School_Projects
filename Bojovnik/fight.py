from bojovnik import Bojovnik as fighter
import random as rnd


class Fight():
    def __init__(self, boj1: fighter, boj2: fighter):
        self.__boj1: fighter = boj1
        self.__boj2: fighter = boj2



    #Spell (1-3)
    def Vampire_Bites(self, boj_utocici: fighter, boj_branici: fighter):
        atk_power = boj_branici.difference(boj_utocici.attack(), boj_branici.block())
        boj_branici.change_hp(-atk_power)
        boj_utocici.change_hp(atk_power)
        print(f"Bojovnik:{boj_utocici.get_name()} vysál {boj_branici.get_name()} {atk_power}krve, zbyva mu:{boj_branici.get_hp()} a sám si pdoplnil hp na {boj_utocici.get_hp()}")

    def Critical_Hit(self, boj_utocici: fighter, boj_branici: fighter):
        atk_power = boj_branici.difference(boj_utocici.attack(), boj_branici.block())
        atk_power = atk_power*2
        boj_branici.change_hp(-atk_power)
        print(f"Bojovnik:{boj_branici.get_name()} to schytal od:{boj_utocici.get_name()} za:{atk_power} a zbyva mu:{boj_branici.get_hp()}")

    def Coin_Of_Fortune(self, boj_utocici: fighter, boj_branici: fighter):
        c = rnd.randint(0, 1)
        if c==0:
            boj_branici.change_hp(-50)
            print(f"Bojovnik:{boj_branici.get_name()} to schytal od:Coin Of Fortune za:50 a zbyva mu:{boj_branici.get_hp()}")
        else:
            boj_utocici.change_hp(-50)
            print(f"Bojovnik:{boj_utocici.get_name()} to schytal od:Coin Of Fortune za:50 a zbyva mu:{boj_utocici.get_hp()}")


    #Potion (4-6)
    def Hp_Potion(self, boj_utocici: fighter):
        boj_utocici.change_hp(20)

    def Deff_Potion(self, boj_utocici: fighter):
        boj_utocici.change_deff(3)

    def Atk_Potion(self, boj_utocici: fighter):
        boj_utocici.change_atk(5)




    # Samotny vypocet attacku
    def attack(self, boj_utocici: fighter, boj_branici: fighter):
        print()
        print()
        print(f"Na řadě je {boj_utocici.get_name()}")
        print("1 - Vampire_Bites - Normální attak + live steal")
        print("2 - Critical_Hit - Critical attak (2*damage)")
        print("3 - Coin_Of_Fortune - 50% šace že spůsobíš 50 damage nepříteli ale pokud to nevyjde tak ho způsobíš sobě")
        print("4 - Hp_Potion - Získáš 20hp")
        print("5 - Deff_Potion - Získáš 3 deff do konce hry")
        print("6 - Atk_Potion - Získáš 5 atk do konce hry")
        print("7,8,9,0 - Nic")
        i = int(input(f"{boj_utocici.get_name()} zadej číslo od 1 do 9:"))
        if i == 1:
            print(f"{boj_utocici.get_name()} si vybral Vampire Bites")
            self.Vampire_Bites(boj_utocici, boj_branici)
        elif i == 2:
            print(f"Bojovnik:{boj_utocici.get_name()} si vybral ")
            self.Critical_Hit(boj_utocici, boj_branici)
        elif i == 3:
            print(f"Bojovnik:{boj_utocici.get_name()} si vybral Coin Of Fortune")
            self.Coin_Of_Fortune(boj_utocici, boj_branici)
        elif i == 4:
            print(f"Bojovnik:{boj_utocici.get_name()} si vybral Hp Potion")
            self.Hp_Potion(boj_utocici)
        elif i == 5:
            print(f"Bojovnik:{boj_utocici.get_name()} si vybral Deff Potion")
            self.Deff_Potion(boj_utocici)
        elif i == 6:
            print(f"Bojovnik:{boj_utocici.get_name()} si vybral Atk Potion")
            self.Atk_Potion(boj_utocici)
        else:
            print(f"Bojovnik:{boj_utocici.get_name()} si nevybral nic.")


        atk_power = boj_branici.difference(boj_utocici.attack(), boj_branici.block())
        boj_branici.change_hp(-atk_power)
        print(f"Bojovnik:{boj_branici.get_name()} to schytal od:{boj_utocici.get_name()} za:{atk_power} a zbyva mu:{boj_branici.get_hp()}")

    # Metoda pro generování, který bojovník bude bojovat. Aktuálně je to random z val.
    def who_attack(self, val):
        rnd_value = rnd.randint(0, val)
        if rnd_value <= int(val / 2):  # utoci bojovnik 1
            return self.attack(self.__boj1, self.__boj2)
        else:
            return self.attack(self.__boj2, self.__boj1)


    # metoda pro simulaci celeho zapasu a vyhodnoceni. vraci vitezneho bojovnika
    def process(self, val):
        while self.__boj1.get_hp() > 0 and self.__boj2.get_hp() > 0:
            self.who_attack(val)
        if self.__boj1.get_hp() < 0:
            print()
            print(f"Vyhral bojovnik:{self.__boj2.get_name()}.")
            print()
            return self.__boj2
        else:
            print()
            print(f"Vyhral bojovnik:{self.__boj1.get_name()}.")
            print()
            return self.__boj1

#    def to_string(self):
#        return f"Bojovnik:{self.__boj1.get_name()}_vs_Bojovnik:{self.__boj2.get_name()}"

