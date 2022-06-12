T = int(input())

a = []
for i in range(T):
    A, B = list(map(int, input().split(' ')))
    a.append(A+B)
print(*a, sep='\n')