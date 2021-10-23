import turtle

def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]): #if element is list, rsum called again with element as the argument
            tot += r_sum(element)
        else:
            tot += element

    return tot

def r_max(nxs):
    """
    Find the maximum in a recursive structure of lists
    within other lists.
    Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest

# print(r_max([2, 9, [1, 13], 8, 6]))
# print(r_max([2, [[100, 7], 90], [1, 13], 8, 6]))
# print(r_max(["joe", ["sam", "ben"]]))

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)


wn = turtle.Screen() 
wn.bgcolor("lightgreen")
t = turtle.Turtle()
t.color('blue')
t.pensize(3)
t.speed(10)



koch(t,3,300)

wn.mainloop()