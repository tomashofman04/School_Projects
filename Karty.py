import random, time
if __name__ == '__main__':
    pokracovat = '1'
    while pokracovat == '1':


#1) Hráč má k dispozici balíček 32 karet.
        balicek = []
        for i in range(0, 32):
            balicek.append(i)


#2) Karty jsou v balíčků seřazené, proto je před hrou hráč zamíchá.
        random.shuffle(balicek)


#3) Hráč líže z vrchu balíčku kartu a hledá výherní kartu. (Sám si řekne před prvním líznutím, která karta je výherní)

 #3.1) Sám si řekne před prvním líznutím, která karta je výherní
        setting = True
        while setting:
            x = int(input("Vyber vyherní kartu: (0-31) "))
            if 1 <= x <= 32:
                setting = False

#3.2) Hráč líže z vrchu balíčku kartu a hledá výherní kartu.
        i = 0
        for hra in balicek:
            for karta in range(1):
                print('karta', balicek[i])


#4) Pokud líznete kartu a bude se jednat o výherní kartu – poté hráč vítězí, informujte hráče o vítězství a dejte mu
#   možnost si zvolit, zda bude chtít hrát znova, nebo hru bude chtít ukončit.

 #4.1) Pokud líznete kartu a bude se jednat o výherní kartu – poté hráč vítězí, informujte hráče o vítězství
            if balicek[i] == x:
                print ("Je výherní!")
                break
            else:
                print ("Není výherní.")
                time.sleep(0.3)
                i = i + 1

 #4.2) dejte mu možnost si zvolit, zda bude chtít hrát znova, nebo hru bude chtít ukončit.
        print("Chcete pokracovat ve hre?")
        pokracovat = input('Pokud ano napis "1" pokud ne napis cokoliv jineho. ')


#5) Při skončení hry karty seřadíte od největší do nejmenší a pro kontrolu si je vytisknete. (př. Karta31, Karta30…. Karta0)
    balicek=list(range(0, 32))
    sorted_balicek=sorted(balicek, key=int, reverse=True)
    #sorted_balicek = list(itertools.product(sorted_balicek))
    for konec in range(32):
        print("karta", sorted_balicek[konec])
