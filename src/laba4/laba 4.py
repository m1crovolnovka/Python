class String:
    def __init__(self,str1):
        self.str1 = str1
    def countOfVowels(self):
        vowels = "aeiouyаеёоыуяиюэ"
        return sum(1 for a in self.str1 if a in vowels or a in vowels.upper() )
    def countOfConsonants(self):
        consonants = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ"
        return sum(1 for a in self.str1 if a in consonants or a in consonants.upper())
    def reverse(self):
        return self.str1[::-1]
    def info(self):
        print("В строке ", self.countOfVowels()," гласных, ", self.countOfConsonants()," согласных и ", len(self.str1), " символов.")
    def countOfWords(self):
        words = 1
        for i in range(len(self.str1))[1:]:
            if self.str1[i] == ' ' and self.str1[i + 1].isalpha() and self.str1[i-1]!=" ":
                words+=1
        return words

class Country:
    def __init__(self,capital,area,populationSize):
        self.capital = capital
        self.area = area
        self.populationSize = populationSize
    def __str__(self):
        return f"Столица: {self.capital}, площадь: {self.area}, численность населения: {self.populationSize}."
    def __repr__(self):
        return str(self)

def task2():
    listCountry = [Country("Минск",207600,9155978),
            Country("Москва",17123191,147182123),
            Country("Варшава",312696,37636508),
            Country("Вильнюс",65302,2893887),
            Country("Рига",64583,1871882)]
    while True:
        try:
            choice = int(input("Введите номер пункта "))
            match(choice):
                case 1:
                    minGivenArea = int(input("Введите минимальную площадь "))
                    maxGivenArea = int(input("Введите максимальную площадь "))
                    listArea = [country for country in listCountry if country.area >= minGivenArea and country.area <= maxGivenArea]
                    print(listArea)
                    return
                case 2:
                    minGivenPopulation = int(input("Введите минимальную численность "))
                    maxGivenPopulation = int(input("Введите максимальную численность "))
                    listArea = [country for country in listCountry if country.area >= minGivenPopulation and country.area <= maxGivenPopulation]
                    print(listArea)
                    return
        except:
            print("Что-то не так")

class Animal:
    def __gt__(self, other):
        return self.cost > other.cost
    def __str__(self):
        return "Животное породы: " + self.breed + " и ценой: "+ str(self.cost) +"р.\n"
    def __init__(self,breed,cost):
        self.breed = breed
        self.cost = cost
    def move(self):
        return "Я передвигаюсь"
class Fish(Animal):
    def __str__(self):
        return "Рыба породы: " + self.breed + " и ценой: "+ str(self.cost) +"р.\n"
    def move(self):
        return "Я плаваю"
class Bird(Animal):
    def __str__(self):
        return "Птица породы: " + self.breed + " и ценой: "+ str(self.cost)+"р.\n"
    def move(self):
        return "Я летаю"
class PetShop:
    def __init__(self,*args):
        self.animalList = args
    def expensiveBreed(self):
        print(max(self.animalList))
    def writeAnimal(self):
        with open("Животные", "w", encoding="utf-8") as file:
            file.writelines(map(str, self.animalList))
def task3():
    shop = PetShop(Bird("Корелла",408),
                   Bird("Гульда",360),
                   Bird("Какарик",185),
                   Fish("Сом Агамикс",10.10),
                   Fish("Кардинал",2.40),
                   Fish("Меченосец рубиновый",8.40))
    shop.expensiveBreed()
    shop.writeAnimal()

class House:
    count = 0
    def __init__(self,width, length):
        self.width = width
        self.length = length
        House.count += 1
    def calculateSquare(self):
        return self.length * self.width
    @classmethod
    def houseCount(cls):
        return cls.count
    @staticmethod
    def statusOfHouse(floor):
        if(floor >= 9):
            return "Здание многоэтажное"
        elif floor >= 5 and floor <= 8:
            return "Здание среднеэтажное"
        else:
            return "Здание малоэтажное"
def task4():
    bsuir5k = House(30,70)
    print(bsuir5k.calculateSquare())
    print(House.houseCount())
    print(House.statusOfHouse(9))
#def tasl3():
def main():
    while True:
        try:
            numberOfTask = int(input("Введите номер задания: "))
            match (numberOfTask):
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
