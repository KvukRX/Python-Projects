import pickle

map_list = {}
num = 0
def new_map():
    a = int(input("введите высоту уровня: "))
    room = []
    global num

    print(
        "А теперь нарисуйте уровень. Используйте (-) для стенок, (x) для клеток перемещения. \n Не забывайте ставить пробелы между каждой клеткой!\n")

    for i in range(a):
        room.append(list(map(str, input().split())))
    map_list.update({num: room})
    num += 1
    with open('Saved_Dict.pkl', 'wb') as f:
        pickle.dump(map_list, f)
    main()

def main():
    print('хотите создать новую карту?\n')
    bool = str(input('Yes|No\n'))
    if bool == 'Yes':
        new_map()
    else:
        ans = str(input('Хотите посмотреть существующие карты?\nYes|No\n'))
        if ans == 'Yes':
            with open('Saved_Dict.pkl', 'rb') as f:
                loaded_dict = pickle.load(f)
                print(loaded_dict)

main()