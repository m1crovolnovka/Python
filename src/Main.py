def task1():
    num = input("Введите натуральное число ")
    is_increase = True
    for i in range(len(num) -1):
        if int(num[i]) >= int(num[i+1]):  continue
        else:
            is_increase = False
            break
    if(is_increase): print("Число упорядоченно по возрастанию справа налево")
    else: print("Число не упорядочено")
def task2():
    sogl = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬбвгджзйклмнпрстфхцчшщъь"
    glas = "АЕЁИОУЫЭЮЯаеёиоуыэюя"
    text = input()
    soglLetters =""
    glasLetters = 0
    words = 1
    for i in range(len(text)):
        if text[i] in sogl:
            soglLetters += text[i]
        if text[i] in glas:
            glasLetters += 1
        if text[i] == ' ' and text[i+1].isalpha():
            words +=1
    if len(soglLetters) == glasLetters:
        print(soglLetters)
    print(f"Количество слов: {words}")
def task3():
    spis = list(map(int,input("Введите список чисел").split()))
    count = 0
    for i in range(len(spis)):
        for k in range(i +1,len(spis)):
            if spis[i] == spis[k]: count+=1
    print(count)
def task4():
    stroka = input()
    dict = {}
    for i in stroka:
        if int(i) in dict:continue
        else: dict[int(i)] = stroka.count(i)
    print(dict)
def task5():
    dict={
        "Lego": [125,10],
        "Робот": [520,12],
        "Барби":[96, 7],
        "Hot Wheels":[19, 9],
        "Плюшевый Медведь":[206,3],
        "Бакуган":[40,20],
        "Мяч":[30,21],
        "Самокат":[150,4]
    }
    while True:
        print("Выберите действие: ","1 - Просмотр цены.", "2 - Просмотр количества.", "3 - Всю информацию.", "4 - Покупка.", "5 - До свидания.", sep = '\n')
        num = int(input());
        match num:
            case 1 :
                for i in dict.keys():
                    print(i,dict[i][0], "Руб.")
            case 2:
                for i in dict.keys():
                    print(i,dict.get(i)[1], "Шт.")
            case 3:
                for i in dict.keys():
                    print(i,dict.get(i)[0], "Руб.",dict.get(i)[1], "Шт.")
            case 4:
                choice = input("Выберите продукт ")
                while choice not in dict.keys():
                    choice = input("Выберите продукт ")
                count_pr = int(input("Выберите количество штук "))
                while count_pr > dict.get(choice)[1]:
                    count_pr = int(input("Выберите количество штук "))
                print("Сумма покупки: ", count_pr * dict.get(choice)[0])
                dict.get(choice)[1] -= count_pr;
                print("Осталось таких товаров: ", dict.get(choice)[1])
            case _ :
                return
def task6():
    spis = list(map(int,input("Введите список:").split()))
    n = len(spis)
    i = 0
    while i < n:
        if spis.count(spis[i]) > 1:
            spis.remove(spis[i])
            i-=1
            n-=1
        else: i+=1
    spis.reverse()  # spis = set(spis)# spis = spis[::-1]
    spis = tuple(spis)
    print(spis)
choice = int(input("Выберите номер задания "))
match choice:
    case 1:
        task1()
    case 2:
        task2()
    case 3:
        task3()
    case 4:
        task4()
    case 5:
        task5()
    case 6:
        task6()