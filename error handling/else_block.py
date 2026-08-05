try:
    num =int(input("Enter number : "))
    result=10/num
    print("result :", result)
except ValueError:
    print("Enter a valid number")
else:
    print("Calculation successful ")