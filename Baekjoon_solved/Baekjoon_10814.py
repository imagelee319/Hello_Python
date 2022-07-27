join = []
for i in range(int(input())):
    age, name = input().split()
    age = int(age)
    join.append([i, age, name])

join.sort(key=lambda x: (x[1], x[0]))

for i in range(len(join)):
    print(join[i][1],join[i][2])
