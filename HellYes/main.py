# OOP


class PlayerCharacter:
    membership = True  # Class Object attribute - static attribute

    def __init__(self, name='anonymous', age=0):
        if age > 1:
            self.name = name
            self.age = age

    def run(self):
        print('run')
        return 'Done'

    def shout(self):
        print(f'My name is {self.name}')


player1 = PlayerCharacter('Luna', 3)
player2 = PlayerCharacter('George', 2.5)

print(player1.name, player1.age)
player1.run()

player2.attack = 50

print(player2.attack)
player1.shout()


# EXERCISE Cats
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# instantiate 3 cats
Leo = Cat("Leo", 4)
Luna = Cat("Luna", 3)
George = Cat("George", 3)


# create a function that finds the oldest cat
def oldest(cats):
    oldest_cat = Cat('anonymous', 0)

    for this_cat in cats:
        if this_cat.age > oldest_cat.age:
            oldest_cat = this_cat
    return oldest_cat.name


competitors = (Leo, Luna, George)
print(oldest(competitors))
