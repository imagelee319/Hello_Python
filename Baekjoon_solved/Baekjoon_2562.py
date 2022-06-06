
b = []
for i in range(9):
    a = int(input())
    b.append(a)

max_num = max(b)
print(max_num)
print(b.index(max_num)+1)
