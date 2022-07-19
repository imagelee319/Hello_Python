N, M = list(map(int, input().split()))
card = list(map(int, input().split()))

sample = 0
check = []

for a in range(len(card)):
    sample += card[a]

    for b in range(len(card)):
        if card[b] == card[a]:
            sample = card[a]
            pass
        else:
            for c in range(len(card)):
                if card[c] == card[a] or card[c] == card[b]:
                    sample = card[a]+card[b]
                    pass
                else:
                    sample = card[a]+card[b]+card[c]
                    if sample <= M:
                        check.append(sample)

print(max(check))
