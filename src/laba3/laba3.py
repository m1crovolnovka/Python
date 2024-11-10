from idlelib.iomenu import encoding
from sys import api_version
import json

def task1():
    with open("F1.txt", "w+", encoding='utf-8') as firstFile:
        i = input()
        while i != "":
            firstFile.write(i+'\n')
            i = input()
    N = int(input("Введите первый номер строки "))
    K = int(input("Введите второй номер строки "))
    numberOfLine = 1
    with open("F2.txt", "w", encoding='utf-8') as secondFile, open("F1.txt", "r", encoding='utf-8') as firstFile:
            for stroka in firstFile:
                if numberOfLine >= N and numberOfLine <= K:
                    secondFile.write(stroka)
                numberOfLine+=1

def task2():
    with open("ЖурналГруппы.txt", "r", encoding='utf-8') as myfile:
        for student in myfile:
            infStudent = student.split()
            average = sum(map(int,infStudent[1:]))/5
            if average < 6:
                print(student,end='')
def task3():
    lessonsDict = {}
    with open("Предметы.txt", "r", encoding='utf-8') as lessons:
        for lesson in lessons:
            listLesson = lesson.split()
            totalNumber = 0
            for countOfLesson in listLesson[1:]:
                number = ""
                for k in countOfLesson:
                    if k.isdigit():
                        number += k
                    else:
                        break
                totalNumber+=int(number)
            lessonsDict[listLesson[0]] =totalNumber
    print(lessonsDict)

def task4():
    list = [{},{}]
    with open("Фирмы.txt", "r", encoding='utf-8') as firmsFile:
        totalProfit = 0
        countOfProfit = 0
        for firm in firmsFile:
            firmlist = firm.split()
            profit= int(firmlist[2]) - int(firmlist[3])
            list[0][firmlist[0]] = profit
            if profit > 0:
                totalProfit+=profit
                countOfProfit += 1
        list[1]["average_profit"] = totalProfit/countOfProfit
    print(list)
    with open("Firms.json", "w", encoding='utf-8') as f:
        json.dump(list,f,ensure_ascii=False)

def main():
    while True:
        try:
            numberOfTask = int(input("Введите номер задания: "))
            match (numberOfTask):
                case 1:
                    task1()
                    return
                case 2:
                    task2()
                    return
                case 3:
                    task3()
                    return
                case 4:
                    task4()
                    return
                case _:
                    raise Exception
        except:
            print("Что-то не так")
main()
