import random

def human_guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

def ai_guess_the_number():
    secret_number = random.randint(1, 100)
    low, high = 1, 100
    attempts = 0

    while True:
        # AI guesses the middle of the current range
        guess = (low + high) // 2
        attempts += 1

        print(f"The AI guesses: {guess}")

        if guess == secret_number:
            print(f"The AI guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. AI adjusts its range.")
            low = guess + 1
        else:
            print("Too high. AI adjusts its range.")
            high = guess - 1

if __name__ == "__main__":
    print("Let's play Guess the Number!")
    print("1. Human vs Computer")
    print("2. Computer vs Computer")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        human_guess_the_number()
    elif choice == '2':
        ai_guess_the_number()
    else:
        print("Invalid choice. Please enter 1 or 2.")
