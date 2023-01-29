import csv

a = int(input("введите высоту уровня: "))

room = []

print("А теперь нарисуйте уровень. Используйте (-) для стенок, (x) для клеток перемещения. \n Не забывайте ставить пробелы между каждой клеткой!\n")

for i in range(a):
    room.append(list(map(str, input().split())))

file = open('File.csv', 'a')
wr = csv.writer(file, delimiter=' ')
wr.writerows(room)
