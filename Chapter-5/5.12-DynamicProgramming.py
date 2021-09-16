def recDC(coinValueList,change,knownResults):
    minCoins = change
    if change in coinValueList:
       knownResults[change] = 1
       return 1
    elif knownResults[change] > 0:
       return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
          numCoins = 1 + recDC(coinValueList, change-i,
                               knownResults)
          if numCoins < minCoins:
             minCoins = numCoins
             knownResults[change] = minCoins
    return minCoins

# print(recDC([1,5,10,25],63,[0]*64)) 

def dpMakeChange(coinValueList,change,minCoins):
   for cents in range(change+1):
      coinCount = cents
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
      minCoins[cents] = coinCount
   return minCoins[change]

def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integers only'
    if n in [0,1]:
        return 1
    return n*(factorial(n-1))

# print(factorial(-4))

def fib(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integers only'
    if n in [0,1]:
        return n
    return fib(n-2) + fib(n-1)

print(fib(10))