user = list(map(int,input().split()))

dist_list = []

first = user[3]-user[1]
second = user[2]-user[0]
third = user[0]
forth = user[1]

dist_list.extend([first, second, third, forth])
print(min(dist_list))