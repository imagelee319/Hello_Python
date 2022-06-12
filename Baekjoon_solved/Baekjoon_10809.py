user = input()

ordlist = []
for i in range(97,123):
    ordlist.append(chr(i))

sum_list = []
for j in ordlist:
    one = user.find(j)
    sum_list.append(one)

print(*sum_list)
