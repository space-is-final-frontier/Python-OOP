#The way of creating a class is simply "class [class name]:"

#We can have atrributes (variables) static by just setting them or we can have them dynamic with the dunder init method.

#Methods are functions specific to a single class

'''
class Monster:
    health = 50
    energy = 100
    
    def attack():
        print("The monster has attacked")
'''

#Creating a monster object from the following class with work but running the attack method will give an error (running "monster1.attack()")

#This is cause python automatically passes a reference to the class as the first argument into this method

#This reference needs to be always caputed within a variable, i.e., There always needs to be atleast one argument to any method in a class

#This variable can be named anything (cause it's a variable, duh!), however by python convention, it is written as self, just like by convention, the class name is written in CamelCase not snake_case

'''
class Monster:
    health = 50
    energy = 100
    
    def attack(self):
        print("The monster has attacked")
'''

#An important thing to note is that when there are more than a single method in a class, both would have self as the first parameter, but they have no relation whatsoever, they are entirely speatarte

#self is highly powerful, cause if we imagined the class as the global scope, then the attributes health and energy would be global "variables". This would also make the methods in a class as functions, so any change we would try to do to the attributes wouldn't work cause we would be creating a local variable which wouldn't work with the gloabal one

'''
class Monster:
    health = 50
    energy = 100
    
    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage was dealt')
        self.energy -= 20
        print(self.energy)'''

#Duner Method (Double underscore methods)
#These methods are not specifically called by the user in a "Monster1.attack()" fashion, instead it called by python when something happens, like __init__ is called when an object is created, __len__ is called when the object is passed into the len()

#Since the self.[attribute] = [attribute] refers to that class only, there is no need to write the attributes in static first, we can immediably write def __init__(self, attribute): \n self.attribute = attribute and have it work just fine

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
        
#We can place the parameters as is or as named arguments
monster1 = Monster(40, 50)
monster2 = Monster(health = 100, energy = 80)

#We can use dir() and pass in an object and get a list of all of the inbuilt dunder methods, attributes and methods

print(dir(monster1))