
# def test(alist):
#     a = []
#     for num in alist:
#         a = a.append(num%11)

#     return a

# l = [54,26,93,17,77,31]
# print(test(l))

def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum%tablesize

print(hash('asdasdss', 11))