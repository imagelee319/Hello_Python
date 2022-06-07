user = int(input())

if user % 4 == 0 and user % 100 != 0:
    print(1)
elif user % 400 == 0:
    print(1)
else:
    print(0)