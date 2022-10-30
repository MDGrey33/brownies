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
print(cat_dic['Lona'])
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
"""

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
