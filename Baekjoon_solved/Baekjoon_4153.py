a = []
b = []
while True:
    ex = list(map(int, input().split(' ')))

    if ex != [0, 0, 0]:
        ex.sort()
        if (ex[0]**2+ex[1]**2) == ex[2]**2:
            b.append('right')
        else:
            b.append('wrong')

    elif ex == [0, 0, 0]:
        break

print(*b, sep='\n')

