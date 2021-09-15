import turtle
from random import randrange

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()

def help(n):
    n = randrange(1,15)
    return n

def tree(branchLen,t):
    if branchLen > 5:
        a = randrange(1,15)
        t.forward(branchLen)
        t.right(20)
        # t.pensize(abs(t.pensize()-1))
        tree(branchLen-help(a),t)
        t.left(40)
        tree(branchLen-help(a),t)
        t.right(20)
        t.backward(branchLen)


# def tree(branchLen,t):
#     if branchLen > 5:
#         t.forward(branchLen)
#         t.right(20)
#         # t.pensize(abs(t.pensize() - 1)) 
#         tree(branchLen-15,t)
#         t.left(40)
#         tree(branchLen-15,t)
#         t.right(20)
#         t.backward(branchLen)



def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.pensize(5)
    tree(75,t)
    myWin.exitonclick()


main()