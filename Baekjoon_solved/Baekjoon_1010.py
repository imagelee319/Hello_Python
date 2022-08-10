
for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    N_list = list(range(1, N+1))
    M_list = list(range(1, M+1))
    M_list.sort(reverse=True)

    coni = 1
    for i in M_list[:len(N_list)]:
        coni *= i

    conj = 1
    for j in N_list:
        conj *= j

    print(coni//conj)







