n = int(input())
s = input()
sum =0
sum3 =0 
sum2 = 0
a = s.split()
for i in range(1,n+1):
    for j in range(0,n):
        if i == 3*j+1:
            sum = sum+int(a[i-1])
        elif i == 3*j+2:
            sum2 = sum2 + int(a[i-1])
        elif i == 3*j+3:
            sum3 = sum3 + int(a[i-1])
        else:
            print("")
        j = j+1
    i = i+1
print(sum,sum2,sum3)
