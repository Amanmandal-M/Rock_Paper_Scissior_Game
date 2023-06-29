import random

def get_user_choice():
    while True:
        user_choice = input("Enter your move (rock/paper/scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid input! Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"
    else:
        return "computer"

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "no"]:
            return play_again == "yes"
        else:
            print("Invalid input! Please enter yes or no.")

def play_game():
    user_wins = 0
    computer_wins = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        print(f"\nUser wins: {user_wins}")
        print(f"Computer wins: {computer_wins}")

        if not play_again():
            break

print("Welcome to Rock, Paper, Scissors!")
play_game()
print("Thanks for playing. Goodbye!")