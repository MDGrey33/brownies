"""# Object-Oriented Programming


class Dog():
    # Class object attributes
    # Same in any instance of the class
    species = 'mammal'

    def __init__(self, breed, name, spots, language):
        # attributes
        # We take in the argument
        # Assign it using the self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots
        self.language = language

    # Methods, functions inside a file, operations/actions
    def bark(self, times):
        bark_language = {'English': 'Wuf', 'Russian': 'Gav', 'Latvian': 'Vau'}
        if self.language in bark_language:
            print(bark_language[self.language] * times)


my_dog = Dog('lab', 'sam', False, 'English')

print(my_dog.name, my_dog.breed, my_dog.spots)

your_dog = Dog(breed='german Shephard', name='Rockey', spots=False, language='Russian')

print(your_dog.name, your_dog.breed, your_dog.spots)

my_dog.bark(3)
your_dog.bark(33333)



class Circle():
    # class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(radius=30)
print(my_circle.pi)
print(my_circle.get_circumference())
print(my_circle.area)

class Animal():

    def __init__(self):
        print("Animal created")

    def who_are_you(self):
        return "I am an animal, a party animal"

    def eat(self):
        return 'Numunum num num num num num numunum https://youtu.be/vP9r6UjCA7I'


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_are_you(self):
        return "I am an dog,https://youtu.be/Qkuu0Lwb5EM"

    def bark(self):
        return "Wuf!"


my_animal = Animal()
print(my_animal.who_are_you())
print(my_animal.eat())

my_dog = Dog()
print(my_dog.eat())
print(my_dog.who_are_you())
print(my_dog.bark())



class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"I am {self.name} and I say Woof!"


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"I am {self.name} and I say Miaw!"


rocky = Dog('Rocky')
print(rocky.speak())

lona = Cat('Lona')
print(lona.speak())


for pet in [rocky, lona]:

    print(type(pet))
    print(pet.speak())





class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('subclass must implement this abstract method')


class Dog(Animal):

    def speak(self):
        return self.name + ' says Woof'


class Cat(Animal):

    def speak(self):
        return self.name + ' says Miaw'


fred = Dog('Fred')
print(fred.speak())

luna = Cat('Luna')
print(luna.speak())


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f'{self.title} book object has been deleted')


b = Book('Python rocks', 'Jose Muhika', 200)

print(b)
print(len(b))
del b
print(b)

# Distance and slope of a line
import math


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.dist(self.coor1, self.coor2)

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())


import math


class Cylinder:

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi*pow(self.radius, 2)*self.height

    def surfa_area(self):
        return 2 * math.pi * pow(self.radius, 2) + self.height * self.radius * 2 * math.pi


c = Cylinder(2, 3)
print(c.volume())
print(c.surfa_area())


import string
import random


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Welcome {self.owner},\nyour balance is {self.balance}."

    def deposit(self, amount):
        if amount < 1000:
            self.balance = self.balance + amount
        else:
            return f'{self.owner} unless you provide the following information, we will assume you are funding terrorism and close your bank account\n{string.ascii_lowercase*5} \nyou got 5 minutes Bitch!'


    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance - amount
        else:
            return f'Fund unavailable!'

acct1 = Account('Maija', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
print(acct1.deposit(2000))
print(acct1.withdraw(75))
print(acct1.withdraw(500))
# Fund unavailable

"""

class Character:
    def __init__(self, name, species, craft):
        self.name = name
        self.species = species
        self.craft = craft

    def shout(self):
        return "waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    @classmethod
    def run(cls, coordinates, steps):
        return coordinates + steps


