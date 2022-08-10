N, M = list(map(int, input().split()))
tree_H = list(map(int, input().split()))

start = 0
end = max(tree_H)
result = 0

while start <= end:
    mid = (start+end) // 2
    tmp = 0
    for i in range(N):
        if tree_H[i] - mid > 0:
            tmp += tree_H[i]-mid
            if tmp >= M:
                break
    if tmp >= M:
        result = mid
        start = mid+1
    else:
        end = mid-1
print(result)







