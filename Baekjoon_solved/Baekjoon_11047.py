n, k = map(int, input().split())
count = 0
coin = []

for _ in range(n):
    coin.append(int(input()))

for i in coin[::-1]:
    count += k // i
    k = k % i

print(count)