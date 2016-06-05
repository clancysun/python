from random import randint
num = randint(1, 100)

bingo = False

while bingo == False:
    answer = input('Guess what I think? ')

    if answer > num:
        print('%s is to big.' % answer)

    if answer < num:
        print('%s is to small.' % answer)

    if answer == num:
        print('Bingo, %s is the right answer!' % answer)
        bingo = True
