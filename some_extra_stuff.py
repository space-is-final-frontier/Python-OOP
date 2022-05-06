class Monster:

    '''A monster class that would probably never be touched again after this notes file of some extra stuff is finished'''

    #The above comment will be returned when the print the dunder doc method of this class

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

        #Private Attributes
        self._id = 1
        
        #This attribute by convention is not supossed to be changed. This format lets other developers know that this attribute should not be worked on

    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

    #Private Methods
    def _id_return(self):
        return self._id

    #Just like in private attributes the underscore at the front lets other developers know that this method is not supposed to be changed

monster1 = Monster(health = 20, energy = 10)


#hasattr and setattr

#hasattr lets us know if an object has that particular attribute which we passed by returning True or False

'''hasattr(object, 'attribute')'''

print(hasattr(monster1, 'health'))

#setattr creates a new attribute for a particular object

'''setattr(object, 'attribute', value)'''

setattr(monster1, 'weapon', 'Sword')

#This function is the same as " monster1.weapon = 'Sword' ", however unlike this, the setattr function is iterable allowing us to do the following

new_attr = (['weapon', 'Axe'], ['armour', 'Shield'], ['potion', 'Healing'])
for attr, value in new_attr:
    setattr(monster1, attr, value)

#Now when we print the variables of the object monster1 with the vars function, we can see all of the newly added attributes

print(vars(monster1))   #The vars function returns the __dict__ attribute of an object

#Note that the __dict__ is an attribute not a method, this in comparison to other dunder methods becomes an exception.


#doc

#doc is a dunder method that is just there to explain what the object does

print(monster1.__doc__)