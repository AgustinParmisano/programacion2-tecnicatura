import datetime

class User:
    def __init__(self,fn,dob):
        self.fullname= fn
        self.date_of_birth= dob
    
    def salutte(self):
        print("Hello I'am {}. Nice to meet you!".format(self.fullname))

    def age(self):
        yearnow = datetime.datetime.now().year
        userage = yearnow - self.date_of_birth.year
        return userage
    
    def name(self):
        username= self.fullname.split(", ")[-1]
        return username

    def lastname(self):
        userln= self.fullname.split(", ")[0]
        return userln

fechanac = datetime.datetime(1980, 2, 4, 0, 0)
fechanac1 = datetime.datetime(1985, 5, 23, 0, 0)
fechanac2 = datetime.datetime(1983, 11, 27, 0, 0)

users = []

mauro = User("Francois, Mauro",fechanac)
marcos = User("Di Lauro, Marcos",fechanac1)
fran = User("Landivar, Francisco Javier",fechanac2) 


users.append(mauro)
users.append(marcos)
users.append(fran)
#print(help(mauro))

for u in users:
    u.salutte()
    print(u.age())
    print(u.name())
    print(u.lastname())


