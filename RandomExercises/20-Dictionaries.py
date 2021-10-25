import operator
import collections
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

print(multiply_values({'test':1, 'test1':3, 'test2': 4, 'test3': 2}))
