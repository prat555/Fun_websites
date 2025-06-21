from random import randint

winning_score = 2
comp = 0
p = 0

print("Welcome to Rock-Paper-Scissors!")
print("First to", winning_score, "wins!")
print("Enter:")
print("1 or 'rock' for Rock")
print("2 or 'paper' for Paper")
print("3 or 'scissors' for Scissors")
print("'quit' or 'q' to exit the game\n")

while p < winning_score and comp < winning_score:
    print(f"Current score - Computer: {comp} | Player: {p}\n")
    player = input("Player, make your move: ").lower()

    if player in ["quit", "q"]:
        print("\nThanks for playing! Final scores:")
        print(f"Computer: {comp} | Player: {p}")
        break

    # Convert number input to word
    if player == "1":
        player = "rock"
    elif player == "2":
        player = "paper"
    elif player == "3":
        player = "scissors"

    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"\nComputer plays {computer}")

    if player not in ["rock", "paper", "scissors"]:
        print("Please enter a valid move! (1/rock, 2/paper, 3/scissors)\n")
        continue

    if player == computer:
        print("It's a tie!\n")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins!\n")
            p += 1
        else:
            print("Computer wins!\n")
            comp += 1
    elif player == "paper":
        if computer == "rock":
            print("Player wins!\n")
            p += 1
        else:
            print("Computer wins!\n")
            comp += 1
    elif player == "scissors":
        if computer == "paper":
            print("Player wins!\n")
            p += 1
        else:
            print("Computer wins!\n")
            comp += 1

# Only show final result if game wasn't quit early
if p < winning_score and comp < winning_score:
    pass  # Game was quit
else:
    print("\n=== Final Result ===")
    print(f"Computer: {comp} | Player: {p}")
    if comp > p:
        print("The computer wins the game!")
    elif p > comp:
        print("The player wins the game!")
    else:
        print("It's a tie overall!")
