# ------------- Imports -------------

import random
import os
from time import sleep

# ------------- Variables -------------

points = 0
status = True

# ------------- Game Logic code -------------

def get_words(filename): # --- Status: Completed not checked ---
    with open(filename, 'r') as file:
        words = [word.strip() for word in file]
        return words

def select_word(words): # --- Status: Completed not checked ---
    word = random.choice(words)
    return word

def encode_word(word,difficulty): # --- Status: Completed and checked ---        
    up = 0
    low = 0
    if difficulty == 1:
        up = len(word)//4
    elif difficulty == 2:
        up = len(word)//2         
    elif difficulty == 3:
        up = len(word)-2

    if up == 1:
        low = 1
    else:
        low = up-1
    num_of_underscores = random.randint(low, up) #0,1
    # ---------- Returns a list of positions where '_' is to be added ----------
    position_underscore = random.sample(range(len(word)), num_of_underscores)
    word_list = list(word)
    
    for pos in position_underscore:
        word_list[pos]='_'
    
    encoded_word = ''.join(word_list)        
    return encoded_word

def game_engine(difficulty, attempts): # --- Status: Completed not checked ---
    global points
    points = 0
    words_list = get_words('word_list')
    while attempts >= 1:
        os.system('cls')
        word = select_word(words_list).upper()
        encoded_word = encode_word(word, difficulty)
        print(" | Points: ", points)
        print(" | Attempts: ", attempts)
        print(" | Word: ", encoded_word)
        guess = input(" | Guess: ").upper()
        if guess == word:
            points+=1
            print(" | Correct guess!")
        else:
            attempts-=1
            print(" | Incorrect guess! attempts left: ", attempts)
            print(" | The word was : ", word)
    print(" | Game Over! Well Played")
    print(" | Total Points: ", points)        

def game_logic(key): # --- Status: Completed not checked ---
    # ------------- Rookie Game Mode -------------
    if key == 1:
        attempts = 5
        game_engine(key, attempts)
        
    
    # ------------- Medium Game Mode -------------
    elif key == 2:
        attempts = 3
        game_engine(key, attempts)
            
    # ------------- Maniac Game Mode -------------
    elif key == 3:
        attempts = 1
        game_engine(key, attempts)
        
# ------------- Game Menu code -------------

def main_menu(): # --- Status: Completed not checked ---
    #clears the screen
    os.system('cls')
    print(" | WordGuessr by kleo")
    print("----------------------------------------------")  

    #creating a reference of menu_key in the function
    global menu_key
    print(" | 1. Play")
    print(" | 2. Leaderboard")
    print(" | 3. Quit")
    menu_key = int(input(" | key: "))

def play_menu(): # --- Status: Completed not checked ---
    global menu_key
    os.system('cls')
    print(" | Select Difficulty")
    print("----------------------------------------------")  
    print(" | 1. Rookie 🌶")
    print(" | 2. Medium 🌶🌶")
    print(" | 3. Maniac 🌶🌶🌶")
    print(" | 0. Return back to Main Menu")
    menu_key = int(input(" | key: "))

def leaderboard_menu(): # TODO: Add a leaderboard menu
    pass

# ------------- Main Game code -------------

def main():
    global status
    
    while status == True:
        main_menu()
        if menu_key == 1:
            while status == True:
                play_menu()
                if menu_key == 1:
                    game_logic(1)
                    status = False
                elif menu_key == 2:
                    game_logic(2)
                    status = False
                elif menu_key == 3:
                    game_logic(3)
                    status = False
                elif menu_key == 0:
                    main()
                    status = False
        elif menu_key == 2:
            leaderboard_menu()
        elif menu_key == 3:
            exit()

main()

# ---------- Errors ----------
# 1.    Input: Elephant (while guessing) 
#       ValueError: Sample larger than population or is negative

# ---------- TODO: ----------
# 1. Add a good CLI UI while playing game
# 2. Fix the known errors