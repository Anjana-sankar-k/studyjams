import random


def play_game():
    number_to_guess = random.randint(1, 20)
    attempts = 0
    print("I'm thinking of a number between 1 and 20.")


    while True:
        try:
            guess= int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Congrats! You guessed my number in {attempts} tries!")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
 