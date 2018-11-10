cases = int(input())
week = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
for j in range(0,cases):
    sum = 0
    weekwork = 0
    goal = int(input())
    shedule = input()
    daily = shedule.split()

    for i in range(0,7):
        sum = sum + int(daily[i])
        print(sum)
        for i in range(0,7):
                weekwork= weekwork+int(daily[i])
        if sum >= goal%weekwork and goal%weekwork != 0:
			print("fe")
			print(week[i])
            break
        elif  goal%weekwork == 0:
            for i in range(0,7):
                if daily[6-i] != 0:
                    print(week[6-i])
                    break
                else:
                    continue
        else:
            continue
