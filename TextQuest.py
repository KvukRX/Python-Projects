a = int(input("введите высоту уровня: "))

room = []

print(
    "А теперь нарисуйте уровень. Используйте (-) для стенок, (x) для клеток перемещения. \n Не забывайте ставить пробелы между каждой клеткой!\n")

for i in range(a):
    room.append(list(map(str, input().split())))

Px = int(input('задайте позицию игрока X: '))
Py = int(input('задайте позицию игрока Y: '))
Tx = int(input('задайте позицию сокровища X: '))
Ty = int(input('задайте позицию сокровища Y: '))

for n in range(len(room)):
    for k in range(len(room[i])):
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
    for g in range(len(room[i])):
        print(room[f][g], end=" ")
    print()
coin = 0
while coin == 0:
    print('куда вы хотите пойти?')
    Direction = str(input("Вперёд:Назад:Влево:Вправо "))
    Direction = Direction.lower()
    match Direction:
        case 'вперёд':
            if room[Px - 1][Py] == '-':
                print('На пути стена')
            else:
                room[Px][Py] = 'x'
                Px -= 1
                room[Px][Py] = '0'
        case 'назад':
            if room[Px + 1][Py] == '-':
                print('На пути стена')
            else:
                room[Px][Py] = 'x'
                Px += 1
                room[Px][Py] = '0'
        case 'влево':
            if room[Px][Py - 1] == '-':
                print('На пути стена')
            else:
                room[Px][Py] = 'x'
                Py -= 1
                room[Px][Py] = '0'
        case 'вправо':
            if room[Px][Py + 1] == '-':
                print('На пути стена')
            else:
                room[Px][Py] = 'x'
                Py += 1
                room[Px][Py] = '0'
    if Px == Tx and Py == Ty:
        print('ТЫ НАШЁЛ СОКРОВИЩЕ!')
        coin += 1
    else:
        for f in range(len(room)):
            for g in range(len(room[i])):
                print(room[f][g], end=" ")
            print()

