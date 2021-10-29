import operator
import collections
import ast
from itertools import product
from heapq import nlargest
from collections import Counter, ChainMap
from functools import reduce
# eng2sp = {"one": "uno", "two": "dos", "three": "tres"}

# for k in eng2sp:
#     print("Got key", k, "which maps to value", eng2sp[k])

# print(list(eng2sp.values())[1:])

# alreadyknown = {0: 0, 1: 1}

# def fib(n):
#     if n not in alreadyknown:
#         new_value = fib(n-1) + fib(n-2)
#         alreadyknown[n] = new_value
#         # print(alreadyknown)
#     return alreadyknown[n] 

# print(fib(10))

# letter_counts = {}

# for letter in 'Mississippi':
#     letter_counts[letter] = letter_counts.get(letter, 0) + 1

# print(letter_counts)

# def letter_counter(strng):
#     lower_string = strng.lower()
#     letter_counts = {}
#     for letter in lower_string:
#         letter_counts[letter] = letter_counts.get(letter, 0) + 1

#     letter_items = list(letter_counts.items())
#     letter_items.sort()

#     # for pair in letter_items:
#     #     print(f'{pair}\n')

#     return letter_items 
    

# print(letter_counter('ThiS is String with Upper and lower case Letters'))



def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = quantity
    return inventory
            
# new_inventory = {}
# add_fruit(new_inventory, "strawberries", 10)
# # print("strawberries" in new_inventory)
# # print(new_inventory["strawberries"] == 10)
# add_fruit(new_inventory, "strawberries", 25)
# print(new_inventory["strawberries"] == 35)

#################################### EXERCISES ##################################
def sort_dict(dictionary, order):
    """ orders dict based on values, 1 for ascending and -1 for descending"""
    if order == 1:
        ascending = sorted(dictionary.items(), key=operator.itemgetter(1))
        ascending = dict(ascending)
        return ascending
    if order == -1:    
        descending = sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True)
        descending = dict(descending)
        return descending
    if order not in [1, -1]:
        return 'Please enter a value that is either 1 or -1'
    


# fruits = {'banana': 20, 'orange':30, 'papaya': 12, 'apple': 3}
# print(sort_dict(fruits, 3))

def add_to_dict(d, key, value):
    d[key] = value
    return d 

# d = {0: 10, 1:20}
# print(add_to_dict(d,2,30))

def add_3_dicts(d_list):
    # final_dict = d1 | d2 | d3 # only possible in python 3.9 and above
    # final_dict = {}
    # for d in [d1,d2,d3]:
    #     final_dict.update(d)
    # return final_dict
    super_dict = collections.defaultdict(list)
    for d in d_list:
        for k, v in d.items():
            super_dict[k].append(v)

    return super_dict


# print(add_3_dicts([{1:10, 2:20}, {3:30, 4:40}, {5:50,6:60}]))

def generate_dict(n):
    d = {}
    for num in range(1, n+1):
        d[num] = num*num
    return d

# print(generate_dict(5))

def add_dict_values(d):
    return sum(d.values())

# print(add_dict_values({'test':1, 'test1':3, 'test2':8}))

def multiply_values(d):
    result = 1
    for val in d.values():
        result = result * val
    return result

# print(multiply_values({'test':1, 'test1':3, 'test2': 4, 'test3': 2}))

def transform_list(l1,l2):
    keys = l1
    values = l2
    return dict(zip(keys,values))

# print(transform_list([1,2,3],[4,5,6]))

# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}

def sorted_dict_key(d):
    a = {}
    for key in sorted(d):
        a.update({key: d[key]})
    return a

# print(sorted_dict_key(color_dict))

def max_min_dict_value(d, choice):
    """ returns max or min value of the dictionary provided, choice must be max or min"""
    if choice.lower() == 'max':
        return max(d.values())
    if choice.lower() == 'min':
        return min(d.values())
    else:
        return 'Please enter max or min in string form'
        

# print(max_min_dict_value({'x':500, 'y':5874, 'z': 560}, 'maxx'))

