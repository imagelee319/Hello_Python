A = int(input())
B = int(input())
C = int(input())

multi = A*B*C
multi = str(multi)
multi_list = list(multi)
multi_int = list(map(int, multi_list))

for i in range(10):
    print(multi_int.count(i))