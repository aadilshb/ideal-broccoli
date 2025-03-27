import random

def load_words(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

def choose_word(word_list):
    return random.choice(word_list)

def guess_word(secret_word):
    guessed_letters=set()
    attempts=len(secret_word)+3
    print("\nGuess the word! It has",len(secret_word),"letters.")

    while attempts>0:
        display_word=''.join([letter if letter in guessed_letters else '_' for letter in secret_word])
        print("Word:",display_word)

        if display_word==secret_word:
            print("Congratulations! You guessed the word:",secret_word)
            break

        guess=input("Guess a letter:").strip().lower()

        if len(guess)!= 1 or not guess.isalpha():
            print("Invalid input! Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts-=1

        print("Attempts left:",attempts)

    if display_word!=secret_word:
        print("You ran out of attempts! The word was:",secret_word)

word_list=load_words("C:/Users/aadil/Desktop/Jumpwhere/assignment 9/words.txt")
secret_word=choose_word(word_list).lower()
guess_word(secret_word)
