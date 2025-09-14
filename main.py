import random

choices = ['rock', 'paper', 'scissors']

win_condition = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

while True:
    user_choice = (input("Choose between 'rock', 'paper', 'scissors' "
                   "(or 'quit' to exit): ")
                   .lower()
                   .strip())

    if user_choice == "quit":
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice! Please select rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif win_condition[user_choice] == computer_choice:
        print((f"{user_choice.capitalize()} beats "
               f"{computer_choice.capitalize()}. You win!\n"))
    else:
        print(f"{user_choice.capitalize()} loses to "
              f"{computer_choice.capitalize()}. You lose!\n")
