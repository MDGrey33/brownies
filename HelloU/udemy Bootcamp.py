"""print('Hello U')
age = 4+5
print(3**3)
my_cat = 'Lona'
print(my_cat)
print(f'{my_cat} is {age}')
division = age/age
print(f'age data type is {type(age)}')
print(f'division data type is {type(division)}')
print('\n\n\n')

print('strings\n')
cat = 'Leonards'
print(f'first letter of the cat is {cat[0]}')
print(f'Last letter of the cat is {cat[-1]}')
print(f'cat has {len(cat)} characters in it')

catFullName = "Leonards Von Burma"
print(catFullName[8:-3])
print(catFullName[3:-3])
print(catFullName[::2])  # 3rd parameter is step size. Output = Load um
print(catFullName[::-1])  # Reverse string

print(cat + ' ' + catFullName)
print((cat + ' ')*5)

x = "Hello cat"
print(x.upper())  # uppercase
print(catFullName.split('a'))

# List are arrays
my_list = ["starring", 1, 2, 3]
print(len(my_list))

print(my_list[1:4])
new_list = my_list + [4, 5]
print(f"zis is {new_list[0].upper()}  {new_list[1:6]}")
new_list.pop()
print(new_list)

cats_list = ["Luna", "Migo", "Leo", "George"]
sorted_list = (sorted(cats_list))
print(f"{cats_list} \n {sorted_list}")
# Dictionaries are lists of key pairs
cat_dic = {'Luna': 'I will thief the hell out of your food',
           'George': 'Move let me sleep',
           'Lona': 'I pee on the toilet seat!, bitch!'}
print(cat_dic['Luna'])
cat_dic['Migo'] = 'I shall take care of you weeklings, I mean you too human!'
print(cat_dic)
cat_dic.pop('Migo')
print(cat_dic)
cat_dic['Migo'] = 'I shall take care of you weaklings, I mean you too human!'
print(cat_dic)
print(cat_dic.keys())
print(cat_dic.values())
# Tuples elements are immutable
my_tuple = (1, 2, 3, 1)
print(my_tuple[-1])
print(my_tuple.count(2))
print(my_tuple.index(1))
# Sets elements are unique
my_set = {"apple", "banana", "cherry"}
print(my_set)
my_set.add("apple")
print(my_set)

# IO file manipulation

# Reading files
my_file = open('resources/my_file.txt')
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
my_file_lines = my_file.readlines()
print(my_file_lines)

# Cleaner way for reading files

with open('resources/my_file.txt') as my_file:
    content = my_file.read()
    print(content)
    my_file.seek(0)
    my_file_lines = my_file.readlines()
    print(my_file_lines)

with open('resources/my_file.txt', mode='r') as my_file:
    content = my_file.read()
    print(content)
    my_file.seek(0)
    my_file_lines = my_file.readlines()
    print(my_file_lines)

# Appending files
with open('resources/my_new_file.txt', mode='a') as my_file:
    my_file.write('\nThis is an appended line that will appear often')

# Writing Files
with open('resources/my_file_lines.txt', mode='w') as my_file:
    my_file.write('I just deleted the old file and made a new one with this text')


# Comparison operators
print('2' == 2)
print('2' != 2)
print(2 <= 2)
print(2 < 2)

print(2 == 2 and 2 > 1)
print(2 == 2 > 1)

# If elif and else statements

if 3 > 2:
    print("it is truly greater")

hungry = False
# hungry = True

if hungry:
    print("Eat something")
else:
    print("It is too early for food")

loc = "Store"

if loc == 'Auto shop':
    print("Cars are cool!")
elif loc == 'Bank':
    print("Money is cool!")
elif loc == 'Store':
    print("Welcome to the store!")
else:
    print("I do not know much!")


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for loop examples
for the_number in my_list:
    print(the_number)

# printing even numbers, if odd multiply by 2 and add to the end of the list to how efficient for is :)
list_sum = 0
for the_number in my_list:
    if the_number % 2 == 0:
        print(the_number)
        list_sum = list_sum + the_number
    else:
        my_list.append(the_number*2)
print(f'the total is {list_sum}')



# Looping through tuples,
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(my_list))

# Printing items from a tuple
for item in my_list:
    print(item)

# unpacking each item in the tuple
for a, b in my_list:
    print(a)
    print(b)


# unpacking a dictionary to find keys with a specific value
d = {'k1': 1, "k2": 2, "k3": 3, 'k4': 2}

for key, value in d.items():
    if value == 2:
        print(key)

# While loop

x = 0
while x < 5:
    print(x)
    x = x + 1
else:
    print("end")

# pass, continue and break

her_name = 'Maija'

print('pass')
for letter in her_name:
    if letter == 'i':
        pass
        print('*')
    print(letter)

print('continue')
for letter in her_name:
    if letter == 'i':
        continue
        print('*')
    print(letter)

print('break')
for letter in her_name:
    if letter == 'i':
        break
        print('*')
    print(letter)

# Range
for num in range(10):
    print(num)
for num in range(0, 10, 2):
    print(num)
print(range(10))
print(list(range(10)))


# Enumerate

for index, letter in enumerate('Maija'):
    print(f'at index {index}, we have the letter {letter} \n')


# Zipping multiple lists/strings into a tuple

for name, color, age in zip(['Georges', 'Luna', 'Migo', 'Lona'],['white', 'gray', 'camouflage', 'black'], [1, 1, 7, 2]):
    print(f"{name}'s color is {color} and they are {age} years old")



# in
print('j' in 'Maija')

my_list = [5, 6, 7, 8, 9, 0, 4, 2, 6, 8]

# min
print(min(my_list))

# max
print(max(my_list))

# sort
my_list.sort()
print('sorted')
for number in my_list:
    print(number)

# shuffle
from random import shuffle
shuffle(my_list)
print('shuffled')
for number in my_list:
    print(number)

# Random number and
from random import randint
# user input
end_of_range = input('enter a number')
# convert string to number
end_of_range = int(end_of_range)
random_number = randint(0, end_of_range)
print(random_number)

# compound to one line
print(randint(0, int(input('enter a number'))))

# Looping through and transforming lists
#convert a strint to a list of its characters and print it
my_list = [letter for letter in "Maija"]
print(my_list)

# make a list out ot a range and print it
my_list = [number for number in range(0,11)]
print(my_list)

# Print even numbers in a range
my_list = [number for number in range(0, 11) if number % 2 == 0]
print(my_list)

# Convert Celsius to fahrenheit and print the fahrenheit values
celcius = [0, 10, 20, 34.5]
fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
for value in fahrenheit:
    print(value)

# Make one list in celsius and fahrenheit and print it formatted
temperatures = zip(celcius, fahrenheit)
print('print formatted')
for c, f in temperatures:
    print(f'{c}\'C, is {f} fahrenheit\n')
print('formatted printed')

# Nested loop in a list comprehension, to be avoided due to lack of readability

# standard expanded double loop
my_list= []
for x in [2, 4, 6]:
    for y in [10, 100, 1000]:
        my_list.append(x * y)
print(my_list)

# now the same in list comprehension
my_list = [x * y for x in [2, 4, 6] for y in [10, 100, 1000]]
print(my_list)
# a bit more extreme
print([x * y for x in [2, 4, 6] for y in [10, 100, 1000]])

for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)


for word in 'Sam print only the words that start with s in this sentence'.split():
    if word[0].lower() == 's':
        print(word)

for number in range(11):
    if number % 2 == 0:
        print(number)

print(list(range(0, 11, 2)))

print(list(range(3, 50, 3)))


range_min = int(input('type the range start '))
range_max = int(input('type the range end '))
divider = int(input('type multiplier '))
for number in range(range_min, (range_max + 1)):
    if number % divider == 0:
        print(number)
# Working with functions


def say_hello_to(name = 'Anonymous'):
    print(f'hello {name}')


say_hello_to('Maija')


def add(num_one = 0, num_two = 0):
    return num_one + num_two


print(add(1, 8))


def return_even_numbers(the_list):
    even_numbers = []
    for number in the_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


my_list = [1, 2, 3, 5, 6, 7]

print(return_even_numbers(my_list))


# unpacking tuples in functions

def get_price(stock_prices, stock_requested):
    for stock, price in stock_prices:
        if stock == stock_requested:
            return price


def get_most_expensive(stock_price_list):
    highyest_price = 0
    for stock, price in stock_price_list:
        if highyest_price < price:
            highyest_price = price
            most_expensive = stock
    return most_expensive, highyest_price


stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]


print(get_price(stock_prices, 'MSFT'))

stock, price = get_most_expensive(stock_prices)
print(f'The most expensive stock is {stock}, it stands at {price}')




from random import shuffle
# Shuffle game

def shuffle_list():
    my_list = ['', 'O', '']
    shuffle(my_list)
    return my_list


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('chose a number 0, 1, or 2')
    else:
        return guess


def check_guess(guess_number):
    result = shuffle_list()
    if result[guess_number] == 'O':
        return 'Good guess', result
    else:
        return 'Better luck next time', result


guess = int(player_guess())
print(check_guess(guess))



# Passing an undefined amount of arguments


def my_func(*args):
    for item in args:
        print(item)


print(my_func(5, 1000, 5, 7))


# passing undefined amount of keyword arguments
def my_new_func(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("I didn't find any fruits here")
    # print(kwargs)


my_new_func(fruit="apple", vegie='carrot')

# Passing Arguments and Keyword arguments


def my_real_func(*args, **kwargs):
#    print(args)
#    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['fruit']))


my_real_func(10, 20, 30, fruit="apple", vegie='carrot')

# exercise print even numbers of an undefined number of Arguments


def myfunc(*args):
    for number in args:
        if number % 2 == 0:
            print(number)


myfunc(5, 6, 7, 8)

# Exercise Lesser of two evens


def lesser_of_two_events(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_events(10, 4))




# Exercise Animal crackers


def animal_crackers( word_list):
    word_list = word_list.lower().split()
    return word_list[0][0] == word_list[1][0]


print(animal_crackers('samir Selim'))


# Makes twenty


def makes_twenty(a, b):
    return a == 20 or b == 20 or a + b == 20


print(makes_twenty(20, 5))

print(makes_twenty(0, 20))

print(makes_twenty(10, 10))

print(makes_twenty(10, 11))


# Capitalize first and 3rd letter


def old_mcdonald(my_text):
    return my_text[:3].capitalize() + my_text[3:].capitalize()


print(old_mcdonald("macdonalds"))




# Master Yoda


def master_yoda(word_list):
    word_list = word_list.split()
    word_list.insert(0, word_list[-1].capitalize())
    word_list[1] = word_list[1].lower()
    # word_list.pop()
    word_list = " ".join(word_list)
    print(word_list)


master_yoda('You must eat')


# Exercise Almost there, returns almost there if within 10 from 100 or 200 with test suite


def almost_there(my_number):
    return abs(100-my_number) <= 10 or abs(200-my_number) <= 10


def test_suite(true_assertions, false_assertions):
    # Defining defaults
    result = "Test failed to run"
    test_count = 0

    # Testing true assertions
    for number in true_assertions:
        if almost_there(number):
            print(f'Test for {number} passed')
            test_count += 1
        else:
            print(f'Test for {number} failed')
            break

    # Testing false assertions.
    for number in false_assertions:
        if not almost_there(number):
            print(f'Test for {number} passed')
            test_count += 1
        else:
            print(f'Test for {number} failed')
            break
    # Validating that all tests ran as expected
    test_count_expected = (len(true_assertions) + len(false_assertions))
    if test_count == test_count_expected:
        print(f'{test_count} / {test_count_expected} passed')
        result = "Test completed successfully"
    print(result)


true_test_cases = (90, 91, 100, 101, 110, 190, 191, 200, 201, 210)
false_test_cases = (89, 111, 189, 211)
test_suite(true_test_cases, false_test_cases)



# has_33 checks if the number 3 comes up twice


def has_33(my_numbers):
    x = '-'
    for this_number in my_numbers:
        # print(x, this_number)
        if this_number == 33 or x == 3 and this_number == 3:
            return True
        x = this_number
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# has_33 another way


def has_33_also(my_numbers):
    for i in range(0, len(my_numbers)-1):
        print(my_numbers[i], my_numbers[i+1])
        if my_numbers[i] == 3 and my_numbers[i+1] == 3 or my_numbers[i] == 33:
            return True
    return False


def has_33_sliced(my_numbers):
    for i in range(0, len(my_numbers)-1):
        print(my_numbers[i], my_numbers[i+1])
        if my_numbers[i:i+2] == [3, 3]:
            return True
    return False

print(has_33_also([1, 3, 3]))
print(has_33_also([1, 3, 1, 3]))
print(has_33_also([3, 1, 3]))
print(has_33_also([33, 1, 3]))




# Paper doll exercise


def paper_doll(text):
    result = ''
    for letter in text:
        result += letter * 3
    return result


print(paper_doll('Maija'))



# Blackjack
# given 3 integers between 1 and 11
# if their sum is less than or equal to 21:
#       return their sum
# if their sum exceeds 21 and there is an 11
#       reduce the total sum by 10
# If the sum after adjustment is still above 21 return Bust
# else return their sum


def print_sum(total):
    print(total)


def check_bust(total):
    if total > 21:
        total = 'Bust!!!'
    print_sum(total)


def adjust(my_cards, total):
    for card in my_cards:
        if card == 11:
            total -= 10
            break
    check_bust(total)


def check(my_cards):
    total = 0
    for number in my_cards:
        total += number
    if total <= 21:
        print_sum(total)
    else:
        adjust(my_cards, total)


# commented to test manual input

check([11, 10, 0])


# Allow the user to manually input the my_cards
# Randomly chose the users cards


# test 1 line evaluation of condition
john = 14
above_age = john >= 18


def store_response(response):
    print(response)


store_response('Allowed') if above_age else store_response('Denied')

# gource -f -960x540 --disable-progress --seconds-per-day 0.01 --auto-skip-seconds 0.1 --stop-on-idle --title Toptal --file-idle-time 0 --hide filenames,dirnames,progress --start-position 0.5 --output-ppm-stream - | ffmpeg -y -r 30 -f image2pipe -vcodec ppm -i - -vcodec libx264 -preset ultrafast -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 ~/Desktop/billing.mp4




def find_the_spy(population):
    code = [0, 0, 7, 'spy']
    for citizen in population:
        if citizen == code[0]:
            code.pop(0)
    return len(code) == 1


def inspect_population(population):
    for city in population:
        print(f'Inspecting {city}')
        if find_the_spy(population[city]):
            print('Spy found')
        else:
            print('No need for suspicion')


population_baltics = {'Riga': [1, 2, 4, 0, 0, 7, 5], 'Tallin': [1, 0, 2, 4, 0, 5, 7], 'Vilnius': [1, 7, 2, 0, 4, 5, 0]}
population_germany = {'Berlin': [1, 2, 4, 0, 0, 7, 5], 'Munich': [1, 0, 2, 4, 0, 5, 7], 'Cologne': [1, 0, 0, 7, 2, 0, 4, 5, 0]}

inspect_population(population_baltics)
inspect_population(population_germany)


# OOP


# class
class BigObject:
    pass


# Instantiate
object1 = BigObject()

print(type(object1))

class PlayerCharacter:
    # Class object attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name
            # Attribute
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')
        return 'done'


player1 = PlayerCharacter('Maija', 22)
player2 = PlayerCharacter('Roland', 33)
player2.attack = 50

player1.shout()
player2.shout()

print(player2.attack)

print(player1)
print(player2.membership)



class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat_one = Cat('Leo', 4)
cat_two = Cat('Luna', 2)
cat_three = Cat('George', 2)


def the_oldest(age_competitors):
    oldest_cat = Cat('anonymous', 0)

    for this_cat in age_competitors:
        if this_cat.age > oldest_cat.age:
            oldest_cat = this_cat
    return oldest_cat


competitors = (cat_one, cat_two, cat_three)
print(f'{the_oldest(competitors).name} is {the_oldest(competitors).age} years old and he is the oldest cat in town')


def square(number):
    return number ** 2


my_numbers = [1, 2, 3, 4, 5, 6]
squared_list = list(map(square, my_numbers))
print(squared_list)


def is_even(number):
    return number % 2 == 0


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(filter(is_even, numbers_list)))

my_numbers = [1, 2, 3, 4, 5]

print(list(map(lambda number: number ** 2, my_numbers)))

print(list(filter(lambda number: number % 2 == 0, my_numbers)))

x = 50


def think_global():
    global x
    print(x)
    x += 1
    print(x)


think_global()
print(x)

# calculate the radius
import math
import string
from curses.ascii import islower, isupper


def vol(rad):
    return 4 / 3 * math.pi * (rad ** 3)


print(vol(2))


# Check number in boundaries


def ran_check(num, low, high):
    return low <= num <= high


print(ran_check(77, 3, 7))


# Count upper case and lowercase


def up_low(text):
    upper = 0
    lower = 0
    for letter in text:
        if isupper(letter):
            upper += 1
        elif islower(letter):
            lower += 1
    print(f'upper {upper} \nlower {lower}')


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

up_low(s)
print(len(s))


# return unique list


def unique_list(lst):
    print(list(set(lst)))


unique_list([1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5])


def multiply(numbers):
    total = 1
    for number in numbers:
        total *= number
    print(total)


multiply(([1, 2, 3, -4]))


# Palindrome


def palindrome(the_sentence):
    return the_sentence.replace(' ', '')[::-1] == the_sentence.replace(' ', '')


sentence = 'nurses run'
sentence = 'helleh'
sentence = 'nurses do run'


print(palindrome(sentence))


# Pangram
import string


def is_pangram(sentence):
    new_sentence = ''
    for letter in ''.join(sorted(set(sentence.lower()))):
        if letter.isalpha():
            new_sentence += letter
    return new_sentence == string.ascii_lowercase


the_sentence = "bbc adefgh ijklmn gooppdqerrsgguvt xry w  z"
the_sentence2 = 'The quick brown fox jumps over a lazy dog!'
the_sentence3 = 'the quick brown fox jumps over a lazy do!'

print(is_pangram(the_sentence2))





# Object-Oriented Programming


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


from colorama import init
from colorama import Fore

init()
print(Fore.RED + 'hello there')
print(Fore.GREEN + 'hello there')


items = [ 1, 2, 3, 4, 5, 6]

print('the elements are:', *items, sep='\n')



# Generators and iterators

def create_cubes(n):
    result = []
    for x in range(n):
        result = yield x**3
    return result


for x in create_cubes(10):
    print(x)


def simple_gen():
    for x in range(300):
        yield x

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
print(next(g))



s = 'hello'

for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))


def generate_squares(upper_limit):
    for x in range(upper_limit):
        yield x**3


list = generate_squares(10)

for number in list:
    print(number)

import random


def random_number(low, high, amount_of_numbers):
    for x in range(amount_of_numbers):
        yield random.randint(low, high)


for number in random_number(1,10,12):
    print(number)


# Counters

from collections import Counter

mylist = [1, 2, 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 7, 8]
print(Counter(mylist))

mylist = "hello you how are you"

c = (Counter(mylist))

print(c.most_common(3))

print(Counter(mylist.split()))

# Default dictionary
from collections import defaultdict

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])
print(d['wrong'])
d = defaultdict(lambda: 404)
print(d['wrong'])

dd = {'a': 10}
dd['b']= 3
print(dd['b'])
print(dd['c'])

# Named Tuple
# Ordinary tuples

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[3])

from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=1, breed='husky', name='Sam')
print(type(sammy))
print(sammy)
print(sammy.age, sammy.breed)

# OS commands test outside virtual environment of pycharm
import os

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))

"""
"""output:

python3 main.py
Path at terminal when executing this file
/Users/roland/code/brownies/HelloU

This file path, relative to os.getcwd()
/Users/roland/code/brownies/HelloU/main.py

This file full path (following symlinks)
/Users/roland/code/brownies/HelloU/main.py

This file directory and name
/Users/roland/code/brownies/HelloU --> main.py

This file directory only
/Users/roland/code/brownies/HelloU"""
"""

# OS work, don't run before you read and research carefully

import shutil
import os

os.listdir('/Users/roland/code/brownies/HelloU/resources/')
"""
"""Output
python3 main.py"""
"""
# Moves a file
shutil.move('./my_file.txt', 'my_file_lines.txt')
# Deletes a folder
shutil.rmtree('./resources/test')
os.listdir('/Users/roland/code/brownies/HelloU/resources/')
# removes a folder if the folder is empty
os.rmdir('./resources/test')
# deletes a file
os.unlink('/Users/roland/code/brownies/HelloU/resource/test/my_file.txt')

# prints a list of folders and subfolders

import os

print(os.getcwd())
directory = os.getcwd()

for folder, sub_folders, files in os.walk(directory):
    print(f'currently looking at {folder}')
    print('\n')
    print('The subfolders are:')
    for sub_folder in sub_folders:
        print(f'Subfolder: {sub_folder}')
    print('\nthe files are:')
    for file in files:
        print(f'\t file: {file}')

# Date and time
import datetime

my_time = datetime.time(2, 22)

print(my_time)
print(my_time.hour)
print(my_time.minute)

today = datetime.date.today()

print(today)
print(today.ctime())

from datetime import datetime
from datetime import date

now = datetime(2021, 10, 3, 14, 20, 1)
print(now)

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
result = date1 - date2
print(result)
print(type(result))
later = datetime(2021, 10, 3, 14, 20, 1)
before = datetime(2020, 10, 3, 4, 20, 1)

diff = later - before

print(diff)
print(diff.seconds)

# math in python
# Numpy is worth looking in for deep math

import math
import random

# help(math)

value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(value))

print(math.pi)

print(math.e)

my_list = range(1, 50)

print(random.choice(my_list))
print(random.sample(population=my_list, k=10))
random.uniform(a=0, b=100)
random.gauss(mu=0, sigma=1)

# debugging
import pdb

x = [1, 2, 3]
y = 2
z = 3

result = y + z
pdb.set_trace()
result2 = x + y

text = "The agent's phone number is Maija Maria Naria 408-555-1234. call phone soon!"

print('phone' in text)

import re

pattern = 'phone'

print(re.search(pattern, text))

pattern = 'Julien'

print(re.search(pattern, text))

pattern = 'phone'

match = re.search(pattern, text)

match

match.span()
match.start()
match.end()

print(re.findall(pattern, text))


for match in re.finditer(pattern, text):
    print(match)
    print(match.group())

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone)
print(phone.group())
phone = re.search(r'\d+-\d+-\d+', text)
print(phone)

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)

phone = re.findall(r'M*a*i*', text)
print(phone)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results.group())
print(results.group(3))

print(re.search(r'cat|dog', 'The cat is here'))
print(re.findall(r'.at', 'the cat in the hat went splat'))

print(re.findall(r'^\d', '1 is a number, where 2 is two'))

print(re.findall(r'\d$', 'you are the number 2'))

phrase = 'There are 3 numbers 34 inside 5 this sentence'

pattern = r'[^\d]'

print(re.findall(pattern, phrase))

# Creating files zipping and unzipping

f = open('file_one.txt', 'w+')
f.write('ONE FILE')
f.close()

f = open('file_two.txt', 'w+')
f.write('TWO FILE')
f.close()

import zipfile

compressed_file = zipfile.ZipFile('compressed_file.zip','w')

compressed_file.write('file_one.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('file_two.txt', compress_type=zipfile.ZIP_DEFLATED)

compressed_file.close()

zip_object = zipfile.ZipFile('compressed_file.zip', 'r')
zip_object.extractall('extracted_content')

import shutil
directory_to_zip = '/Users/roland/code/brownies/HelloU/extracted_content'
output_filename = 'example'

shutil.make_archive(output_filename, 'zip', directory_to_zip)

shutil.unpack_archive('example.zip', 'final_unzip', 'zip')



# More decorators

def my_decorator(func):
    def wrap_function(x):
        print('x'*8)
        func(x)
        print('x' * 8)
    return wrap_function


@my_decorator
def hello(greeting):
    print(greeting, ':)')


hello('hi')

# Parsing JSON from API
import requests
import json

# Cat facts API
response = requests.get("https://catfact.ninja/fact")
# jason_print(response.json())
if response.status_code == 200:
    cat_facts = json.loads(response.content)
    print(cat_facts['fact'])
else:
    print('Something went wrong')
    print(response.status_code)
    print(response)

print('\n')

# Bitcoin price API
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
# jason_print(response.json())
if response.status_code == 200:
    bitcoin_price = json.loads(response.content)
    print(f'bitcoin price on ' + (bitcoin_price['time']['updated']) + ' is ' + str(bitcoin_price['bpi']['EUR']['rate_float']) + ' EUR')
else:
    print('Something went wrong')
    print(response.status_code)
    print(response)

print('\n')

# Agify, genderize and nationalize the name
name = input('write a name and we will tell you their approximate age')

url_age = 'https://api.agify.io?name=' + name
response = requests.get(url_age)
if response.status_code == 200:
    agify = json.loads(response.content)
    print(agify['age'])
else:
    print('Something went wrong')
    print(response.status_code)
    print(response)

url_gender = 'https://api.genderize.io?name=' + name
response = requests.get(url_gender)
if response.status_code == 200:
    genderize = json.loads(response.content)
    print(genderize['gender'])
else:
    print('Something went wrong')
    print(response.status_code)
    print(response)

url_nationality = 'https://api.nationalize.io?name=' + name
response = requests.get(url_nationality)
if response.status_code == 200:
    nationalize = json.loads(response.content)
    for country in nationalize['country']:
        print('Country: ' + country['country_id'] + ' Probability: ' + str(country['probability']))
else:
    print('Something went wrong')
    print(response.status_code)
    print(response)

print('\n')


# API Client

import requests
import json


def jason_print(object):
    text = json.dumps(object, sort_keys=True, indent=4)
    print(text)


# Astronauts in space
response = requests.get('http://api.open-notify.org/astros.json')
# jason_print(response.json())
if response.status_code == 200:
    astronauts_in_space = json.loads(response.content)
    print('The astronauts in space at this point are:')
    for astronaut in astronauts_in_space['people']:
        print(astronaut['name'] + ' traveled in ' + astronaut['craft'])
else:
    print('Something went wrong')
    print(response.status_code)
    print(response)

print('\n')


def print_response(url, parameters):
    response = requests.get(url, params=parameters)
    jason_print(response.json())
    return response


# Data USA population
parameters = {
    'drilldowns': 'Nation',
    'measures': 'Population'
}
url = 'https://datausa.io/api/data'
response = print_response(url, parameters)
population_year = json.loads(response.content)
for year in population_year['data']:
    print(year['ID Year'], ": ", year['Population'])

# Basic API Implementation with Flask

import json
import time
from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    data_set ={'Page': 'Home', 'Message': 'successfully loaded the home page', 'Timestamp': time.time() }
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user')) #/user/?user=usergoeshere
    data_set = {'Page': 'user page', 'Message': f'successfully loaded the profile for {user_query}',  'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run(port=7777)

# Web Scraping
import requests, bs4, lxml

result = requests.get('http://example.com/')
# print(result.text)
soup = bs4.BeautifulSoup(result.text, 'lxml')
# element = soup.select('title')
# element = soup.select('h1')
element = soup.select('title')[0].get_text()
site_paragraphs = soup.select("p")
# print(site_paragraphs[0].getText())

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
# for item in soup.select('.toctext'):
    # print(item.text)
# print(soup.select('.toctext')[i])
# print(text)

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, 'lxml')
images = soup.select('.thumbimage')[0]
# print(images['src'])
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')
# print(image_link.content)
f = open('my_computer_image.png', 'wb')
f.write(image_link.content)
f.close()


# Web Scraping
import requests, bs4, lxml

author_list = set()
quote_list = []
tag_list = set()

for n in range(1, 100):
    print('Scraping page ', n)
    base_url = 'http://quotes.toscrape.com/page/{}/'
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Extract authors
    authors = soup.select('.author')
    for author in authors:
        author_list.add(author.text)

    # Extract Quotes
    quotes = soup.select('.text')
    for quote in quotes:
        quote_list.append(quote.text)

    # Extract tags
    tags_box = soup.select('.col-md-4.tags-box')
    tags = tags_box[0].select('a')
    for tag in tags:
        tag_list.add(tag.text)

    pager = soup.select('.pager')
    next_page = pager[0].select('.next')
    if len(next_page) == 0:
        print(n, ' pages scraped.')
        print(len(author_list), ' authors collected')
        print(len(quote_list), ' quotes collected')
        break


print(quote_list)
print(author_list)
print(tag_list)

# Working with images
from PIL import Image

pencils = Image.open('pencils.jpg')
mac = Image.open('example.jpg')
# print(type(mac))
# mac.show()
print(mac.size)
# print(mac.format_description)

x = 890
y = 850
w = 1140
h = 1202
computer = mac.crop((x, y, w, h))
mac.paste(im=computer, box=(0, 0))

x1 = 0
y1 = 500
w1 = 650
h1 = 1202
pens = pencils.crop((x1, y1, w1, h1))
pens.putalpha(100)
mac.paste(im=pens, box=(0, 850), mask=pens)
blue = Image.open('purple.png')
blue.putalpha(100)
mac.paste(im=blue, box=(890, 850), mask=blue)
mac.show()

# OS Functions 

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))

import csv

# Open csv file
data = open('resources/example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
for line in data_lines:
    print(line)

# pull data out of csv file
all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])

full_name = []
for line in data_lines[1:]:
    full_name.append(line[1] + ' ' + line[2])

# Create a file and store date
file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['1', '2', '3'])
csv_writer.writerows([['1', '2', '3'], ['1', '2', '3']])
file_to_output.close()

# Add a line
f = open('to_save_file.csv', mode='a', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['1', '2', '3'])
file_to_output.close()


# Open and read a page from a pdf file
# Write page one from the file to a new pdf file
import PyPDF2

f = open('resources/Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)

page_one = pdf_reader.getPage(0)

page_one_text = page_one.extractText()

print(page_one_text)
f.close()
f = open('resources/Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfWriter()
print(type(first_page))
pdf_writer.addPage(first_page)
pdf_output = open('Some_Brand_New_doc.pdf', 'wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

# Working with emails
import smtplib
smtp_object = smtplib.SMTP('0.0.0.0', 1025)
print(smtp_object.ehlo())

from_address = 'from@senderdomain.com'
to_address = 'to@receiver.com'
message = 'Subject: this is a test email from pychatm \n hey this is the body of the email'
smtp_object.sendmail(from_address, to_address, message)


# Working with advanced Sets

s = set()
s.add(1)
s.add(2)
s.add(1)
sc = s.copy()
s.add(4)
print(s)
print(sc)
print(s.difference(sc))
set1 = {1, 2, 3}
set2 = {1, 4, 5}
print(set1.difference_update(set2), '\n', set1, '\n', set2)
set2.discard(5)
print(set2)

s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)


s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

print(s1.isdisjoint(s3))
print(s1.issubset(s2))
print(s2.issuperset(s1))

s1 = {1, 2}
s2 = {1, 2, 4}
s1.update(s2)
print(s1, s2)

square_feet = 5
square_meters = square_feet / 10.8
print(f'{square_feet} sq ft is {square_meters:.2f} sq meters')

name = 'Charbel'
greeting = 'Welcome {}'
with_name = greeting.format(name)
print(with_name)

"""