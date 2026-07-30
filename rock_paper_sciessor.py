import random
def get_computer_choice():
    choice =["paper","rock","sciessor"]
    selected_choice = random.choice(choice)
    print(choice)
    return selected_choice

def get_player_choice():
    player_choice=input("select one : rock , paper, sciessor :")
    return player_choice
def check_winner(selected_choice,player_choice):
    if selected_choice == player_choice :
        return "Draw"
    elif (selected_choice == "paper" and player_choice == "sciessor") or (selected_choice == "sciessor" and player_choice == "rock") or (selected_choice == "rock" and player_choice == "paper"):
        return "You Win!!!"
    else :
        return "Computer Win"

def play_game():
    computer_chosen = get_computer_choice()
    print(computer_chosen)
    while True:
        player_chosen = get_player_choice()

        winner=check_winner(computer_chosen,player_chosen)
        if winner == "Computer Win":
            break
play_game()
    
