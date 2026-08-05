try:
    num=int(input("Enter number :"))
    result=10/num
    print(result)
except ValueError:
    print("invalid number")
else:
    print("calculation successful")
finally:
    print("program ended, thank you for using")