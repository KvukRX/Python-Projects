import pickle

room = []
loaded_dict = None
l = 10

def main():
    ans = input('Create new map|choose existed\n')
    ans = ans.lower()
    if ans == 'create new map':
        a = int(input("введите высоту уровня: "))

        global room

        print("А теперь нарисуйте уровень. Используйте (-) для стенок, (x) для клеток перемещения. \n Не забывайте ставить пробелы между каждой клеткой!\n")

        global l
        for i in range(a):
            room.append(list(map(str, input().split())))
            if i > l:
                l = i
        game()
    else:
        with open('Saved_Dict.pkl', 'rb') as f:
            room = pickle.load(f)
            global loaded_dict
            choose()

def choose():
    num = int(input('Pick a map number', loaded_dict.keys))
    global room
    room = loaded_dict[num]
    for f in range(len(room)):
        for g in range(len(room[l])):
            print(room[f][g], end=" ")
        print()
    ans = input('Confurm?\nYes|No\n')
    ans = ans.lower()
    if ans == 'yes':
        game()
    else:
        main()


def game():
    Px = int(input('задайте позицию игрока X: '))
    Py = int(input('задайте позицию игрока Y: '))
    Tx = int(input('задайте позицию сокровища X: '))
    Ty = int(input('задайте позицию сокровища Y: '))

    for n in range(len(room)):
        for k in range(len(room[l])):
            if Px == n and Py == k and room[n][k] == '-':
                print('вы не можете начать отсюда')
                Px = int(input('задайте позицию игрока X: '))
                Py = int(input('задайте позицию игрока Y: '))
            if Tx == n and Ty == k and room[n][k] == '-':
                print('здесь не может быть сокровища')
                Tx = int(input('задайте позицию сокровища X: '))
                Ty = int(input('задайте позицию сокровища Y: '))
            if Px == n and Py == k and room[n][k] == 'x':
                print('позиция игрока задана')
                room[n][k] = '0'
            if Tx == n and Ty == k and room[n][k] == 'x':
                print('позиция сокровища задана')
                # room[n][k] = '*'
            elif Tx == n and Ty == k and room[n][k] == '0':
                print('сокровище нельзя ставить на игрока')
                Tx = int(input('задайте позицию сокровища X: '))
                Ty = int(input('задайте позицию сокровища Y: '))

            for f in range(len(room)):
                for g in range(len(room[l])):
                    print(room[f][g], end=" ")
                print()

            while True:
                print('куда вы хотите пойти?')
                Direction = str(input("Вперёд:Назад:Влево:Вправо\n   1     2     3      4  \nВвод: "))
                Direction = Direction.lower()
                match Direction:
                    case 'вперёд' | '1':
                        if room[Px - 1][Py] == '-':
                            print('На пути стена')
                        else:
                            room[Px][Py] = 'x'
                            Px -= 1
                            room[Px][Py] = '0'
                    case 'назад' | '2':
                        if room[Px + 1][Py] == '-':
                            print('На пути стена')
                        else:
                            room[Px][Py] = 'x'
                            Px += 1
                            room[Px][Py] = '0'
                    case 'влево' | '3':
                        if room[Px][Py - 1] == '-':
                            print('На пути стена')
                        else:
                            room[Px][Py] = 'x'
                            Py -= 1
                            room[Px][Py] = '0'
                    case 'вправо' | '4':
                        if room[Px][Py + 1] == '-':
                            print('На пути стена')
                        else:
                            room[Px][Py] = 'x'
                            Py += 1
                            room[Px][Py] = '0'
                if Px == Tx and Py == Ty:
                    print('ТЫ НАШЁЛ СОКРОВИЩЕ!')
                    break
                else:
                    for f in range(len(room)):
                        for g in range(len(room[l])):
                            print(room[f][g], end=" ")
                        print()
main()