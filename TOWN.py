import random
import math

meeple = []
resource = []
class Meeple:
    def __init__(self,firstname,lastname,sex,age,job,bal):
        self.fname = firstname
        self.lname = lastname
        self.name = firstname+" "+lastname
        self.sex = sex
        self.age = age
        self.job = job
        self.married = False
        self.partner = []
        self.children = []
        self.inventory = {
         "bal" : bal
        }
    def addItem(self,item,amount):
        if item not in self.inventory:
            self.inventory.update({item:amount})
        else:
            self.inventory.update({item:self.inventory[item]+amount})
    def subtractItem(self,item,amount):
        self.inventory.update({item:self.inventory[item]-amount})

    def marry(self,other):
        if not self.married:
            if self.sex == "Male":
                other.lname = self.lname
                other.partner = self.name
                updatenames(meeple)
                self.partner = other.name
                self.married = True

            else:
                self.lname = other.lname
                other.partner = self.name
                updatenames(meeple)
                self.partner = other.name
                self.married = True


    def haveChild(self,other,children):
        if self.married :
            for item in range(children):
                if random.randrange(2) == 1:
                    sex = "Male"
                else:
                    sex = "Female"
                self.children = Meeple(getName(sex)[0],self.lname,sex,0,"unemployed",0)
                meeple.append(self.children)
        else:
            print('Married'+ self.married)



class Resource:
    def __init__(self,name,rarity):
        self.name = name
        self.rarity =rarity


def updatenames(obj):
    for i in obj:
        i.name = i.fname + " " + i.lname

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
        meeple.append(Meeple(newname[0],newname[1],sex,age,job,bal))

def getName(sex):
    l = open("assets/names/lastnames.txt","r")
    last = l.read().split("\n")
    if sex == "Male":
        f = open("assets/names/malefirstnames.txt","r")
        first = f.read().split("\n")
    else:
        f= open("assets/names/femalefirstnames.txt","r")
        first = f.read().split("\n")
    return [first[random.randrange(len(first)-1)],last[random.randrange(len(last)-1)]]

def listMeeples(option = "all"):
    for i in meeple:
        if  option == "all":
            print(f' name: {i.name} \n Sex: {i.sex}     Age: {i.age}    Occupation: {i.job}     Balance: ${i.inventory["bal"]}   Married to: {i.partner} \n Inventory : {i.inventory}\n')
        elif option == "names":
            print(i.name)
        elif option == "sex":
            print(f'{i.name} is {i.sex}')
        elif option == "age":
            print(f'{i.name} is {i.age}')
        elif option == "job":
            print(f'{i.name} is a {i.job}')
        elif option == "bal":
            print(f'{i.name} has ${i.inventory["bal"]}')
        elif option == "inv":
            print(f'{i.name} inventory: {i.inventory}')
        elif option == "fname":
            print(f' first name is {i.fname}')
        elif option == "lname":
            print(f' {i.fname}s last name is {i.lname}')

generateMeeples(4)
listMeeples("all")
print(len(meeple))
meeple[len(meeple)-1].marry(meeple[len(meeple)-2])
meeple[len(meeple)-1].haveChild(meeple[len(meeple)-2],2)
listMeeples("all")
print(len(meeple))
