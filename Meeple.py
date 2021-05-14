class Meeple:
    def __init__(self,firstname,lastname,sex,age,job,bal):
        self.fname = firstname
        self.lname = lastname
        self.name = firstname+" "+lastname
        self.sex = sex
        self.age = age
        self.job = job
        self.married = False
        self.parents = []
        self.siblings = []
        self.children = []
        self.partner = []
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
                other.partner = self.name
                self.married = True
                other.married = True

            else:
                self.lname = other.lname
                other.partner = self.name
                updatenames(meeple)
                self.partner = other.name
                other.partner = self.name
                self.married = True
                other.married = True

    def haveChild(self,other,children):
        if self.married :
            for item in range(children):
                if random.randrange(2) == 1:
                    sex = "Male"
                else:
                    sex = "Female"
                self.children.append(Meeple(getName(sex)[0],self.lname,sex,0,"unemployed",0))
                other.children = self.children
            for child in self.children:
                meeple.append(child)
                child.parents = [self,other]
                for otherchild in self.children:
                    if child!=otherchild:
                        child.siblings.append(otherchild)

        else:
            marry(self,other)
            haveChild(self,other,children)

    def getRelativeNames(self,op):
        names = []
        if op == "children":
            relative = self.children
        elif op == "parents":
            relative = self.parents
        elif op == "siblings":
            relative = self.siblings
        for i in relative:
            names.append(i.name)
        return names
