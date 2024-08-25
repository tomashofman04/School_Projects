from fight import Fight
from bojovnik import Bojovnik



if __name__=="__main__":
    a = input("P1 name:")
    b = int(input("P1 atk(rec.20):"))
    c = int(input("P1 deff(rec.15):"))
    d = int(input("P1 hp(rec.100):"))
    e = input("P2 name:")
    f = int(input("P2 atk(rec.20):"))
    g = int(input("P2 deff(rec.15):"))
    h = int(input("P2 hp(rec.100):"))
    boj1=Bojovnik(a,b,c,d)
    boj2=Bojovnik(e,f,g,h)
    souboj=Fight(boj1,boj2)
    souboj.process(100) # Random value podle ktere se pocita sance na utok prvniho nebo druheho bojovnika
    run = 1
    while run == 1:
        run = int(input("Odveta? 1-Ano 2-Ne 3-Ano ale změnit jména"))
        if run == 1:
            boj1=Bojovnik(a,b,c,d)
            boj2=Bojovnik(e,f,g,h)
            souboj=Fight(boj1,boj2)
            souboj.process(100)
        elif run == 3:
            a = input("P1 name:")
            b = int(input("P1 atk(rec.20):"))
            c = int(input("P1 deff(rec.15):"))
            d = int(input("P1 hp(rec.100):"))
            e = input("P2 name:")
            f = int(input("P2 atk(rec.20):"))
            g = int(input("P2 deff(rec.15):"))
            h = int(input("P2 hp(rec.100):"))
            boj1 = Bojovnik(a, b, c, d)
            boj2 = Bojovnik(e, f, g, h)
            souboj = Fight(boj1, boj2)
            souboj.process(100)

