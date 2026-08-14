numbers=[[1,2],[3,4],[5,6]]
combined=[num for row in numbers  for num in row ]
print(combined) 

pair=[(x,y) for x in range(1,3) for y in range(1,3)]
print(pair) 