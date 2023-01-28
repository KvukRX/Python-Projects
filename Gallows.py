def main():
    a = 5
    word = str(input("загадайте слово \n"))
    secret = word
    word = word.lower()
    word = list(word)
    answer = list("_" * len(word))
    print(answer)
    print('у вас ' + str(a) + ' попыток')
    while a > 0:
        let = str(input("угадай букву"))
        let = let.lower()
        if word.count(let) > 0:
            n = word.count(let)
            while n > 0:
                n -= 1
                i = word.index(let)
                word[i] = '-'
                answer[i] = let
            print(answer)
        else:
            a -= 1
            print('осталось ' + str(a) + ' попыток')
        if a == 0:
            print('You lost!'+'answer was '+secret)
            break
        if answer.count('_') == 0:
            print('You won!')
            break
main()