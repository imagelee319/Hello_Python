testcase = int(input())

for cnt in range(testcase):
    k = int(input())
    n = int(input())

    ex = [list(range(1, n+1))]
    for floor in range(1, k+1):
        tmp = []
        for room in range(1, n+1):
            tmp.append(sum(ex[floor-1][:room]))
        ex.append(tmp)
    print(ex[k][n-1])








