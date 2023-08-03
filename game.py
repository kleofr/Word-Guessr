import os
from time import sleep
menu_key = 0
def start_of_game():
    #clears the screen
    os.system('cls')
    print(" | Welcome to WordGuessr 💥")
    print(" | by kleo ")
    print("----------------------------------------------")
    
def menu_of_game():
    #creating a reference of menu_key in the function
    global menu_key
    print(" | 1. Play")
    print(" | 2. Leaderboard")
    print(" | 3. Quit")
    menu_key = int(input(" | key: "))    

def play_game():
    os.system('cls')
    #Creating a reference of menu_key
    global menu_key
    play_game_menu()
    menu_key=int(input(" | key: "))
    if menu_key<0 or menu_key>3:
        print("Invalid Output, Please try again")
        sleep(1)
        play_game()
    else:
        if menu_key==0:
            main()

def play_game_menu():
    print(" | Select Difficulty")
    print("----------------------------------------------")
    print(" | 1. Easy")
    print(" | 2. Medium")
    print(" | 3. Hard")
    print(" | ")
    print(" | 0. Go back to menu")

def game_leaderboard():
    return 0

def main():
    start_of_game()
    menu_of_game()
    #user input validation
    if menu_key<1 or menu_key>3:
        print("| Invalid option, Please try again")
        sleep(1)
        os.system('cls')
        main()
    else:
        if menu_key==1:
            play_game()
        elif(menu_key==2):
            game_leaderboard()
        else:
            os.system('cls')
            exit()
main()
