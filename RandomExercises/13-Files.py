
# myfile = open('test.txt', 'w')
# myfile.write('writing some text in this file\n')
# myfile.write("---------------------------------\n")
# myfile.write("Hello, world!\n")
# myfile.close()

# mynewhandle = open('test.txt', 'r')
# while True:
#     theline = mynewhandle.readline()
#     if len(theline) == 0:
#         break

#     print(theline, end='')

# mynewhandle.close()

# f = open("friends.txt", "r")
# xs = f.readlines()
# f.close()

# xs.sort()

# g = open("sortedfriends.txt", "w")
# for v in xs:
#     g.write(v)

# g.close()

# f = open("somefile.txt")
# content = f.read()
# f.close()

# words = content.split()
# print("There are {0} words in the file.".format(len(words)))

##################### BINARY FILES ################################

f = open("somefile.zip", "rb")
g = open("thecopy.zip", "wb")
while True:
    buf = f.read(1024)
    if len(buf) == 0:
        break
    g.write(buf)

f.close()
g.close()


def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if text[0] == "#":
            continue

        # Put any more processing logic here
        outfile.write(text)

    infile.close()
    outfile.close()
