#An example of simple inheritance with static attributes

'''
class Monster:
    health = 50
    energy = 100

    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} of damage was done')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved!')
        print(f'The monster moved with {speed} speed')

class Shark(Monster):
    def __init__(self, speed):
        self.speed = speed

    def bite(self):
        print('The shark has bitten something')

    def move(self):
        print('The shark has moved!')
        print(f'The shark moved with speed {self.speed}')


shark1 = Shark(speed = 120)
print(shark1.health, shark1.energy, shark1.speed, sep = '\n')
shark1.attack(20)
shark1.bite()
shark1.move()
'''


#Now, there are two ways to implement dynamic attributes from parent class, one is an outdated methord and one is a newer better methord

'''
class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        
    ...

'''
    

#Older Methord

'''

...
class Shark(Monster):
    def __init__(self, speed, health, energy):
        Monster.__init__(self, health, energy)
        self.speed = speed
        
    ...
    
shark1 = Shark(speed = 120, health = 80, energy = 240)
print(shark1.health, shark1.energy, shark1.speed, sep = '\n')
shark1.attack(20)
shark1.bite()
shark1.move()
'''

#In this the self parameter in the Monster.__init__() refers to the self in __init__ method of the child Shark class, not the parent Monster class


# Newer Methord

'''
class Shark(Monster):
    def __init__(self, speed, health, energy):
        super().__init__(health, energy)
        self.speed = speed
        
    ...
    
shark1 = Shark(speed = 120, health = 80, energy = 240)
print(shark1.health, shark1.energy, shark1.speed, sep = '\n')
shark1.attack(20)
shark1.bite()
shark1.move()
'''

#This is a much easier way to implement dynamic attributes from parent class as we don't have to get confused with the self parameter

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} of damage was done')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved!')
        print(f'The monster moved with {speed} speed')

class Shark(Monster):
    def __init__(self, speed, health, energy):
        super().__init__(health, energy)
        self.speed = speed

    def bite(self):
        print('The shark has bitten something')

    def move(self):
        print('The shark has moved!')
        print(f'The shark moved with speed {self.speed}')

shark1 = Shark(speed = 120, health = 80, energy = 240)
print(shark1.health, shark1.energy, shark1.speed, sep = '\n')
shark1.attack(20)
shark1.bite()
shark1.move()