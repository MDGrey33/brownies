"""print('Hellou U')
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

catFullName = "Leonards Burma"
print(catFullName[8:-3])
print(catFullName[3:-3])
print(catFullName[::2]) # 3rd parameter is step size. Output = Load um
print(catFullName[::-1]) #Reverse string

print(cat + ' ' + catFullName)
print((cat + ' ')*5)

x = "Hello cat"
print(x.upper()) #uppercase
print(catFullName.split('a'))

print('Cats name is {1}'.format(cat, 'Gatto', 'Negro'))
print('\n\n\n')

print('Lists\n')
my_list = [1,2,3,5]
other_list = [1,"String",20.1]
print(my_list)
print(my_list + other_list)
cats_list = ['Leo', 'Luna', 'George', 'Migo']
print(cats_list[1])
cats_list[0] = 'Ljonis'
print(cats_list)
cats_list.append('Muris')
print(cats_list)
new_item = cats_list.pop(2)
print(new_item)

#cats_list.sort()
sort_list = sorted(cats_list)
#sort_list.sort()
print(sort_list)
print(cats_list)

print('\n\n\n')
print('dictionaries') #uses curly braces, dictionaries cant be sorted

cat_colors = {"Leo":"brown",
              "Luna":"tiger",
              "George":"White"}

print(cat_colors["Leo"])
cat_colors["Migo"] = "Also white"
print(cat_colors)
cat_colors.pop("Leo")
print(cat_colors)
print(cat_colors.keys())
print('\n\n\n')

#TUPLES
#similar to lists but cannot be mutable
my_tuple = (1,4,2,7,3,9,4,5) #tuples are defined by regular brackets
my_list = [9,1,5,2,3,4,5]
t=(1,1,2,3,3)
print(t.count(1))
print(t.index(1)) #shows first time element appears
new_tuple = tuple(my_list)
print(new_tuple)
new_list = list(my_tuple)

print(new_tuple)
print(new_list.pop())

# SETS are unique
print(1==2)

myfile = open('myfile.txt')
print(myfile.read())
print(myfile.read()) #does not print because the file is already read and the cursor is at the end

myfile.seek(0) #resets the cursor
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfile.seek(0)

with open('myfile.txt') as my_new_file: #file is opened every time, no need to use seek
    contents = my_new_file.read()
    print(contents)

with open('myfile.txt',mode='r') as myfile: #permission to read file (mode)
    contents = myfile.read()
    print(contents)

with open('my_new_file.txt', mode='a') as f:
    f.write('\nFOUR ON FOURTH')

with open('my_new_file.txt',mode='r') as myfile: # modes: a-append, w-overwrites, r-read
    contents = myfile.read()
    print(contents)
"""
"""
# testing commits form Pycharm
is_magician = True
is_expert = False

if is_magician and is_expert:
    print('You are master magician')

elif is_magician and not is_expert:
    print('At least you\'re getting there')

elif not is_magician:
    print('you need magic powers')

#print('1' is '0')

# FOR LOOPS
for item in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(item, x)

#iterable - list, dict, tuple, set, string
#iterate --> one by one check each item in the collection
user = {
    'name' : 'Golem',
    'age' : 5000
}

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for item in user.items():
    print(item)

for key, value in user.items():
    print(key, value)

#Exercise counter
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in my_list:
    counter += item
print(counter)

#Range - creates range. range(start,stop,step)
for number in range(0,10,2):
    print(number)

#enumerate - gives index and item
for i,char in enumerate('Helllloooo'):
    print(i,char)

for i,char in enumerate(list(range(1,100))):
    if char == 50:
        print(f'index of {char} is: {i}')

# While loop
i = 0
while i<50:
    print(i)
    i += 1
else:
    print('done with all the work')

while i<50:
    print(i)
    break # loop stops when seeing break

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break


#BASICS2

#Conditional logic
is_old = True
is_licenced = True
is_eligible = False


if is_old:
    print('you are old enough to drive')
elif is_licenced:
    print('you can drive now')
else:
    print('checheck')
if is_old and is_licenced and is_eligible:
    print('you can drive')
else:
    print('you cannot drive')
#FUNCTIONS either modifys something or returns something
def say_hello():
    print('Hellloooooo')
# Arguments vs parameters
# parameters are name of the variables function receives
def say_hello(name, emoji):
    print(f'Hellloooooo {name} {emoji}')
# arguments are actual values you pass to the function
say_hello('Leo', ':)')
# keyword arguments
say_hello(emoji=':)', name='Bibi')
# default parameters
def say_hello2(name='Darth Vader', emoji=':O'):
    print(f'Hellloooooo {name} {emoji}')
say_hello2()
say_hello2('Yoda')
# return - automatically exits the function
def summa(num1, num2):
    return num1 + num2
    print('This will not be printed')
print(summa(4,5))
total = summa(10,5)
print(total)
#Exercise TESLA
def checkDriverAge(age = 0):
    if age < 18:
        text = print('Sorry, not old enough to drive')
    elif age > 18:
        text = print('Powering on!')
    elif age == 18:
        text = print('Congratulations on your first year of driving!')
    return text
checkDriverAge(15)
# Methods vs Functions
# methods - a set of instructions that are associated with object
# functions - a set of instructions that perform a task
# Docstrings
def test(a):
'''
#    Info: this function tests and prints param a 
'''
    print(a)
test('blablahblah')
help(test)
print(test.__doc__)
# *args **kwargs
# *args lets you pass any number of arguments
# **kwargs - keyword arguments
def super_func(*args, **kwargs):
    print(kwargs)
    return sum(args) 
print(super_func(1,2,3,4,5, num1=5, num2=10))
#Rule: params, *args, default parameters, **kwargs
'''
#Exercise - return highest even number in the list
def highest_even(li):
    evens = []
    for i in li:
        if i % 2 == 0:
            evens.append(i)
    return max(evens)

print(highest_even([10,2,3,4,5,13]))

# break, continue, pass
# continue - goes back to the start of the loop
# pass - does nothing - passes to the next line. useful as a placeholder

new_list = [1,2,3]
for item in new_list:
    #thinking about it
    pass



#OOP


class PlayerCharacter:
    membership = True # Class Object attribute - static attribute
    def __init__(self, name='anonymous', age=0):
        if (age > 1):
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

"""
# map
def square(n):
    return n ** 2 # n*n (squared)

my_nums = [1,2,3,4,5,6,7,8]
for item in map(square, my_nums):
    print(item)

squared_list = list(map(square, my_nums))
print(squared_list)

