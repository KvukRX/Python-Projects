import random as r


def main():
    while True:
        x = r.randint(0, 2)
        choose = str(input("choose you fighter: \n"))
        choose = choose.lower()
        match choose:
            case 'rock':
                y = 0
            case 'paper':
                y = 1
            case 'scissors':
                y = 2
            case _:
                print('долбаёб ебаный буквы пиши сука')
        if x == y:
            print('ничья ебать')
        if (x == 0 and y == 1) or (x == 1 and y == 2) or (x == 2 and y == 0):
            print('хорош')
        if (x == 0 and y == 2) or (x == 1 and y == 0) or (x == 2 and y == 1):
            print('лох')


main()