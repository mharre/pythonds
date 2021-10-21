
def add_vectors(u,v):
    a = []

    for i, vi in enumerate(v): 
        a.append(u[i] + vi) 
    
    return a

# print(add_vectors([1, 1], [1, 1]))
# print(add_vectors([1, 2], [1, 4])) 
# print(add_vectors([1, 2, 1], [1, 4, 3])) 

def scalar_mult(s,v):
    a = []

    for num in v:
        a.append(s * num)

    return a

# print(scalar_mult(5, [1,2]))
# print(scalar_mult(3, [1, 0, -1]))
# print(scalar_mult(7, [3, 0, 5, 11, 2]))

def dot_product(u, v):
    a = []
    for i, vi in enumerate(v):
        a.append(u[i] * vi)
 
    return sum(a)

# print(dot_product([1, 1], [1, 1]))
# print(dot_product([1, 2], [1, 4]))
# print(dot_product([1, 2, 1], [1, 4, 3]))

def replace(s, old, new):
    a = s.split(old)
    glue = new
    a = glue.join(a)

    return a

# print(replace('Mississippi', 'i', 'I'))
# s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
# print(replace(s,'om', 'am'))
# print(replace(s, "o", "a"))

