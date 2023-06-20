import math

#naive

def getTriangleNumber(n):
    return (n*(n+1)) / 2

def getDivisorCount(number):
    count = 0
    for i in range(1, math.floor(math.sqrt(number))):
        if number % i == 0:
            count += 2
    if math.sqrt(number)**2 == number:
        count -= 1
    return count

def naive(divisorCount):
    i = 1
    while getDivisorCount((getTriangleNumber(i))) < divisorCount:
        i += 1
    print(getTriangleNumber(i))

#a little smarter

def lessnaive(divisorCount):
    count = 0
    n = 1
    tn = 0
    while count < divisorCount:
        tn = getTriangleNumber(n)
        if n % 2 ==0:
            count = getDivisorCount(n/2) * getDivisorCount(n+1)
        else:
            count = getDivisorCount(n) * getDivisorCount((n+1)/2)
        n+=1
    print(tn)

lessnaive(500)