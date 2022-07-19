case = int(input())

room_number = []
zero = '0'

for c in range(case):
    H, W, N = list(map(int, input().split()))
    room = str(N // H + 1)

    if N % H == 0:
        room = str(N // H)
        floor = str(H)
    else:
        room = str(N // H + 1)
        floor = str(N % H)

    if int(room) < 10:
        room = zero+room

    room_number.append(floor+room)

print(*room_number)

