test  = int(input())
for i in range(0,test):
    q = input()
    hur = int(q.split()[0])
    power = int(q.split()[1])
    hurdles = input()
    hurdlepow = [int(i) for i in hurdles.split()]
    t = 0
    sum = 0
    for i in range(0,hur):
        if t%2 != 0 and t!=0:
            for i in range(0,hur):
                if hurdlepow[i]%2 == 0:
                    hurdlepow[i] = hurdlepow[i]-1
                else:
                    continue
            t = t+1
        elif t%2 == 0 and t != 0:
            for i in range(0,hur):
                if hurdlepow[i]%2 != 0:
                    hurdlepow[i] = hurdlepow[i]-1
                else:
					continue
            t = t+1
        else:
			continue
        print(hurdlepow)    
        for i in range(0,hur):
            sum = sum+hurdlepow[i]
            print(sum)
            if sum>=power:
                print("No")
                break
            else:
                print("yes"),
                print(power-sum)
                hurdlepow.remove(hurdlepow[i])
        break
