space = []
for i in range(int(input())):  # 입력한 수 만큼 단어 받아오기
    space.append(input())  # space라는 list에 단어들 추가

space = list(set(space))
space.sort()
space.sort(key=len)

print(*space, sep='\n')