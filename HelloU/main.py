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
"""


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



