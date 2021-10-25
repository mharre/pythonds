
# eng2sp = {"one": "uno", "two": "dos", "three": "tres"}

# for k in eng2sp:
#     print("Got key", k, "which maps to value", eng2sp[k])

# print(list(eng2sp.values())[1:])

alreadyknown = {0: 0, 1: 1}

def fib(n):
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-2)
        alreadyknown[n] = new_value
        # print(alreadyknown)
    return alreadyknown[n] 

print(fib(10))