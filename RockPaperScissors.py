import random
run = True
type_list = ['rock', 'paper', 'scissors']
x = 0
y = 0
if __name__ == '__main__':
    while run:
        chose = True
        while chose:
            print('1 - rock')
            print('2 - paper')
            print('3 - scissors')
            a = input('Chose 1 or 2 or 3 ')
            if a == '1':
                c = 'rock'
                chose = False
            elif a == '2':
                c = 'paper'
                chose = False
            elif a == '3':
                c = 'scissors'
                chose = False
        print(f'You chosed {c}')
        b = random.choice(type_list)
        print(f'Oponent chosed {b}')
        if c == 'rock':
            if b == 'rock':
                print('Draw!')
            elif b == 'paper':
                print('Enemy win!')
                y += 1
                print(f'{y} - {x}')
            else:
                print('You win!')
                x += 1
                print(f'{x} - {y}')
        elif c == 'paper':
            if b == 'rock':
                print('You win!')
                x += 1
                print(f'{x} - {y}')
            elif b == 'paper':
                print('Draw!')
            else:
                print('Enemy win!')
                y += 1
                print(f'{y} - {x}')
        else:
            if b == 'rock':
                print('Enemy win!')
                y += 1
                print(f'{y} - {x}')
            elif b == 'paper':
                print('You win!')
                x += 1
                print(f'{x} - {y}')
            else:
                print('Draw!')
        print()