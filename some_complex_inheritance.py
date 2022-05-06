#An example of a child class inheriting from two parent classes

'''
class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

class Fish:
    def __init__(self, speed, has_scales):
        self.speed = speed
        self.has_scales = has_scales

    def swim(self):
        print('The fish is swimming')
        print(f'It has a speed of {self.speed}')
'''

'''
class Shark(Monster, Fish):
    def __init__(self, bite_strength):
        self.bite_strength = bite_strength
        super().__init__(???)
        '''

        #Since there are two parent classes, what should be order in which we place the parameters for parent class in super dunder init method?

#Here the topic of mro comes into play
#mro -> method resolution order

'''print(Shark.mro())'''

#Output:
#[<class '__main__.Shark'>, <class '__main__.Monster'>, <class '__main__.Fish'>, <class 'object'>]

#No need on focusing on the "<class 'object'>" statement in the output

#The order in which this output occured is the order in which the parent classes were given to python for the child class

'''
class Fish(Monster, Fish):
    def __init__(self,bite_strength, health, energy):
        self.bite_strength = bite_strength
        super().__init__(health, energy)
        '''

        #This here works on its own without giving any errors

'''
shark1 = Shark(bite_strength = 50, health = 200, energy = 100)
print(shark1.health, shark1.energy, shark1.bite_strength, sep = '\n')
shark1.move(10)
shark1.attack(20)
'''

#But we don't have anything related to the Fish parent class, hence the following code with give an error

'''
shark1 = Shark(bite_strength = 50, health = 200, energy = 100)
print(shark1.speed)
'''

#To fix this, we add "super().__init__() to the Monster class and henceforth all classes that allow to daisy-chain inhertiance amongst multiple parent classes, so that we can go the next init method of the next parent class according to the rmo, without breaking anything in that parent class if it was used as is

'''
class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        super().__init__()
'''

#But we now run into the dilemma that how do we give the arguments of speed and has_scales, which are of the Fish class, from the Shark class when we call "super().__init__", via the Monster class

#To do this we use the keywords arguments or **kwargs in the method parameters of __init__ of monster and henceforth all classes

#When we do this, all of the unnecessary arguments get stored in a dictionary, however for this to happen, we need to give the keywords for each parameter or in other words give named arguments, like 
# "super().__init__(health = health, energy = energy, speed = speed, has_scales = has_scales"

#Now to unpack this dictionary, we again use the **kwargs so that it upacks the dict stored in **kwargs and turns the key-value pairs into named arguments

#Hence the final code would be:

class Monster:
    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)

    def swim(self):
        print('The fish is swimming')
        print(f'It has a speed of {self.speed}')

class Shark(Monster,Fish):
    def __init__(self,bite_strength,health,energy,speed,has_scales):
        self.bite_strength = bite_strength
        super().__init__(health = health, energy = energy, speed = speed, has_scales = has_scales)

shark1 = Shark(
    bite_strength = 50,
    health = 200,
    energy = 55,
    speed = 120, 
    has_scales = False)
 
print(shark1.health, shark1.energy, shark1.speed, shark1.has_scales, sep = '\n')
shark1.attack(20)
shark1.move(50)
shark1.swim()