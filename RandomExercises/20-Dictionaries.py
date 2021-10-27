import operator
import collections
import ast
from itertools import product
from heapq import nlargest
from collections import Counter
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

print(strng_to_dict('w3resource'))