numbers = [6,5,8,1,2,0,3,9,10,7]
large_no = 0

for n in numbers:
    if large_no < n:
        large_no = n
numbers.remove(large_no)
second_large_no = 0
for n in numbers:
    if second_large_no < n:
        second_large_no = n

print(second_large_no)