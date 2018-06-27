import random, time

class Player:
    def __init__(self,name,hp,strg):
        self.name= name
        if hp < 100:
            self.hp= hp
        else: 
            self.hp= 100
        if strg < (100 - self.hp):
            self.strg= strg
        else: 
            self.strg= 100 - self.hp
            
    
    def attack(self,enemy):
        if self.hp > 0:
            i= random.randint(1,10)
            enemy.hp-= int((self.strg + self.hp)/i)
        print("Resultado ataque:")
        print(self)

    def heal(self):
        i= random.randint(0,25)
        self.hp+= i
        print("Resultado curacion:")
        print(self)

    def __str__(self):
        return(self.name+": "+str(self.hp))

player1= Player("Archer",50,40)
player2= Player("Warrior",70,30)
player3= Player("Mage",40,60)
player4= Player("Paladin",80,20)
player5= Player("Bard",60,35)

'''player1.attack(player2)
player2.attack(player1)'''
print(player1)
print(player2)
while (player1.hp > 0) and (player2.hp > 0):
    player1.attack(player2)
    player2.attack(player1)
    player1.heal()
    player2.heal()
    time.sleep(1)
