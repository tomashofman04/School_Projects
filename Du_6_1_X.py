if __name__ == '__main__':
    print('zadej cislo a:')
    a=int(input())
    #a=int(input('zadej cislo a:'))
    b=int(input('radej cislo b:'))
    c=int(input('zadej cislo c:'))
    vysledek = ((a * b) - c * 6) / (b - (a * c)) - (a + b * 2)
    print('vysledek prvni je:{}'.format(vysledek))
    print('vysledek prvni je:',vysledek)
    list=[]
    for a in range(0,10,1):
        vysledek = ((a * b) - c * 6) / (b - (a * c)) - (a + b * 2)
        list.append(vysledek)
        print('vysledek pro a:{} je roven:{}'.format(a,vysledek))
        print('vysledek pro a:',a,'je roven:',vysledek)
    for i in range(0,len(list),1):
        print('vysledek v listku na pozici:{} je roven{}'.format(i,list[i]))
        print('vysledek v listku na pozici:',i,'je roven',list[i])



    list2d=[]
    for i in range(0,5,1):
        radek=[]
        for j in range(0,5,1):
            if i==j:
                radek.append(1)
            else:
                radek.append(0)
            #print(' {} '. format(radek[j]),end='')
            print(radek[j],' ',end='')
        list2d.append(radek)
        print()
