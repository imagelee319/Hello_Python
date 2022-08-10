N, M = map(int, input().split())

chess = []
for i in range(N):
    chess.append(input())

case = ["BWBWBWBW", "WBWBWBWB"]

min_result = M*N

for i in range(N-8+1):
    for j in range(M-8+1):
        B_start_cnt = 0
        W_start_cnt = 0
        for x in range(8):
            for y in range(8):
                if chess[i+x][j+y] != case[x%2][y]:
                    B_start_cnt += 1
                if chess[i+x][j+y] != case[(x+1)%2][y]:
                    W_start_cnt += 1
        min_result = min(min_result, B_start_cnt, W_start_cnt)

print(min_result)



