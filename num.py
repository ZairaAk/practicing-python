import random

while True:
    number = random.randint(1, 100)
    print("\n Guess the number between 1 and 100.")
    attempts = 0

    while True:
        guess = int(input(" Your guess: "))
        attempts += 1

        if guess == number:
            print(f" Correct! You guessed it in {attempts} tries.")
            break
        elif guess < number:
            print("⬆ Too low! Try again.")
        else:
            print("⬇ Too high! Try again.")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print("The End!")
        break
