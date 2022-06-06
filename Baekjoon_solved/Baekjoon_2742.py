N =int(input())

a = []
for i in range(1,N+1):
    a.append(i)

a.sort(reverse=True)

for j in a:
    print(j)