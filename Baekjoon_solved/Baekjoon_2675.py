T = int(input())

ex = {}
for i in range(T):
    S = input()

    S_sp = S.split()  # 숫자와 문자 분리

    R = int(S_sp[0])  # 첫번째 index를 int로 변경
    S = list(map(str, S_sp[1]))  # 두번째 index를 list 형태로 각각 분리

    P = []
    for i in S:
        P.append(i*R)  # 각각의 문자를 R만큼 반복 하여 P에 저장

    P = ''.join(P)  # 나누어져 있는 문자열을 공백 없이 합해줌

    ex.setdefault(P)

for key in ex.keys():
    print(key)


