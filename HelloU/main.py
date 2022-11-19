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

"""
my_numbers = [1, 2, 3, 4, 5]

print(list(map(lambda number: number ** 2, my_numbers)))

