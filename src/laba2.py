def is_prime(num):
    if(num%2==0):
        return False
    for i in range(3,num,2):
        if num % i==0:
            return False
    return True
def task1():
    while(True):
        try:
            num = int(input("Введите число: "))
            if num < 0 or num >1000:
                raise Exception
            print(f"Число простое? {is_prime(num)}")
            return
        except:
            print("Ошибка ввода")
def calculate(obj):
    if isinstance(obj,list):
        for i in obj:
            if isinstance(i,str):
                print(len(i),end=" ")
        print()
    elif isinstance(obj,tuple):
        countLet= 0
        countNum =0
        for i in obj:
            if isinstance(i, str):
                countLet += len(i)
            if isinstance(i, int):
                countNum+=1
        print(f"Количество букв: {countLet}. Количество чисел: {countNum}")
    elif isinstance(obj,float) or isinstance(obj,int):
        print(str(obj)[::-1])
    elif isinstance(obj,str):
        sum = 0
        for i in obj:
            if i.isdigit():
                sum +=int(i)
        print(sum)
def task2():
    calculate(["Java","Python","C++",1,2,3])
    calculate((1,2,3,"Windows","Linux"))
    calculate(123.123)
    calculate("52 секунды")
def task3():
    while (True):
        try:
            order = int(input("Введите порядок матрицы: "))
            if order < 1:
                raise Exception
            break
        except:
            print("Ошибка ввода")
    while (True):
        try:
            matrix =[]
            for i in range(order):
                matrix.append(list(map(int, input("Введите строку матрицы ").split())))
                if len(matrix[-1]) != order:
                    raise Exception
            break
        except:print("Ошибка ввода")
    for i in range(order):
        for k in range((i + 1),order):
            if(matrix[i][k] != matrix[k][i]):
                print("Матрица не симметрична")
                return
    print("Матрица симметрична")
def task4():
        try:
            number = int(input("Введите число "))
        except:
            print("Преобразование прошло не удачно")
        finally:
            print("Блок try завершился")
while True:
    try:
        choice = int(input("Выберите номер задания "))
        if choice < 1 or choice > 4:
            raise Exception
        break
    except:
        print("Неправильный ввод")
match choice:
    case 1:
        task1()
    case 2:
        task2()
    case 3:
        task3()
    case 4:
        task4()