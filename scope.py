#Local scope problem in functions

'''
def update_health(amount):
    health += amount

health = 10
print(health)
update_health(20)
print(health)
'''

#This however will give an error

#The above problem can be fixed by adding global keyword

'''
def update_health(amount):
    global health
    health += amount
'''

#This in a large code would get messy, so we would use classes which overcome this easily

'''
def update_health(amount):
    monster1.health += amount

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

monster1 = Monster(health = 100, energy = 50)
update_health(20)
print(monster.health)
'''

#We can use methods interchangably between classes to change attributes with no worry of scope

class Monster:
    def __init__(self, health):
        self.health = health

    def get_damage(self, amount):
        self.health -= amount

class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)

monster1 = Monster(health = 100)
hero = Hero(damage = 20, monster = monster1)

hero.attack()
print(monster1.health)