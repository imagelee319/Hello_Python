user = input()
user_sp = user.split()

H = int(user_sp[0])
M = int(user_sp[1])

hour_value = H*60 + M

alarm = hour_value - 45
alarm_H = alarm // 60
alarm_M = alarm % 60

if alarm_H < 0:
    alarm_H = 24+alarm_H

print(alarm_H,alarm_M)


