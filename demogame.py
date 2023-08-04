import random

def read_words_from_file(filename):
    with open(filename, 'r') as file:
        words = [word.strip() for word in file]
    return words

def encode_word(word):
    encoded = list(word)
    word_length = len(word)
    num_underscore = random.randint(1, word_length - 1)
    indices = random.sample(range(word_length), num_underscore)
    
    for index in indices:
        encoded[index] = '_'
    
    return ''.join(encoded)

def main():
    filename = "rookie.txt"
    words = read_words_from_file(filename)
    
    if not words:
        print("No words found in the file.")
        return
    
    chosen_word = random.choice(words)
    encoded_word = encode_word(chosen_word)

    print("Welcome to the Word Guessing Game!")
    print(f"Guess the word: {encoded_word}")

    attempts = 3
    while attempts > 0:
        user_guess = input("Enter your guess: ").strip().lower()
        if user_guess == chosen_word:
            print("Congratulations! You guessed the word correctly!")
            break
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
    else:
        print(f"Sorry, you couldn't guess the word. The word was: {chosen_word}")

if __name__ == "__main__":
    main()
