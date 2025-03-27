import random

digits=list(range(10))
random.shuffle(digits)
secret_number=''.join(str(digits[i]) for i in range(4))

attempts=0
print("Welcome to Cows and Bulls!")
print("4-digit number with unique digits generated.")

while True:
    guess=input("Enter your guess:")
    if len(guess)!=4 or not guess.isdigit() or len(set(guess))!=4:
        print("Invalid input! Enter a 4-digit number with unique digits.")
        continue

    attempts+=1
    cows=0
    bulls=0

    for i in range(4):
        if guess[i] == secret_number[i]:
            cows+=1
        elif guess[i] in secret_number:
            bulls+=1

    print(f"{cows} Cows, {bulls} Bulls")

    if cows == 4:
        print(f"Congrats! You guessed it in {attempts} tries. The number was {secret_number}.")
        break