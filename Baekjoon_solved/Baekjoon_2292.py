N = int(input())

init = 1
cnt = 1

while N > init:
    init += cnt * 6
    cnt += 1

print(cnt)