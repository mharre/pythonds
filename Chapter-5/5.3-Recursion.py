from pythonds.basic import Stack

def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

# print(listsum([1,3,5,7,9]))

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
       return convertString[n]
   else:
        # print(n // base, base)
        # print(convertString[n % base])
        return toStr(n // base, base) + convertString[n % base]

# print(f'result: {toStr(1453,16)}')

def reverse(s):
    if s <= 1:
        return s
    return reverse(s[1:] + s[0])

def removeWhite(s):
    new_s = s.replace(' ', '').replace("'", '')
    return new_s

# print(removeWhite("madam i'm adam"))

rStack = Stack()

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))
print(toStr(10,2))

