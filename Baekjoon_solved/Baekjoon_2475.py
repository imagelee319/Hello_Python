user=map(int, input().split())

sum=0
for i in user:
    sum+=(i**2)

print(sum%10)