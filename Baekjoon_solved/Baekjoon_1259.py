result = []
while True:
        user = input()
        if user == '0':
            break
        elif user[::-1] == user:
            result.append('yes')
        elif user[::-1] != user:
            result.append('no')
print(*result, sep='\n')
