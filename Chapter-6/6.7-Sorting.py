def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                # print(f'{alist[i]} - {alist[i+1]}')
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# alist = [54,26,93,17,77,31,44,55,20]
# alist1 = [54,26,93,17]
# bubbleSort(alist1)
# print(alist1)

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
