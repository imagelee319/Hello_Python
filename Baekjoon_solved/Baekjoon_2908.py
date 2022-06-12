sang = list(input().split(' '))

sang[0] = sang[0][::-1]
sang[1] = sang[1][::-1]

print(max(sang))