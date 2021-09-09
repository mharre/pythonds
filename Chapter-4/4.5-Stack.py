from pythonds.basic import Stack

# class Stack:
#     def __init__(self):
#         self.items = []

#     def __repr__(self):
#         return str(self.items)

#     def is_empty(self):
#         return self.items == []

#     def push(self,item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def peek(self):
#         return self.items[len(self.items)-1]

#     def size(self):
#         return len(self.items)


# s = Stack()
# print(s.is_empty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.is_empty())
# s.push(8.4)
# print(s)
# print(s.pop())
# print(s.pop())
# print(s.size())
# print(s)

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))