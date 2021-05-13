import random
import math

meeple = []
class Meeple:
    def __init__(self,name,sex,age,job,bal):
        self.name = name
        self.sex = sex
        self.age = age
        self.job = job
        self.bal = bal

def generateMeeples(num):
    ageSD = 8
    ageMU = 30
    job = "Unemployed"
    wealthSD = 300
    wealthMU = 1000
    names = []
    while len(meeple) != num:
        age = math.floor(random.normalvariate(ageMU,ageSD))
        bal = math.floor(random.normalvariate(wealthMU,wealthSD))
        if random.randrange(2) == 1:
            sex = "Male"
        else:
            sex = "Female"
        newname = getName(sex)
        if newname not in names:
            newname = getName(sex)
        names.append(newname)
        meeple.append(Meeple(newname,sex,age,job,bal))
def getName(sex):
    l = open("assets/names/lastnames.txt","r")
    last = l.read().split("\n")
    if sex == "Male":
        f = open("assets/names/malefirstnames.txt","r")
        first = f.read().split("\n")
    else:
        f= open("assets/names/femalefirstnames.txt","r")
        first = f.read().split("\n")
    return first[random.randrange(len(first)-1)]+" "+last[random.randrange(len(last)-1)]

def listMeeples(option = "all"):
    for i in meeple:
        if  option == "all":
            print(f'name:{i.name} Sex:{i.sex} Age:{i.age} Occupation:{i.job} Balance:{i.bal}')
        elif option == "names":
            print(i.name)
        elif option == "sex":
            print(f'{i.name} is {i.sex}')
        elif option == "age":
            print(f'{i.name} is {i.age}')
        elif option == "job":
            print(f'{i.name} is a {i.job}')
        elif option == "bal":
            print(f'{i.name} has {i.bal}')
        # elif option == "rel":
        #     print(listrelatives())
generateMeeples(100)
listMeeples("all")
