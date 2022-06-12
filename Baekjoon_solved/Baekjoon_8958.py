user = int(input())

# OX_sum = []

for i in range(user):
	OX = input().split('X')
	# OX_sum.append(OX)
	sum = 0
	for j in OX:
		for x in range(len(j)):
			sum+=(x+1)
	print(sum)