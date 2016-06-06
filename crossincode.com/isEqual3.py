def isEqual(num1, num2):
    if num1 < num2:
        print('too small')
        return False
    if num1 > num2:
        print('too big')
        return False
    if num1 == num2:
        print('Bingo')
        return True


from random import randint
num = randint(1, 100)

print('Guess what I think? ')
bingo = False

while bingo == False:
    answer = input()
    if answer < 0:
        print('Exit game...')
        break
    bingo = isEqual(answer, num)
