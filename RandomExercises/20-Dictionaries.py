import operator
import collections
import ast
from itertools import product
from heapq import nlargest
from collections import Counter, ChainMap
from functools import reduce
from operator import getitem
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
    
# print(sort_dict({'banana': 20, 'orange':30, 'papaya': 12, 'apple': 3}, 3))

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

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}

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

# dict_nums = dict(x=list(range(11,20)),y=list(range(21,30)),z=list(range(31,40)))
# print(dict_nums['x'][4]) 

def dict_list_generator(x,y,z):
    x = dict(x=list(range(11,20)))
    y = dict(y=list(range(21,30)))
    z = dict(z=list(range(31,40)))

    return x | y | z

# test = dict_list_generator('x','y','z')
# print(test)
# print(test['x'][4])

def drop_empty_items(d):
    # for key, value in list(d.items()):
    #     if value == None or '':
    #         d.pop(key)
    # return d
    return { k : v for k,v in d.items() if v is not None} #makes copy and returns new dict
        

# print(drop_empty_items({'c1': 'Red', 'c2': 'Green', 'c3': None}))

def filter_based_on_value(d):
    return { k: v for k,v in d.items() if v < 170}

# print(filter_based_on_value({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}))

def convert_list_to_nested_dict(l1,l2,l3):
    return [{x: {y: z}} for (x,y,z) in zip(l1,l2,l3)]

# l1 = ['S001', 'S002', 'S003', 'S004']
# l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# l3 = [85, 98, 89, 92]

# print(convert_list_to_nested_dict(l1,l2,l3))

def filter_based_on_ht_wt(d,operator,ht,wt):
    if operator.lower() == 'less':
        return { k: v for k,v in d.items() if v < (ht, wt)}
    if operator.lower() == 'greater':
        return { k: v for k,v in d.items() if v > (ht, wt)}
    return 'please change operator to "less" or "greater" only'

# print(filter_based_on_ht_wt({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}, 'less' , 6, 70))

def check_same_values(d, num):
    result = all(val == num for val in d.values())
    return result

# print(check_same_values({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 13}, 10))

def group_seq_of_kvp_into_dict(li):
    d = {}
    for k,v in li:
        d.setdefault(k,[]).append(v)

    return d

# print(group_seq_of_kvp_into_dict([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]))

def dict_of_lists_to_lists_of_dict(d):
    v = [dict(zip(d,t)) for t in zip(*d.values())]
    return v    

# print(dict_of_lists_to_lists_of_dict({'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}))

def remove_dict_from_list(l,remove):
    for d in l:
        for idx,v in enumerate(d.values()):
            # print(k)
            if v == remove:
                l.pop(idx)
    return l

# print(remove_dict_from_list([{'id': '#FF0000', 'color': 'Red'},
#                             {'id': '#800000', 'color': 'Maroon'}, 
#                             {'id': '#FFFF00', 'color': 'Yellow'}, 
#                             {'id': '#808000', 'color': 'Olive'}],'#FF0000'))

                
def remove_dict_from_list2(colors,r_id):
    colors[:] = [d for d in colors if d.get('id') != r_id]
    return colors

# print(remove_dict_from_list2([{'id': '#FF0000', 'color': 'Red'},
#                             {'id': '#800000', 'color': 'Maroon'}, 
#                             {'id': '#FFFF00', 'color': 'Yellow'}, 
#                             {'id': '#808000', 'color': 'Olive'}],'#FF0000'))


def turn_string_into(dict_list, strng):
    if strng.lower() == 'int':
        for d in dict_list:
            for k,v in d.items():
                d[k] = int(v)
        return dict_list

    if strng.lower() == 'float':
        for d in dict_list:
            for k,v in d.items():
                d[k] = float(v) 
        return dict_list

# print(turn_string_into([{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}], 'float'))

# def convert_to_int(lst):
#     result = [dict([a, int(x)] for a, x in b.items()) for b in lst]
#     return result

# def convert_to_float(lst):
#     result = [dict([a, float(x)] for a, x in b.items()) for b in lst]
#     return result

def clear_list_in_dict(d):
    return {k:[v.clear()] for k,v in d.items() if len(v) != 0}

# print(clear_list_in_dict({'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}))

