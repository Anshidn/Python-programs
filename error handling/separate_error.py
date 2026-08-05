try:
    num =int(input("enter number : "))
    result=10/num
    print("result :", result)
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("cannot divide by zero")
