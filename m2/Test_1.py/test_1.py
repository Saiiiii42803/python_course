lives = 5
secret_number = 27

print("Number guessing game")
print("guesses left: ", lives)
guess = int(input("Enter your guess in the number: "))

while lives > 0:
    if guess == secret_number:
        print()
        print("=== You win ===")
        print("guesses left: ", lives)
    else:
        
        print()
        if lives > 1:
            print("=== Try Again ===")
        else:
            print("=== You Lose ===")
        lives = lives - 1
        if lives > 1:
            print("guesses left: ", lives)
            guess = int(input("Enter your guess in the number: "))
            if guess = 