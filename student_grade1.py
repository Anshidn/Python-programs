def  get_marks():
    english = int(input("enter the english mark :"))
    maths = int(input("enter the maths mark : "))
    science = int(input("enter the science mark : "))
    social = int(input("enter the social mark : "))
    computer = int(input("enter the computer mark : "))
    return english,maths,science,social,computer
    
def calculate_total(english,maths,science,social,computer):
    total = english +maths+science+social+computer
    return total
    
def calculate_average(english,maths,science,social,computer) :
    total = english + maths + science + social + computer
    average = total / 5
    return average
    
def find_grade(average) :
    average = total / 5
    if average >= 90 and average <= 100 :
         return "A"
    elif average >= 80 and average <= 89 :
         return "B"
    elif average >= 70 and average <= 79 :
        return "C"
    elif average >= 60 and average <= 69 :
        return "D"
    else :
        return "Fail"
        
english,maths,science,social,computer =  get_marks()
total = calculate_total(english,maths,science,social,computer)
average = calculate_average(english,maths,science,social,computer)
grade = find_grade(average)


def display_function(total ,average , grade):
    print("total is", total)
    print("average is", average)
    print("grade is", grade)