def remove_dups(d):
    results = {}

    for key,value in d.items():
        if value not in results.values():
            results[key] = value

    return results

# student_data = {'id1': 
#    {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id2': 
#   {'name': ['David'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id3': 
#     {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id4': 
#    {'name': ['Surya'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
# }

# print(remove_dups(student_data))

def add_common_values(d1,d2):
    d = collections.Counter(d1) + collections.Counter(d2)
    return d

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

# print(add_common_values(d1,d2))

def unique_values(d):
    # return set(dic for item in d for dic in item.values())
    results = []
    for item in d:
        for dic in item.values():
            results.append(dic)

    return set(results)

# print(unique_values([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))

def all_combos(d):
    results = []
    for x,y in product(*d.values()):
        results.append(x+y)

    return results

# a = {'1':['a','b'], '2':['c','d']}
# print(all_combos(a))

def highest_3(d):
    return nlargest(3,d,key=d.get)

# print(highest_3({'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}))

def strng_to_dict(strng):
    d = {}
    for letter in strng:
        d[letter] = d.get(letter, 0) + 1
    return d

# print(strng_to_dict('w3resource'))

# d = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

# for row in zip(*([key] + (value) for key, value in sorted(d.items()))):
#     print(*row)

# def count_values(L):
#     super_dict = collections.defaultdict(list)
#     for d in L:
#         for k, v in d.items():
#             super_dict[k].append(v)

#     for value in super_dict.items():
#         print(sum(value[1]))

#     return type(super_dict)

# L = [
#     {'id': 1, 'success': True, 'name': 'Lary'},
#     {'id': 2, 'success': False, 'name': 'Rabi'},
#     {'id': 3, 'success': True, 'name': 'Alex'}
# ]

# print(count_values(L))

def sorted_list_in_dict(d):
    sorted_dict = {x: sorted(y) for x, y in d.items()}
    return sorted_dict


# print(sorted_list_in_dict({'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}))

def replace_blank_spaces(d):
    d = {k.replace(' ', ''): v for k,v in d.items()}
    return d

# print(replace_blank_spaces({'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}))


def get_key_value_count(d):
    print('Key Value Count')
    for i, (key,value) in enumerate(d.items(),1):
        print(f'{key}    {value}    {i}')

    return 'Success'

# get_key_value_count({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})

# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}

# for x in students:
#     print(x)
#     for y in students[x]:
#         print(y, ':', students[x][y])


def count_items_in_list_in_dict(d):
    return sum(map(len,d.values()))

# print(count_items_in_list_in_dict({'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}))

# x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
# print(x.most_common())


def create_dict_from_2lists(l1, l2):
    super_dict = collections.defaultdict(set)
    for c, i in zip(l1,l2):
        super_dict[c].add(i)
            
    return super_dict

# print(create_dict_from_2lists(['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]))


def sum_of_average(l):
    for d in l:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        num = round((n1 + n2) / 2)
        d['V + VI'] = num

    return l

# print(sum_of_average([
#   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ])) 

# d = {"students":[{"firstName": "Nikki", "lastName": "Roysden"},
#                {"firstName": "Mervin", "lastName": "Friedland"},
#                {"firstName": "Aron ", "lastName": "Wilkins"}],
# "teachers":[{"firstName": "Amberly", "lastName": "Calico"},
#          {"firstName": "Regine", "lastName": "Agtarap"}]}
# print("Original dictionary:")
# print(d)
# print(type(d))
# import json
 
# with open("dictionary", "w") as f:
#    json.dump(d, f, indent = 4, sort_keys = True)
 
# print("\nJson file to dictionary:")
# with open('dictionary') as f:
#  data = json.load(f)
# print(data)

dict_nums = dict(x=list(range(11,20)),y=list(range(21,30)),z=list(range(31,40)))
print(dict_nums['x'][4]) 

def dict_list_generator(x,y,z):
    x = dict(x=list(range(11,20)))
    y = dict(y=list(range(21,30)))
    z = dict(z=list(range(31,40)))

    return x | y | z

print(dict_list_generator('x','y','z'))

