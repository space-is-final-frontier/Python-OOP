#A function is just an object with the dunder call method

'''
def test():
    pass

a = test

print(dir(a))
print(dir(test)))
'''

#These two print statement will give the same output as we stored the test object into variable a turning a into an object

#We can place functions as arguemnts for objects

'''
def add(a, b):
    return a + b

class Test:
    def __init__(self, add_func):
        self.add_function = add_func

test = Test(add_func = add)
print(test.add_function(1, 5))'''


#We can place methods as arguments for objects

class Monster:
    def __init__(self, func):
        self.func = func

class Attacks:
    def bite(self):
        print("BITE")

    def strike(self):
        print("STRIKE")

    def slash(self):
        print("SLASH")

    def kick(self):
        print("KICK")

#The following way to implement giving methods as arguments for objects is completely wrong and will give an error when tried to run the given method from the class into which it was given

'''
monster = Monster(func = Attacks.bite)
monster.func()
'''

#This happens cause the Attacks in "Attacks.bite" doesn't return an object but it returns a class, which confuses python

#To fix this, we need to turn this class into an object. To do this, we simple call the class

monster = Monster(func = Attacks().bite)
monster.func()

#This now works and in the "Attacks()" object we will get the "bite" method in "Attacks().bite"

#Another way around this is to just create a separate object and pass the bite method from that object

attacks_object = Attacks()
monster = Monster(func = attacks_object.bite)
monster.func()