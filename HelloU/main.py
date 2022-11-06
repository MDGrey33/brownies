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

"""

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
    print(kwargs)


my_new_func(fruit="apple", vegie='carrot')

# Passing Arguments and Keyword arguments


def my_real_func(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['fruit']))


my_real_func(10, 20, 30, fruit="apple", vegie='carrot')