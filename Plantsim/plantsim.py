import random

users = []
plantowners = {
"cat person":
}

class User:
    def __init__(self,name,balance):
        self.name = name,
        self.balance  = balance
        self.plants = []
        self.inventory = {
        "seeds":10
        }
    def mintPlant(self,speciesname):
        name = SpeciesGenerator(speciesname)
        serial = len(self.plants)+1
        gt = round(random.normalVariate(120,30))
        hy = random.normalVariate(3,1)
        properties = generatePlantProperties()
class Plant:
    def __init__(self,name,serial,growTime,hy,parents=False):
        self.name = name
        self.serial = serial
        if parent:
            self.parents = parent
        self.children = []
        self.age = 0
        self.generation = 0;
        self.properties ={
            "type":type,
            "Leaf Shape": leafshape,
            "Leaf Size": leafsize,
            "color":color,
            "size":size,
            "Grow Time" :growTime,
            "Harvest Yield":hy,
            "zone": zone
        }
def speciesGenerator(customname):
    return customname
def generatePlantProperties():
    
def list(arg):
    if arg == "users":
        for i in users:
            print(i.name)
    if arg == "all":
        for u in users:
            for p in u.plants:
                if u.name not in plantowners:
                    update(plantowners[u.name],[p])
                else:
                    plantowners[u.name].append(p)
        for p in plantowners.keys():
            print(f'{p} owns:')
            for k in plantowners[p]:
                print(k.name)

def newu(name,balance):
    users.append(User(name,balance))

newu("tim",20)
