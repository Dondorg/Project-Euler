collatzDict = {1:4}

def nextCollatzStep(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1

def getCollatzChainLength(n):
    curr = n
    if curr in collatzDict:
        return collatzDict[curr]
    length = 1
    while curr != 1:
        curr = nextCollatzStep(curr)
        if curr in collatzDict:
            length += collatzDict[curr]
            break
        length += 1
    collatzDict[n] = length
    return length

maxlength = 1
maxindex = 1
for i in range(1, 1000000):
    currlen = getCollatzChainLength(i)
    if currlen > maxlength:
        maxlength = currlen
        maxindex = i

print(maxindex, maxlength)