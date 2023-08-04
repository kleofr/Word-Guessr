# ------------- Imports -------------

import random
import os
from time import sleep

# ------------- Variables -------------

points = 0
attempts = 0

# ------------- Game Logic code -------------

def get_words(filename): # --- Status: Completed not checked ---
    with open(filename, 'r') as file:
        words = [word.strip() for word in file]
        return words

def select_word(words): # --- Status: Completed not checked ---
    word = random.choice(words)
    return word

def encode_word(word): #TODO: Encode word with '_' at random places
    return encoded_word

def game_engine(filename): # --- Status: Completed not checked ---
    global points
    global attempts
    words_list = get_words(filename)
    while attempts > 1:
        word = select_word(words_list)
        encoded_word = encode_word(word)
        print(" | Points: ", points)
        print(" | Attempts: ", attempts)
        print(" | Word: ", encoded_word)
        guess = input(" | Guess: ")
        if guess == word:
            points=+1
            print(" | Correct guess!")
        else:
            attempts=-1
            print(" | Incorrect guess! attempts left: ", attempts)
    print(" | Game Over! Well Played")
    print(" | Total Points: ", points)        

def game_logic(key): # --- Status: Completed not checked ---
    # ------------- Rookie Game Mode -------------
    if key == 1:
        global attempts
        global points
        attempts = 5
        points = 0
        game_engine('rookie.txt')
        
    
    # ------------- Medium Game Mode -------------
    elif key == 2:
        global attempts
        global points
        attempts = 3
        points = 0
        game_engine('medium.txt')
            
    # ------------- Maniac Game Mode -------------
    elif key == 3:
        global attempts
        global points
        attempts = 1
        points = 0
        game_engine('maniac.txt')
        
# ------------- Game Menu code -------------

def main_menu():
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

def play_menu():
    global menu_key
    os.system('cls')
    print(" | Select Difficulty")
    print("----------------------------------------------")  
    print(" | 1. Rookie 🌶")
    print(" | 2. Medium 🌶🌶")
    print(" | 3. Maniac 🌶🌶🌶")
    print(" | 0. Return back to Main Menu")
    menu_key = int(input(" | key: "))

def leaderboard_menu():
    pass

# ------------- Main Game code -------------

def main():
    pass

main()
