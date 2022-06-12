user_in = []

for i in range(10):
    user = int(input()) % 42
    user_in.append(user)

final = set(user_in)

print(len(final))
