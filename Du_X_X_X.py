if __name__ == "__main__":
    a = int(input('zadej a'))
    b = int(input('zadej b'))
    c = int(input('zadej c'))
    list2d=[]
    for i in range(0,b,1):
        radek=[]
        for j in range(0,a,1):
            radek.append(1)
            print('{}-'.format(radek[j]), end='')
        list2d.append(radek)
        print()
    print('')
    for i in range(0,b,1):
        for j in range(0,a,1):
            if j % 2 == 0:
                list2d[i][j]*=2
            else:
                list2d[i][j]*=c
            print(' {} '.format(list2d[i][j]), end='')
        print()
    print('')
    list1d=[]
    for i in range (0,len(list2d),1):
        prumer=0
        for j in range(0,len(list2d[i]),1):
            prumer+=list2d[i][j]
        prumer=prumer/(j+1)
        list1d.append(prumer)
    for i in range(0,len(list1d),1):
        print('Průměr {}.radku je roven={}'.format(i,list1d[i]))

