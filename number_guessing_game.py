def generate_number():
    return 44

def get_guess():
    guessed_no =int(input(" guess a number : "))
    return guessed_no

def check_guess(generate_number , get_guess):
    if generate_number == get_guess :
        print("Correct! ")
        return "Correct! "
    elif generate_number > get_guess :
        print("Too low ")
    else:
       print("Too high ")

def play_game(attempt):
    number=generate_number()
    while True :
        guessed_number=get_guess()
        attempt = attempt + 1    
        if check_guess(number,guessed_number) =="Correct! ":
            print("total attempt : ", attempt)
            break
attempt=0

play_game(attempt)