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


my_file = open('myfile.txt')
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
my_file_lines = my_file.readlines()
print(my_file_lines)"""

with open('myfile.txt') as my_file:
    content = my_file.read()
    # print(content)
    my_file.seek(0)
    my_file_lines = my_file.readlines()
    # print(my_file_lines)

with open('myfile.txt', mode='w') as my_file:
    content = my_file.read()
    print(content)
    my_file.seek(0)
    my_file_lines = my_file.readlines()
    print(my_file_lines)
