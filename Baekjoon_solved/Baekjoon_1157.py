user=input()
user = list(user.upper())

list_cnt=list(set(user))

dic_value=[]
for i in list_cnt:
    a=user.count(i)
    dic_value.append(a)

dic_cnt={}
for i in range(len(list_cnt)):
    dic_cnt[list_cnt[i]]=dic_value[i]


max=0
for x,y in dic_cnt.items():
    if y>max:
        max=y
        answer=x
        a=answer
    elif y<max:
        continue
    else:
        a='?'

print(a)
