def fibbonaciSeq():
    f1 = 1
    f2 = 1
    while True:
        result = f1+f2
        f1 = f2
        f2 = result
        yield f2
i = 2
for f in fibbonaciSeq():
    i +=1
    if f >= int(10**999):
        print(i)
        break
