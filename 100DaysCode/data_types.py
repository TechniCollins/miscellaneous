#Getting the data type 
x = 5
print(type(x))

#Setting the data type
#Data types in python are set by default when variables are assigned values
x = "Hello world"

#Setting the specific data type
x = str("Hello World")

#Numeric Types
#int - a whole number, positive or negative of unlimited length -W3Schools
#float - a number, negative or positive containing at least one decimal
#Complex - written with j as the imaginary part

my_int = 439483395038
my_float = 47.89
my_other_float = 12e-4 #e indicates the power of 10
my_complex = 7j

#type conversion
print(int(my_float))

#Random Number

import random
print(random.randrange(1, 3))

#Sequence types
#list - ordered and changeable
my_list = ['item', 'another item', 'still an item']
print(my_list)
print(my_list[1])#print 2nd item
print(my_list[-1])#print the last item
print(my_list[0:2])#print range - returns a new list, index 2 not included

#changing an item
my_list[0] = 'changed item'
print(my_list)

#Loop through a list
for item in my_list:
	print(item)

#check if item exists
if 'another item' in my_list:
	print("another item exists")

#determine length of list
print(len(my_list))

#adding items
my_list.append('even more items')
print(my_list)
my_list.insert(1, 'item item')
print(my_list)

#remove items
my_list.remove('still an item')
print(my_list)

#pop() removes the specified index or the last element if no argument is passed
my_list.pop()
print(my_list)

#del deletes the mentioned index or the entire list if not specified
del my_list[1]
print(my_list)

#clear() clears the list
my_list.clear()
print(my_list)

#How to make a copy of a list
my_other_list = my_list.copy()
my_other_list.append('New list, new item')
print(my_list)
print(my_other_list)

my_list.append('Old list, old item')

#Joining lists
joined_list = my_list + my_other_list
print(joined_list)

#You can use list() to make a new list
my_brothers_list = list(('item1', 'item2', 'item3'))
print(my_brothers_list)

#Tuple - ordered and unchangeable
my_tuple = ('tuple_item1', 'tuple_item2', 'tuple_item3')
print(my_tuple)
#Operations on a tuple are the same as that in a list, except where changing is involved

#Sets - unordered 
my_set = {'set item 1', 'set item 2', 'set item 3'}
print(my_set)

#You cannot change items, but you can add new ones
my_set.add('new set item')
print(my_set)

my_set.update(['another set item', 'set item item'])
print(my_set)

#removing an item
my_set.remove('set item item')
#OR
my_set.discard('another set item')

print(my_set)

#Dictionaries -unordered, changeable, indexed
my_dict = {
	'first':'item1',
	'second':'item2',
	'third':'item3',
}

print(my_dict)

print(my_dict['second'])

#change an item
my_dict['second'] = 'ario'
print(my_dict)

for item in my_dict:
	print(item)#print key
	print(my_dict[item])#print values

#Adding items
my_dict['fourth'] = 'item 4'
print(my_dict)

#making a dictionary using constructor
my_other_dict = dict(first = 'first item', second = 'second item', third = 'third item')
print(my_other_dict)

#boolean
print(10 > 9)
print('first' in my_other_dict)

print(bool(my_other_dict))