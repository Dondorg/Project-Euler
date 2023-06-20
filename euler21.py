def getDivisorsSum(n):
    divsum = 0
    for i in range(1, int(n*0.5)+1):
        if n % i == 0:
            divsum += i
    return divsum

def isAmicable(n):
    amigo = getDivisorsSum(n)
    if amigo == n:
        return (False, amigo)
    if getDivisorsSum(amigo) == n:
        return (True, amigo)
    return (False, amigo)

def solve():
    sums = 0
    for i in range(10000):
        hasFriend, friend = isAmicable(i)
        if hasFriend and friend < 10000:
            sums += friend + i
    return sums/2

print(solve())