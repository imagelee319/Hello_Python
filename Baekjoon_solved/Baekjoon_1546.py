sub=int(input())
score=map(int, input().split())
score=list(score)

M=max(score)

sum=0
for i in score:
    new=i/M*100
    sum+=new
print(sum/sub)
