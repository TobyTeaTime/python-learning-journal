# %%
class Pokemon:
    def __init__(self, name, type, ID, currHP, maxHP, atk, defense, special, speed):
        self.name = name
        self.type = type
        self.ID = ID
        self.currHP = currHP
        self.maxHp = maxHP
        self.atk = atk
        self.defense = defense
        self.special = special
        self.speed = speed

def attack (self, opponentObj):
    newHP = opponentObj.currHP - self.atk
    if opponentObj.currHP < 0:
        print ("HP must be above zero")
        opponentObj.currHP = 0
    else:
        opponentObj.currHP = newHP

def HP(self):
    HP = self.currHP / self.maxHp
    print("HP: " + str(HP * 100) + "%")

starter = Pokemon("pikachu", "electric", 1, 50, 100, 30, 30, 50, 80)
rival = Pokemon("squirtle", "water", 2, 60, 80, 30, 50, 30, 30)

print(HP(rival))

attack(starter, rival)

print(HP(rival))


#
