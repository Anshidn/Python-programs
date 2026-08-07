numbers=[1,2,3,4,5,6,7,8,9,10]
num=[]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0 :
        num.append(numbers[i])
        

print(num)
total = 0
for i in range(len(num)):
    total=total+ num[i]
    print(total)
print(total)