def extract_list_from_list_dict(l, subject):
    result = [d[subject] for d in l if subject in d]

    return result
    # subject = subject.capitalize()
    # new_list = []
    # for d in l:
    #     nums = d.get(subject)
    #     new_list.append(nums)
    # return new_list

# print(extract_list_from_list_dict([{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}], 'Science'))

def length_given_dict_values(d):
    new_dict = {}
    for k,v in d.items():
        # new_dict.update({v: len(v)})
        new_dict[v] = len(v)
    return new_dict

# print(length_given_dict_values({1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}))

def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0

# print(dict_depth({'a':1, 'b': {'c': {'d': {}}}}))

def dict_to_list_of_lists(d):
    new_list = []
    for k,v in d.items():
        new_list.append([k,v])

    return new_list

# print(dict_to_list_of_lists({1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}))

def filter_even(d):
    result = {key: [idx for idx in val if not idx % 2]  
          for key, val in d.items()}   
    return result

# print(filter_even({'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}))

def shortest_list_of_values(d):
    min_value = 1
    return [k for k,v in d.items() if len(v) == min_value]

# print(shortest_list_of_values({'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}))

def count_frequency_of_values(d):
    return collections.Counter(d.values())

# print(count_frequency_of_values({'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}))

def extract_value_into_list(l):
    return [list(d.values()) for d in l]

# print(extract_value_into_list([{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]))

def list_of_lists_to_dict(l):
    # keys = []
    # values = []
    # for idx,li in enumerate(l):
    #     keys.append(li[0])
    #     values.append(li[1:])
    # return dict(zip(keys,values))
    result = {item[0]: item[1:] for item in l}
    return result
    

# print(list_of_lists_to_dict([[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]))

def key_list_pairings(d):
    result = [dict(zip(d, sub)) for sub in product(*d.values())]
    return result

# print(key_list_pairings({1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}))

def total_length_values(d):
    return sum(list(len(v) for v in d.values()))

# print(total_length_values({'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}))

def invert_dict(d):
    super_dict = collections.defaultdict(list)

    for k,v in d.items():
        super_dict[v].append(k)

    return dict(super_dict)

# print(invert_dict({
#   'Ora Mckinney': 8,
#   'Theodore Hollandl': 7,
#   'Mae Fleming': 7,
#   'Mathew Gilbert': 8,
#   'Ivan Little': 7,  
# }))

def combine_dict_values_to_list(d1,d2):
    super_dict = collections.defaultdict(list)
    for d in [d1,d2]:
        for k,v in d.items():
            super_dict[k].append(v)

    return dict(super_dict)

# print(combine_dict_values_to_list({'w': 50, 'x': 100, 'y': 'Green', 'z': 400}, {'x': 300, 'y': 'Red', 'z': 600}))

def no_idea_name(l, fn):
    return dict(zip(l, map(fn,l)))

# print(no_idea_name([1, 2, 3, 4], lambda x: x*x))

def list_of_corresponding_values(l, selector):
    selector = selector.lower()
    return list(d.get(selector) for d in l)

# print(list_of_corresponding_values([{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}],'age'))

def no_idea_name_2(d, fn):
    return dict((k, fn(v)) for k,v in d.items())

# print(no_idea_name_2({
#   'Theodore': { 'user': 'Theodore', 'age': 45 },
#   'Roxanne': { 'user': 'Roxanne', 'age': 15 },
#   'Mathew': { 'user': 'Mathew', 'age': 21 },
# }, lambda u : u['age']))

def find_keys_specified_value(d, selector):
    return [k for k,v in d.items() if selector == v]

# print(find_keys_specified_value({'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}, 20))

def lists_to_dict(l1,l2):
    keys = l1
    values = l2

    return dict(zip(keys,values))

# print(lists_to_dict(['a', 'b', 'c', 'd', 'e', 'f'],[1, 2, 3, 4, 5]))

def dict_to_tuples(d):
    return [(k,v) for k,v in d.items()]

# print(dict_to_tuples({'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}))

def flat_list_of_keys(d):
    return list(d.keys())

# print(flat_list_of_keys({'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}))

def max_min_of_values(d):
    return max(d, key = d.get), min(d, key = d.get)

# print(max_min_of_values)