def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        # print(f'midpoint: {alist[midpoint]}')
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
                # print(f'last: {alist[last]}')
            else:
                first = midpoint+1
                # print(f'first: {alist[first]}')

    return found

# testlist = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
testlist = [ 17, 20, 26, 31, 44, 54, 55, 65, 77, 93 ]
# print(binarySearch(testlist, 3))
# print(binarySearch(testlist, 13))

binarySearch(testlist, 54)
# binarySearch(testlist, 13)
