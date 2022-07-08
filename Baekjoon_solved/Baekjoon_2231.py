N = int(input())

low = N - (len(str(N)) * 9)

while True:
    if low < 0:
        low = 0
    S = sum(map(int, list(str(low)))) + low

    if S == N:
        break

    elif low == N:
        low = 0
        break

    else:
        low += 1
print(low)